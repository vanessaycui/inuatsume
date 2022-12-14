from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('dogs/', views.dogs_index, name='index'),
    path('dogs/<int:dog_id>/', views.dog_detail, name='detail'),
    path('dogs/<int:dog_id>/add_feeding/', views.add_feeding, name='add_feeding')

]