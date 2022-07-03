from django.urls import path
from .views import *

app_name = 'ONSite'
urlpatterns = [
    path('myIssue/', MyIssue.as_view(), name="MyIssue"),
    path('createIssue/', CreateIssue.as_view(), name="CreateIssue"),
    path('update_issue/<int:pk>/', IssueUpdate.as_view(), name='IssueUpdate'),
    path('files_update/<int:pk>/', FilesUpdate.as_view(), name='FilesUpdate'),
]