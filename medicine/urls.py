from django.urls import path

from . import views

urlpatterns = [
    path('',views.medicinesfind, name='medicinesfind'),
    path('search',views.search, name='search'),
    path('pharmacy.html',views.pharmacy),
    path('medicinesfind.html',views.medicinesfind),
    path('medsfind.php',views.medsfind),


]