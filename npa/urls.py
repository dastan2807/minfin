from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    # path('', views.Npa.as_view(), name="npa"),
  
    path('', views.npa, name="npa"),
    path('pdf', views.pdf, name="pdf")
]

