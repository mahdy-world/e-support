from django.db import models
from Auth.models import User
from Core.models import Issue
from datetime import datetime


class Files(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True, verbose_name="Files Name")
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE, verbose_name="issue")
    files = models.FileField(upload_to='files/')
    created = models.DateTimeField(default=datetime.now)

    def delete(self, using=None, keep_parents=False):
        self.files.storage.delete(self.files.name)
        super().delete()

    def __str__(self):
        return self.name


