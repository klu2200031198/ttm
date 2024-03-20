from django.contrib import admin
from django.urls import path
from .views import*

urlpatterns = [
    path('hello2/', hello1),
    path('hello/',hello,name='hello'),
    path('',Homepage,name='Homepage'),
    path('Travel/',Travelpackage,name='Travelpackage'),
    path('print/',print_to_console,name='print_to_console'),
    path('p/',print1,name='print1'),
    path('ran1/',random1,name='random1'),
    path('randomotp/',randomotp,name='randomotp'),
    path('randomotp1/',randomotp1,name='randomotp1'),
    path('date/',getdate,name='getdate'),
    path('date1/',getdate1,name='getdate1'),
    path('tzfunctioncall/',tzfunctioncall,name='tzfunctioncall'),
    path('model/',model,name='model'),
    path('form/',registerloginfunction,name='registerloginfunction'),
    path('form1/',pie_chart,name='pie_chart'),
    path('places/',places,name='places'),
    path('page/',weatherpagecall,name='weatherpagecall'),
    path('weather/',weatherlogic,name='weatherlogic'),
    path('signup',signup, name='signup'),
    path('signup1',signup1, name='signup1'),
    path('login',login, name='login'),
    path('login1',login1, name='login1'),
    path('logout',logout, name='logout'),
    path('contactmail',contactmail,name='contactmail'),
    path('contact',contact, name='contact'),
]