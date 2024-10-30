from django.db import models

# Create your models here.
class Worker(models.Model):
    name = models.CharField(max_length=20, blank=True)
    second_name = models.CharField(max_length=20, blank=True)
    payment = models.CharField(max_length=30,)
    phone = models.CharField(max_length=20,)
    sportCategory = models.ForeignKey('Catigory', on_delete=models.PROTECT, null=True)
    coment = models.TextField(max_length=100,)
    yare = models.CharField(max_length=5,)
    month = models.CharField(max_length=10,)
    day = models.CharField(max_length=2,)

    def __str__(self):
        return f'{self.name},{self.second_name},{self.payment},{self.sportCategory}'

class Catigory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'