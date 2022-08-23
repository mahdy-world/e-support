from AdminMedule.models import *
from django.db import models
from Auth.models import User
from django.contrib.contenttypes.fields import GenericRelation
from comment.models import Comment


# Create your models here.

class Device(models.Model):
    station_name = models.CharField(max_length=50, verbose_name="Station Name", null=True, blank=True)
    office_name = models.CharField(max_length=50, verbose_name="Office Name", null=True, blank=True)
    serial_number = models.CharField(max_length=50, verbose_name="Serial Number", null=True, blank=True)

    def __str__(self):
        return self.serial_number


class Issue(models.Model):
    environment = models.ForeignKey(Environment, on_delete=models.CASCADE, verbose_name="Environment", null=True, blank=True)
    issue_class = models.ForeignKey(IssueClass, on_delete=models.CASCADE, verbose_name="Issue Class", null=True, blank=True)
    issue_type = models.ForeignKey(IssueType, on_delete=models.CASCADE, verbose_name="Issue Type", null=True,blank=True)
    priority = models.ForeignKey(Priroty, on_delete=models.CASCADE, verbose_name="Priority", null=True, blank=True)
    status = models.ForeignKey(Status, on_delete=models.CASCADE, verbose_name="Status", null=True, blank=True)
    reporter = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Reporter", null=True, blank=True)
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE, verbose_name = "Channel")
    module = models.ForeignKey(Module, on_delete=models.CASCADE, verbose_name="Module")
    device_serial = models.ForeignKey(Device, on_delete=models.CASCADE, null=True, blank=True,verbose_name="Device Serial")

    screen = models.CharField(max_length=100, verbose_name="Screen", null=True, blank=True)
    field = models.CharField(max_length=100, verbose_name="Field", null=True, blank=True)
    description = models.TextField(verbose_name="Description")
    # last_comment = models.TextField(verbose_name="Last Comment", null=True, blank=True)
    title = models.CharField(max_length=200, verbose_name="Title")
    jira_id = models.CharField(max_length=150, verbose_name="Jira Id", null=True, blank=True)
    creator = models.CharField(max_length=100, verbose_name= "Creator", null=True, blank=True)
    create= models.DateTimeField(verbose_name="Create Date", null=True, blank=True)
    last_update = models.DateTimeField(verbose_name="Last Update", null=True, blank=True)
    folder_id = models.IntegerField(verbose_name = "Folder Id", null=True, blank=True)

    affects_version = models.FloatField(verbose_name="Affects Version", null=True, blank=True)
    fix_version = models.FloatField(verbose_name="Fix Version", null=True, blank=True)
    supscription_type = models.CharField(max_length=50, null=True, blank=True, verbose_name="Supscription Type")
    train = models.CharField(max_length=50,null=True, blank=True, verbose_name="Train")
    station = models.ForeignKey(Station, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Station")
    comments = GenericRelation(Comment)

    from django.urls import reverse

    def get_absolute_url(self):
        return reverse('ONSite:IssueUpdate', kwargs={'pk': self.id})
    

GANDER = (
    (0, "Male"),
    (1, "Female")
)


class EnrUser(models.Model):
    user_name = models.CharField(max_length=50, verbose_name="Username")    
    password = models.CharField(max_length=50, verbose_name="Password")    
    last_name = models.CharField(max_length=50, verbose_name="Last Name")    
    first_name = models.CharField(max_length=50, verbose_name="First Name" , null=True, blank=True)    
    patronymic_name = models.CharField(max_length=50, verbose_name="Patronymic Name" , null=True, blank=True)    
    phone = models.CharField(max_length=50, verbose_name="Phone" , null=True, blank=True)
    gander = models.IntegerField(choices=GANDER, verbose_name="Gander" , null=True, blank=True)
    active = models.BooleanField(verbose_name="Active" , null=True, blank=True)
    groups = models.TextField(verbose_name="Groups" , null=True, blank=True)
    merchant_login = models.CharField(max_length=200, verbose_name="Marchent" , null=True, blank=True) 
    user = models.CharField(max_length=100, verbose_name="User" , null=True, blank=True)
    
    def __str__(self):
        return self.user_name 