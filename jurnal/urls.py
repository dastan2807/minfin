from django.urls import path
from . import views

urlpatterns = [
    path('', views.AutoRegister.as_view(), name="auto_register"),
    path('/admin', views.JurnalCreate.as_view(), name="jurnal"),
]