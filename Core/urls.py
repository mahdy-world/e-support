from django.urls import path 
from . import views

app_name = 'Core'
urlpatterns = [
    path('', views.Index, name='Index'),
    path('div/', views.index_div, name='Index_div'),
    path('issue_list/<int:status>/', views.IssueList, name='IssueList'),
    path('issue_list_div/<int:status>/', views.IssueList_div, name='IssueList_div'),

]
