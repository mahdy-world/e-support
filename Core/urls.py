from django.urls import path 
from .views import Index

app_name = 'Core'
urlpatterns = [
    path('', Index.as_view(), name="Index")
]
