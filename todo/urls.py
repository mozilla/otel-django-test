from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("__lbheartbeat__/", views.lbheartbeat),
    path("__lbheartbeat__", views.lbheartbeat),
    path('add/', views.add_item, name='add_item'),
    path('delete/<int:item_id>/', views.delete_item, name='delete_item'),
]