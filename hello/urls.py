from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # HOME PAGE
    path('exhibits/', views.exhibit_list, name='exhibit_list'),
    path('exhibits/create/', views.exhibit_create, name='exhibit_create'),
    path('exhibits/<int:pk>/edit/', views.exhibit_update, name='exhibit_update'),
    path('exhibits/<int:pk>/delete/', views.exhibit_delete, name='exhibit_delete'),
]
