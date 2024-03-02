from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Plant


def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def plant_index(request):
    plants = Plant.objects.all()
    return render(request, 'plants/index.html', { 'plants': plants })


def plant_detail(request, plant_id):
  plant = Plant.objects.get(id=plant_id)
  return render(request, 'plants/detail.html', { 'plant': plant })

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