from django.db import models



class Environment(models.Model):
    name = models.CharField(max_length=50, verbose_name="name")
    def __str__(self):
        return self.name
   
    
class IssueType(models.Model):
    name = models.CharField(max_length=50, verbose_name="name")
    icon = models.CharField(max_length=50, null=True, blank=True, verbose_name="icon")
    color = models.CharField(max_length=50, null=True, blank=True, verbose_name="color")
    def __str__(self):
        return self.name
    
    
class Priroty(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True, verbose_name="name")
    icon = models.CharField(max_length=50, null= True, blank=True, verbose_name="icon")
    color = models.CharField(max_length=50, null=True, blank=True, verbose_name="color")

    def __str__(self):
        return self.name
    
    
class Status(models.Model):
    name = models.CharField(max_length=50, verbose_name="name")
    color = models.CharField(max_length=50,null=True, blank=True,  verbose_name="Color Class")
    weight = models.IntegerField(null= True, blank=True, verbose_name="weight")
    def __str__(self):
        return self.name

    
class IssueClass(models.Model):
    name = models.CharField(max_length=50, verbose_name="name")
    def __str__(self):
        return self.name
    
    
class Channel(models.Model):
    name = models.CharField(max_length=50, verbose_name="name")
    def __str__(self):
        return self.name
    
    
class Module(models.Model):
    name = models.CharField(max_length=50, verbose_name="name")
    def __str__(self):
        return self.name
    

class Station(models.Model):
    station_type = models.CharField(max_length=20, verbose_name="Station Type")
    english_name = models.CharField(max_length=20, verbose_name="English Name")
    arabic_name = models.CharField(max_length=20, verbose_name="Station")
    code = models.IntegerField(verbose_name="Code")
    merchant_name = models.CharField(max_length=100, verbose_name="Merchant Name")
    
    def __str__(self):
        return self.english_name


class Office(models.Model):
    station = models.ForeignKey(Station, related_name="station_office", on_delete=models.CASCADE, verbose_name="Station")
    nameEn = models.CharField(max_length=50, null=True, blank=True, verbose_name="English Name")
    nameAr = models.CharField(max_length=50, null=True, blank=True, verbose_name="Arabic Name")

    def __str__(self):
        return self.nameAr
