from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

class Dog:  
  def __init__(self, name, breed, description, age):
    self.name = name
    self.breed = breed
    self.description = description
    self.age = age

dogs = [
  Dog('Benji', 'labrador retriever', 'happy demon', 1),
  Dog('Hachi', 'Akita', 'loyal yellow doggo', 50),
  Dog('Marley', 'labrador retriever', 'psychotic love bug', 8)
]

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def dogs_index(request):
    return render(request, 'dogs/index.html', {'dogs': dogs})