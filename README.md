# scrapy-ebooks
Python scrapy spiders for harvesting publicly available free ebook libraries. 

## Environment Setup
**Here are instructions for an Ubuntu 20.04 machine.**
If you don't got 'em:
```
$ sudo apt install python3 git
```

It is recommended to install and run [scrapy](https://scrapy.org/) in a virtual environment:
```
$ python3 -m venv scrapy
$ cd scrapy
$ source bin/activate
```
To exit the environment later:
```
$ deactivate
```

Next, install scrapy:
```
$ pip install scrapy
```

Get and run this project:
```
$ git clone https://github.com/nymcoy/scrapy-ebooks.git ebooks
$ cd ebooks
$ scrapy crawl survivorlib
```

[The Survivor Library](https://www.survivorlibrary.com/) is the only current scraping target in this project. When run, the books will download in a directory called **SurvivorLib** with category subdirectories. If interrupted and re-run, the spider will ignore already-downloaded books. When you're done, just move the directory where you would like.
