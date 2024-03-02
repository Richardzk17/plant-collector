from django.db import models
from django.urls import reverse

WATERING = (
  ('M', 'Morning'),
  ('A', 'Afternoon'),
  ('N', 'Night')
)

class Plant(models.Model):
    species = models.CharField(max_length=100)
    description = models.TextField()
    height = models.IntegerField()
    watering_frequency = models.CharField(max_length=100)

    def __str__(self):
      return self.species

    def get_absolute_url(self):
      return reverse('plant-detail', kwargs={'plant_id': self.id})

class Feeding(models.Model):
  date = models.DateField()
  watering = models.CharField(
    max_length=1,
    choices=WATERING,
    default=WATERING[0][0]
  )

  plant = models.ForeignKey(Plant, on_delete=models.CASCADE)

  def __str__(self):
    # Nice method for obtaining the friendly value of a Field.choice
    return f"{self.get_watering_display()} on {self.date}"
