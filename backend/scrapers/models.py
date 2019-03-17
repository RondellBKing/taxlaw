from django.db import models
from django.utils import timezone
from datetime import date

# Create your models here.

class County(models.Model):
    county = models.CharField(max_length=120)

    def _str_(self):
        return self.county

    def get_absolute_url(self):
        """Returns the url to access a particular instance of the model."""
        return reverse('model-detail-view', args=[str(self.id)])

class DocType(models.Model):
    doc_type = models.CharField(max_length=120)

    def _str_(self):
        return self.doc_type

    def get_absolute_url(self):
        """Returns the url to access a particular instance of the model."""
        return reverse('model-detail-view', args=[str(self.id)])

class DateRange(models.Model):
    start_date = models.DateField(default=date.today)
    end_tade = models.DateField()

    def _str_(self):
        return self.start_date
        return self.end_date

    def get_absolute_url(self):
        """Returns the url to access a particular instance of the model."""
        return reverse('model-detail-view', args=[str(self.id)])
