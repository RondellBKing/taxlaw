from django.db import models
from scrapy_djangoitem import DjangoItem

# Create your models here.


class County(models.Model):
    name = models.CharField(max_length=120)
    models = models.URLField()

    def __unicode__(self):
        return self.name


class Lien(models.Model):
#    doc_type = models.CharField(max_length=200)
#    county = models.ForeignKey(County, on_delete=models.CASCADE,)
#    url = models.URLField()
    headers = models.TextField()
    body = models.TextField()
    url = models.URLField()

    def __unicode__(self):
        return self.name


class LienItem(DjangoItem):
    django_model = Lien
