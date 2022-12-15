from django.urls import path
from . import views

urlpatterns = [
    #general views
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('dogs/', views.dogs_index, name='index'),
    path('dogs/<int:dog_id>/', views.dog_detail, name='detail'),
    #Dogs
    path('dogs/create/', views.DogCreate.as_view(), name='dogs_create' ),
    path('dogs/<int:pk>/edit', views.DogUpdate.as_view(),name='dogs_update' ),
    path('dogs/<int:pk>/delete', views.DogDelete.as_view(),name='dogs_delete' ),
    #feeding
    path('dogs/<int:dog_id>/add_feeding/', views.add_feeding, name='add_feeding'),
    #Toys
    path('toys/', views.ToyList.as_view(), name='toys_index'),
    path('toys/create/', views.ToyCreate.as_view(), name='toys_create' ),
    path('toys/<int:pk>/', views.ToyDetail.as_view(), name='toys_detail' ),
    path('toys/<int:pk>/update', views.ToyUpdate.as_view(), name='toys_update'),
    path('toys/<int:pk>/delete', views.ToyDelete.as_view(), name='toys_delete'),
    #Toy <> Dog M:M
    path('dogs/<int:dog_id>/toys/<int:toy_id>/add', views.add_toy, name='add_toy'),
    path('dogs/<int:dog_id>/toys/<int:toy_id>/delete', views.delete_toy, name='delete_toy'),

]