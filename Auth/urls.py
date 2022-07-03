from django.urls import path
from .views import *

app_name = "Auth"
urlpatterns = [
    path('users/login/', Login.as_view(), name='Login'),
    path('logout/', Logout.as_view(), name='Logout'),
    path('ChangePassword/', ChangePassword, name='ChangePassword'),
    path('AddNewUser/', create_user, name='create_user'),
    path('Users/', Users.as_view(), name='Users'),
    path('Users/<int:pk>/update/', UsersUpdate.as_view(), name='UsersUpdate'),

]