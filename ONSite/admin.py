from dataclasses import fields
from django.contrib import admin
from django.contrib import admin
from django import forms

from Core.models import*

@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ("serial_number", "station_name", "office_name")
    list_filter = ("serial_number", "station_name", "office_name")


# class AttachedFile(forms.ModelForm):
#     class Meta:
#         model = OnSite
#         widgets = {
#             'file': forms.ClearableFileInput(attrs={'multiple': True})
#         }
#         fields = '__all__'
#
#
# @admin.register(OnSite)
# class OnSiteAdmin(admin.ModelAdmin):
#     list_display = ("title", "issue_type", "priority", "module", "description")
#     list_filter = ("title", "issue_type", "priority", "module")
#     form = AttachedFile
#
#
#