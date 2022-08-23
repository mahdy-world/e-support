from django.contrib import admin
from .models import Issue, EnrUser
# Register your models here.
# @admin.register(Issue)
# class IssuesAdmin(admin.ModelAdmin):
#     list_display = ( "title", "jira_id" , "environment", "module",
#     "channel", "issue_type", "priority", "status", "affects_version")
#     list_filter = ("jira_id", "status","channel","module", "creator", "environment")


@admin.register(EnrUser)
class EnrUserAdmin(admin.ModelAdmin):
    list_display = ( "user_name", "password" , "last_name", "first_name",
    "active", "merchant_login")
    
    
    list_filter = ("user_name", "last_name","first_name","active", "merchant_login",)
    
    fieldsets = (
        (None, {
            'fields': ('user_name', 'password', 'last_name', 'first_name',
                    'merchant_login', 'active')
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('gander', 'groups', 'phone', 'patronymic_name', 'user'),
        }),
    )
    
