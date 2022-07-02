from .models import *
from django.contrib import admin


@admin.register(Environment)
class EvairomentAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    list_filter = ("name", "id")
    
    
@admin.register(IssueType)
class IssueTypeAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    list_filter = ("name", "id")
    
@admin.register(Priroty)
class PrirotyAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    list_filter = ("name", "id")
    
@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    list_filter = ("name", "id")
    
@admin.register(IssueClass)
class IssueClassAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    list_filter = ("name", "id")
    
@admin.register(Channel)
class ChannelAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    list_filter = ("name", "id")
    
@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    list_filter = ("name", "id")


@admin.register(Station)
class StationAdmin(admin.ModelAdmin):
    list_display = ("english_name", "arabic_name", "station_type", "code", "merchant_name" )
    list_filter = ("english_name", "arabic_name","station_type", "code", "merchant_name" )