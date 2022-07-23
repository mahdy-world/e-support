from django.db import models

# Create your models here.

class Tom(models.Model):
    merchant = models.CharField(max_length=50, verbose_name="Merchant")
    terminalId= models.CharField(max_length=50, verbose_name="Terminal Id")
    station = models.IntegerField(verbose_name="Station Id ")
    stationName= models.CharField(max_length=50, verbose_name="Station Name")
    officeName = models.CharField(max_length=50, verbose_name="Office Name")

    def __str__(self):
        return self.stationName
