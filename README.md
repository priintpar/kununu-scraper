# kununu scraper 2025

A tool to scrape company reviews from kununu.com with the [Scrapy framework](https://docs.scrapy.org/en/latest/intro/overview.html) (based on Python).

### Prerequisites

+ Scrapy installed on your machine<br />
 &nbsp; &nbsp; &nbsp; &nbsp;  → Follow this installation guide: https://docs.scrapy.org/en/latest/intro/install.html
 
### How to run this project

1. Clone this repo into your scrapy folder. *(where the default tutorial folder should exist after your installation)*
2. Your folder structure should look something like this:

         scrapy/kununu2025/
            README.md
            scrapy.cfg
            __init__.p
            kununu2025/
                    items.py
                    middlewares.py
                    pipelines.py
                    settings.py
                    spiders/
                       __init__.py
                       kununu2025_spider.py

        scrapy/tutorial/
            scrapy.cfg
            tutorial/
                    items.py
                    ...

3. Open your python CLI (I used miniconda prompt):<br />
       3.1 Navigate into the projects top level folder → (scrapy/kununu2025)<br />
       3.2 Execute the following command: scrapy crawl kununu2025 -O ratings.csv
       
4. By default it scrapes reviews from GTÜ.<br />
   You can change this by adapting the links within the "kununu2025_spider.py" - Spider.

This project is based on the code from https://github.com/TheWoops/Web-Scraping
Shoutouts to him. It just did not work anymore for me.




    
