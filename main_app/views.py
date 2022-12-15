from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Dog, Toy
from .forms import FeedingForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
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
  available_toys = Toy.objects.exclude(id__in=dog.toys.values_list('id'))
  feeding_form = FeedingForm()
  return render(request, 'dogs/detail.html', {
    'dog': dog,
    'feeding_form': feeding_form,
    'toys': available_toys
    })

class DogUpdate(UpdateView):
  model = Dog
  fields = ['breed', 'description', 'age']

class DogDelete(DeleteView):
  model = Dog
  success_url = '/dogs/'
# alternate way:
# def delete(request, dog_id):
#   dog = Dog.objects.get(id = dog_id)
#   dog.delete()
#   return redirect('index')

class DogCreate(CreateView):
  model = Dog
  fields = '__all__'


def add_feeding(request, dog_id):
  form = FeedingForm(request.POST)

  if form.is_valid():
    new_feeding = form.save(commit=False)
    new_feeding.dog_id = dog_id
    new_feeding.save()
  
  return redirect('detail', dog_id = dog_id)

class ToyList(ListView):
  model = Toy

class ToyDetail(DetailView):
  model = Toy

class ToyCreate(CreateView):
  model=Toy
  fields='__all__'

class ToyUpdate(UpdateView):
  model = Toy
  fields = ['color', 'description']

class ToyDelete(DeleteView):
  model = Toy
  success_url = '/toys/'

def add_toy(request, dog_id, toy_id):
  Dog.objects.get(id=dog_id).toys.add(toy_id)
  return redirect('detail', dog_id = dog_id)

def delete_toy(request, dog_id, toy_id):
  Dog.objects.get(id=dog_id).toys.remove(toy_id)
  return redirect('detail', dog_id = dog_id)