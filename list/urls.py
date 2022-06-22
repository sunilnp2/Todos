from ast import Delete
from django.urls import path
from list.views import *
app_name = 'list'
urlpatterns = [
    path('', HomeView.as_view(), name= 'home'),

    path('signup', signup, name= 'signup'),
    path('login/', login, name='login'),
    path('logout', logout, name = 'logout'),
    path('delete/<int:pk>', delete, name='delete'),
    path('update/<int:pk>', update, name='update'),
    path('complete/<int:pk>', complete,name= 'complete'),
]
