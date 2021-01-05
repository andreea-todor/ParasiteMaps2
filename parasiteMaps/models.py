from django.db import models

class Parasite(models.Model):
    name = models.CharField(max_length=40, default=None)
    general_info = models.CharField(max_length=600)
    host = models.CharField(max_length=150)
    disease = models.CharField(max_length=65)
    geographic_distribution = models.CharField(max_length=400)
    prophylaxis = models.CharField(max_length=2100)

    def __str__(self):
        return self.name