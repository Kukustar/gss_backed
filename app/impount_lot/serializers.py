from .models import Impount_lot_car
from rest_framework import serializers

class Impount_lot_car_Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Impount_lot_car
        fields = ['id', 'date', 'number']