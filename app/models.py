from django.db import models

# Create your models here.
class Article(models.Model):
        title = models.CharField(max_length=150)
        date = models.DateField()
        article = models.TextField(blank=True)

        class Meta:
            verbose_name = "English Article"