from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Dog
from .forms import FeedingForm
# Create your views here.


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def dogs_index(request):
  dogs = Dog.objects.all()
  return render(request, 'dogs/index.html', {'dogs': dogs})

def dog_detail(request, dog_id):
  dog = Dog.objects.get(id=dog_id)
  feeding_form = FeedingForm()

  return render(request, 'dogs/detail.html', {
    'dog': dog,
    'feeding_form': feeding_form
    })

def add_feeding(request, dog_id):
  form = FeedingForm(request.POST)

  if form.is_valid():
    new_feeding = form.save(commit=False)
    new_feeding.dog_id = dog_id
    new_feeding.save()
  
  return redirect('detail', dog_id = dog_id)