from django.urls import path
from django.conf.urls import url
from . import views


urlpatterns = [
    path('', views.main, name="main"),
    path('logout', views.Logout.as_view(), name='logout_page'),
    url(r'^table$', views.table_one, name='table'),
    url(r'^table_two$', views.table_two, name='table_two'),
    path('print', views.print, name='print')
]

