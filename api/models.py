from django.db import models

# Create your models here.
class User(models.Model):
    user_id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=256)
    password = models.CharField(max_length=16)
    date_created = models.DateField(auto_now_add=True)

    def __repr__(self):
        return str(self.user_id)

class Station(models.Model):
    station_id = models.BigAutoField(primary_key=True)
    station_name = models.CharField(max_length=256)

    def __repr__(self):
        return str(self.station_id)

class Cycle(models.Model):
    cycle_id = models.BigAutoField(primary_key=True)
    borrowed_user = models.OneToOneField(User, on_delete=models.CASCADE)
    station_id = models.ForeignKey(Station, on_delete=models.CASCADE)

    def __repr__(self):
        return str(self.cycle_id)
