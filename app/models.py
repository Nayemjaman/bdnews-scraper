from django.db import models

# Create your models here.
class Article(models.Model):
        title = models.CharField(max_length=500)
        date = models.CharField(max_length=200)
        article = models.TextField(blank=True)

        def __str__(self) -> str:
              return self.title

        class Meta:
            verbose_name = "English Article"