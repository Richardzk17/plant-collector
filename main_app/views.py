from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import Plant
from .forms import FeedingForm



class Home(LoginView):
  template_name = 'home.html'

def about(request):
  return render(request, 'about.html')

def plant_index(request):
    plants = Plant.objects.all()
    return render(request, 'plants/index.html', { 'plants': plants })


def plant_detail(request, plant_id):
  plant = Plant.objects.get(id=plant_id)
  feeding_form = FeedingForm()
  return render(request, 'plants/detail.html', {
    # include the cat and feeding_form in the context
    'plant': plant, 'feeding_form': feeding_form
  })

def add_feeding(request, plant_id):
  form = FeedingForm(request.POST)
  if form.is_valid():
    new_feeding = form.save(commit=False)
    new_feeding.plant_id = plant_id
    new_feeding.save()
  return redirect('plant-detail', plant_id=plant_id)

class PlantCreate(CreateView):
  model = Plant
  fields = ['species', 'description', 'watering_frequency', 'height']

  def form_valid(self, form):
    form.instance.user = self.request.user 
    return super().form_valid(form)

class PlantUpdate(UpdateView):
  model = Plant
  fields = ['species', 'description', 'watering_frequency', 'height']

class PlantDelete(DeleteView):
  model = Plant
  success_url = '/plants/'

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('cat-index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)
