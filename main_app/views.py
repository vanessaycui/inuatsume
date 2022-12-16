from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Dog, Toy
from .forms import FeedingForm
#this is for creating model forms
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
#this is for authentications
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
# Import the login_required decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def dogs_index(request):
  dogs = Dog.objects.filter(user=request.user)
  return render(request, 'dogs/index.html', {'dogs': dogs})

@login_required
def dog_detail(request, dog_id):
  dog = Dog.objects.get(id=dog_id)
  available_toys = Toy.objects.exclude(id__in=dog.toys.values_list('id'))
  feeding_form = FeedingForm()
  return render(request, 'dogs/detail.html', {
    'dog': dog,
    'feeding_form': feeding_form,
    'toys': available_toys
    })

class DogUpdate(LoginRequiredMixin, UpdateView):
  model = Dog
  fields = ['breed', 'description', 'age']

class DogDelete(LoginRequiredMixin, DeleteView):
  model = Dog
  success_url = '/dogs/'
# alternate way:
# def delete(request, dog_id):
#   dog = Dog.objects.get(id = dog_id)
#   dog.delete()
#   return redirect('index')

class DogCreate(LoginRequiredMixin, CreateView):
  model = Dog
  fields = ["name", "breed", "description", "age"]

  def form_valid(self, form):
    form.instance.user = self.request.user  
    return super().form_valid(form)

@login_required
def add_feeding(request, dog_id):
  form = FeedingForm(request.POST)

  if form.is_valid():
    new_feeding = form.save(commit=False)
    new_feeding.dog_id = dog_id
    new_feeding.save()
  
  return redirect('detail', dog_id = dog_id)

class ToyList(LoginRequiredMixin, ListView):
  model = Toy

class ToyDetail(LoginRequiredMixin, DetailView):
  model = Toy

class ToyCreate(LoginRequiredMixin, CreateView):
  model=Toy
  fields='__all__'

class ToyUpdate(LoginRequiredMixin, UpdateView):
  model = Toy
  fields = ['color', 'description']

class ToyDelete(LoginRequiredMixin, DeleteView):
  model = Toy
  success_url = '/toys/'

@login_required
def add_toy(request, dog_id, toy_id):
  Dog.objects.get(id=dog_id).toys.add(toy_id)
  return redirect('detail', dog_id = dog_id)

@login_required
def delete_toy(request, dog_id, toy_id):
  Dog.objects.get(id=dog_id).toys.remove(toy_id)
  return redirect('detail', dog_id = dog_id)


def signup(request):
  error_msg = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST) #creating a new instance of the form w information from the user
    if form.is_valid():
      user = form.save() #ok save the user
      login(request,user) #login the new user to the website

      return redirect('index')

    else:
      error_msg = 'There is an error with your sign-up info. Please try again. サインアップ情報にエラーがあります。もう一度やり直してください」'
    
  form = UserCreationForm()
  info = {'form': form, 'error_msg':error_msg}
  return render(request, 'registration/signup.html', info)