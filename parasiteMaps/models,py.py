from django.db import models


class Parasite(models.Model):
    name = models.CharField(max_length=50)
    contaminationMethod = models.CharField(max_length=255)
    symptoms = models.CharField(max_length=255)
    protection = models.CharField(max_length=255)
    distribution = models.FloatField()
