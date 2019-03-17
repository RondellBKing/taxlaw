from django.db import models

# Create your models here.

class County(models.Model):
    county = models.CharField(max_length=120)
    doc_type = models.CharField(max_length=120)

    def _str_(self):
        return self.county
