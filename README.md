# bdnews-scraper

Web scraping with Scrapy and integrate with Django


</hr>

![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)
[![Open in Visual Studio Code](https://img.shields.io/static/v1?logo=visualstudiocode&label=&message=Open%20in%20Visual%20Studio%20Code&labelColor=2c2c32&color=007acc&logoColor=007acc)](https://github.dev/Nayemjaman/bdnews-scraper)

</hr>

Welcome to the bdnews-scraper repository!

In this project, I scraped news data (from [thedailystar.net](https://www.thedailystar.net/), [daily-sun.com](https://www.daily-sun.com/) ,[thefinancialexpress.com.bd](https://thefinancialexpress.com.bd/)) using scrapy and integrated it with Django. The data is stored in a PostgreSQL database.

Customizations:
- custom scrapy command to run scrapy spiders from django command line. (ex- `python manage.py <spider_name>`)



## Run   

Create a python virtual environment and run these commands from root directory-
```
pip insrall -r requirements.txt
```

This will run the django app-
```
python manage.py runserver
```

NB: Migrate before running the app
```
python manage.py makemigrations && python manage.py migrate
```

To run all spiders-

```
python run_crawler.py
```

To run a specific spider-
```
python manage.py <spider_name>
```
ex - `python manage.py dailystar`



## Built With
```

Django==4.1.8
django-cors-headers==3.14.0
psycopg2==2.9.6
requests==2.28.2
requests-file==1.5.1
Scrapy==2.8.0
scrapy-djangoitem==1.1.1
scrapy-user-agents==0.1.1

```
