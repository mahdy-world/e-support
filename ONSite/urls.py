from django.urls import path
from .views import  CreateHotIssue,CreateFullIssue, print_issue, IssueUpdate, FilesUpdate, DeleteFiles, FilesUpdateDive, AssignIssue, IssueDetails, FollwerAssign

app_name = 'ONSite'
urlpatterns = [
    # path('myIssue/', MyIssue.as_view(), name="MyIssue"),
    path('createHotIssue/', CreateHotIssue.as_view(), name="CreateHotIssue"),
    path('createFullIssue/', CreateFullIssue.as_view(), name="CreateFullIssue"),
    path('update_issue/<int:pk>/', IssueUpdate.as_view(), name='IssueUpdate'),
    path('files_update/<int:pk>/', FilesUpdate.as_view(), name='FilesUpdate'),
    path('delete_files/', DeleteFiles, name='DeleteFiles'),
    path('div_files/<int:pk>/', FilesUpdateDive.as_view(), name='FilesUpdateDive'),
    path('assign_issue/<int:pk>/', AssignIssue.as_view(), name='AssignIssue'),
    path('assign_follwer/<int:pk>/', FollwerAssign.as_view(), name='FollwerAssign'),
    path('issue_details/<int:pk>/', IssueDetails.as_view(), name='IssueDetails'),
    path('issue_print/<int:pk>/', print_issue, name='PrintIssue')
]