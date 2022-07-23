
from django.contrib import admin
from .models import Tom
# Register your models here.
@admin.register(Tom)
class TomAdmin(admin.ModelAdmin):
    list_display = ("merchant","terminalId","station","stationName","officeName")

