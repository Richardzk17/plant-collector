from django.shortcuts import render
from django.http import HttpResponse

# Define the home view
def home(request):
  return HttpResponse('<h1>Hello ᓚᘏᗢ</h1>')

def about(request):
  return render(request, 'about.html')

# Add new view
def plant_index(request):
  return render(request, 'plants/index.html', { 'plants': plants })

class Plant:  
  def __init__(self, species, breed, description, height,sunlight_requirements, watering_frequency):
    self.name = species
    self.breed = breed
    self.description = description
    self.watering_frequency = watering_frequency
    self.sunlight_requirements = sunlight_requirements
    self.height = height

plants = [
    Plant('Rose', 'Hybrid Tea Rose', 'Classic garden flower with fragrant blooms.', 2, 'Full sun', 'Once a week'),
    Plant('Lavender', 'English Lavender', 'Aromatic herb used for its calming properties.', 1, 'Full sun', 'Twice a week'),
    Plant('Fern', 'Boston Fern', 'Popular indoor plant known for its graceful fronds.', 3, 'Indirect sunlight', 'Every other day'),
    Plant('Cactus', 'Saguaro Cactus', 'Iconic desert plant with tall, ribbed stems.', 10, 'Full sun', 'Once a month')
]