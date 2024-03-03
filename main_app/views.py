from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Plant, Photo
import uuid
import boto3
from .forms import FeedingForm
S3_BASE_URL = 'https://s3.us-east-2.amazonaws.com/'
BUCKET = 'rich-plant-collector'



class Home(LoginView):
  template_name = 'home.html'

def about(request):
  return render(request, 'about.html')
@login_required
def plant_index(request):
    plants = Plant.objects.filter(user=request.user)
    return render(request, 'plants/index.html', { 'plants': plants })

def plant_detail(request, plant_id):
  plant = Plant.objects.get(id=plant_id)
  feeding_form = FeedingForm()
  return render(request, 'plants/detail.html', {
    'plant': plant, 'feeding_form': feeding_form
  })

def add_feeding(request, plant_id):
  form = FeedingForm(request.POST)
  if form.is_valid():
    new_feeding = form.save(commit=False)
    new_feeding.plant_id = plant_id
    new_feeding.save()
  return redirect('plant-detail', plant_id=plant_id)

class PlantCreate(LoginRequiredMixin, CreateView):
  model = Plant
  fields = ['species', 'description', 'watering_frequency', 'height']

  def form_valid(self, form):
    form.instance.user = self.request.user 
    return super().form_valid(form)

class PlantUpdate(LoginRequiredMixin, UpdateView):
  model = Plant
  fields = ['species', 'description', 'watering_frequency', 'height']

class PlantDelete(LoginRequiredMixin, DeleteView):
  model = Plant
  success_url = '/plants/'

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('plant-index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)

def add_photo(request, plant_id):
  photo_file = request.FILES.get('photo-file', None)
  if photo_file:
    s3 = boto3.client('s3')
    key = uuid.uuid4().hex + photo_file.name[photo_file.name.rfind('.'):]
    try:
      s3.upload_fileobj(photo_file, BUCKET, key)
      url = f"{S3_BASE_URL}{BUCKET}/{key}"
      photo = Photo(url=url, plant_id=plant_id)
      plant_photo = Photo.objects.filter(plant_id=plant_id)
      if plant_photo.first():
        plant_photo.first().delete()
      photo.save()
    except Exception as err:
      print('An error occurred uploading file to S3: %s' % err)
  return redirect('plant-detail', plant_id=plant_id)