from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Plant
from .forms import FeedingForm



def home(request):
  return render(request, 'home.html')

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
  success_url = '/plants/'

class PlantUpdate(UpdateView):
  model = Plant
  fields = ['species', 'description', 'watering_frequency', 'height']

class PlantDelete(DeleteView):
  model = Plant
  success_url = '/plants/'