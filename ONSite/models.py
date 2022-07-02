from django.db import models
from Auth.models import User
from AdminMedule.models import*
from Core.models import Issue


class Files(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True, verbose_name="Files Name")
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE, verbose_name="issue")
    files = models.FileField(upload_to='files/')

    def __str__(self):
        return self.name
    
    
