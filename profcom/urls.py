from django.urls import path
from . import views

from minfin import settings
from django.conf.urls.static import static

urlpatterns = [
    path('item_1', views.item_1, name="item_1"),
    path('item_2', views.item_2, name="item_2"),
    path('item_3', views.item_3, name="item_3")
]