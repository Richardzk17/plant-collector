from django.db import models

class Plant(models.Model):
  species = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  watering_frequency = models.IntegerField()
  height = models.IntegerField()

  def __str__(self):
    return self.species



