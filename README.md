# kununu scraper

A tool to scrape company reviews from kununu.com with the [Scrapy framework](https://docs.scrapy.org/en/latest/intro/overview.html) (based on Python).

### Prerequisites

+ Scrapy installed on your machine<br />
 &nbsp; &nbsp; &nbsp; &nbsp;  → Follow this installation guide: https://docs.scrapy.org/en/latest/intro/install.html
 
### How to run this project

1. Clone this repo into your scrapy folder. *(where the default tutorial folder should exist after your installation)*
2. Your folder structure should look something like this:

         scrapy/kununu/
            README.md
            scrapy.cfg
            __init__.p
            kununu/
                    items.py
                    middlewares.py
                    pipelines.py
                    settings.py
                    spiders/
                       __init__.py
                       kununu.py

        scrapy/tutorial/
            scrapy.cfg
            tutorial/
                    items.py
                    ...

3. Open your python CLI (I used anaconda prompt):<br />
       3.1 Navigate into the spider folder within scrapy folder → (scrapy/kununu/kununu/spiders)<br />
       3.2 Execute the following command: scrapy runspider kununu.py
       
4. By default it scrapes reviews from Telefonica Germany.<br />
   You can change this by adapting the links within the "kununu.py" - Spider.


This project is based on the code from https://github.com/TheWoops/Web-Scraping Shoutouts to him. It just did not work anymore for me.




    
