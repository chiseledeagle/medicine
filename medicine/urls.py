from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.heading, name='home'),
    path('patient', views.patient, name="patient"),
    path('home.html',views.home),
    path('search',views.search, name='search'),
    path('searchhelp',views.searchhelp, name='searchhelp'),
    path('Find_Healthcare.html',views.pharmacy),
    path('Find_Medicine.html',views.medicinesfind),
    path('Customer_care.html',views.custom),
    path('result3.html',views.patient),
    path('reminder.html',views.reminder),
    path('welcome.html',views.welcome),
    path('signup.html',views.signup),
    path('login.html',views.login),
    path('signup',views.signup),
    path('login',views.login)
]
