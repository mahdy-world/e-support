from django.urls import path
from .views import MyIssue, CreateIssue, IssueUpdate, FilesUpdate, DeleteFiles, FilesUpdateDive, AssignIssue

app_name = 'ONSite'
urlpatterns = [
    path('myIssue/', MyIssue.as_view(), name="MyIssue"),
    path('createIssue/', CreateIssue.as_view(), name="CreateIssue"),
    path('update_issue/<int:pk>/', IssueUpdate.as_view(), name='IssueUpdate'),
    path('files_update/<int:pk>/', FilesUpdate.as_view(), name='FilesUpdate'),
    path('delete_files/', DeleteFiles, name='DeleteFiles'),
    path('div_files/<int:pk>/',FilesUpdateDive.as_view(), name='FilesUpdateDive'),
    path('assign_issue/<int:pk>/',AssignIssue.as_view(), name='AssignIssue'),
]