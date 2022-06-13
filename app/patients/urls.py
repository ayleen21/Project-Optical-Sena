from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from app.patients.views.views import PatientListView
#agrupar mi listas
app_name='patients'

urlpatterns = [
    path('patients/list/',PatientListView.as_view(),name='patients_list'),
  
]


