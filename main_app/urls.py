from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('dogs/', views.dogs_index, name='index'),
    path('dogs/<int:dog_id>/', views.dog_detail, name='detail'),
    path('dogs/create/', views.DogCreate.as_view(), name='dogs_create' ),
    path('dogs/<int:pk>/edit', views.DogUpdate.as_view(),name='dogs_update' ),
    path('dogs/<int:dog_id>/delete', views.delete,name='dogs_delete' ),
    path('dogs/<int:dog_id>/add_feeding/', views.add_feeding, name='add_feeding')

]