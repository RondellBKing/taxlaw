from django.db import models

# Create your models here.

class County(models.Model):
    county = models.CharField(max_length=120)

    def _str_(self):
        return self.county

class DocType(models.Model):
    doc_type = models.CharField(max_length=120)

    def _str_(self):
        return self.doc_type

class DateRange(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()

    def _str_(self):
        return self.start_date
        return self.end_date
