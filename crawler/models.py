from django.db import models


# Create your models here.
class New(models.Model):
    news_url = models.CharField(max_length=150, blank=True, null=True)
    category = models.CharField(max_length=150,blank=True,null=True)
    # sub_categories = models.CharField(max_length=150)
    headline = models.CharField(max_length=500,blank=True,null=True)
    date = models.CharField(max_length=150,blank=True,null=True)
    images = models.CharField(max_length=500,blank=True,null=True)
    news = models.TextField(blank=True,null=True)
    

    def __str__(self):
        return self.headline