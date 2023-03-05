# Dailystar news scraper
</hr>

![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)
![HTML, CSS and BOOTSTRAP](https://img.shields.io/badge/HTML,%20CSS%20and-BOOTSTRAP-1f425f.svg)
[![Open in Visual Studio Code](https://img.shields.io/static/v1?logo=visualstudiocode&label=&message=Open%20in%20Visual%20Studio%20Code&labelColor=2c2c32&color=007acc&logoColor=007acc)](https://github.dev/Nayemjaman/dailystarscraper)

</hr>

Welcome to the dailystarscraper repository!

In this project, I scraped news data (from [thedailystar.net](https://www.thedailystar.net)) using scrapy and integrated it with Django. The data is stored in a SQLite database.

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


## Built With

```
Django==4.1.5
requests==2.28.1
requests-file==1.5.1
Scrapy==2.7.1
scrapy-djangoitem==1.1.1
scrapy-user-agents==0.1.1
service-identity==21.1.0
urllib3==1.26.13
user-agents==2.2.0
lxml==4.9.2
pycparser==2.21
```

