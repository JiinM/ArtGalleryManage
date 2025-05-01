from django.db import models

# Create your models here.
class Artists(models.Model):
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Exhibits(models.Model):
    artist = models.ForeignKey('Artists', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    date = models.DateField()
    description = models.TextField()
    capacity = models.IntegerField()

    def __str__(self):
        return self.title


class Reservations(models.Model):
    visitor = models.ForeignKey('Visitors', on_delete=models.CASCADE)
    exhibit = models.ForeignKey('Exhibits', on_delete=models.CASCADE, related_name='reservations')
    reserve_date = models.DateField()
    status = models.CharField(max_length=20)


class Visitors(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)