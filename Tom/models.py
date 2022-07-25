from django.db import models

# Create your models here.

class Tom(models.Model):
    merchant = models.CharField(max_length=50, null=True, blank=True, verbose_name="Merchant")
    deviceNum= models.CharField(max_length=50, null=True, blank=True,  verbose_name="DeviceNum")
    station = models.IntegerField(null=True, blank=True, verbose_name="Station Code")
    stationName= models.CharField(max_length=50, null=True, blank=True, verbose_name="Station Name")
    officeEn = models.CharField(max_length=50, null=True, blank=True, verbose_name="OfficeEn")
    officeAr = models.CharField(max_length=50,null=True, blank=True, verbose_name="OfficeAr")
    window = models.CharField(max_length=50, null=True, blank=True, verbose_name="Window")
    type = models.CharField(max_length=50, null=True, blank=True, verbose_name="Type")


    def __str__(self):
        return self.stationName
