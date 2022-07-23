from django.urls import path, include
from .views import TomCreateApiVeiw

app_name = 'Tom'
urlpatterns = [
    path('create/', TomCreateApiVeiw.as_view(), name="Create")
]