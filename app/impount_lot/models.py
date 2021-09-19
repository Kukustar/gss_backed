from django.db import models

class Impount_lot_car(models.Model):
    date = models.DateTimeField('')
    number = models.CharField(max_length=200)
