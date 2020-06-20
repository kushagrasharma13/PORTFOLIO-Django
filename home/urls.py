from django.contrib import admin
from django.urls import path
from home import views

app_name='home'
urlpatterns = [
    path('', views.index,name='home'),
    path('get_value',views.get_value,name='get_value')
]