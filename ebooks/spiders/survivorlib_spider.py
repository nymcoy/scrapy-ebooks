import scrapy
import os

DOWNLOAD_TIMEOUT = 1000 # Some files are large and may timeout

class SurvivorlibSpider(scrapy.Spider):
    name = "survivorlib"

    start_urls = [
        'https://www.survivorlibrary.com/index.php/library-download',
    ]

    def parse(self, response):
        # Skip New Items category
        for link in response.css('td a')[1:]:
            category = link.css('::text').get()
            yield response.follow(link, callback=self.parse_category, cb_kwargs={"category": category})
    
    def parse_category(self, response, category):
        for row in response.css('tr'):
            link = row.css('a::attr(href)').get()
            title = row.css('td:first-of-type::text').get()
            
            # Ignore blank rows
            try:
                # TODO: Don't hardcode base save dir
                path = "/".join([
                    'SurvivorLib',
                    category.strip(),
                    title.strip()])
                path += link[-4:]
            except:
                continue
            
            # Don't re-download already downloaded files.
            if os.path.exists(path):
                self.log(f'SKIPPING: {link}')
                continue

            # Ignore external links
            if link[0] == '/':
                self.log(f'DOWNLOADING: {link}')
                yield response.follow(link, callback=self.download_file, cb_kwargs={"category": category,"title": title, "path":path})

    def download_file(self, response, category, title, path):
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, 'wb') as f:
            f.write(response.body)
        self.log(f'SAVED: {path}')