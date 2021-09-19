from rest_framework import permissions, filters, viewsets
from .serializers import Impount_lot_car_Serializer
from .models import Impount_lot_car
from rest_framework.response import Response


class Impount_lot_car_ViewSet(viewsets.ModelViewSet):
    queryset = Impount_lot_car.objects.all()
    serializer_class = Impount_lot_car_Serializer
    permission_classes = [permissions.IsAuthenticated]


class Impount_lot_car_ViewSet_Search(viewsets.ModelViewSet):
    queryset = Impount_lot_car.objects.all()
    serializer_class = Impount_lot_car_Serializer
    http_method_names = ['get']
    permission_classes = [permissions.AllowAny]

    def list(self, request):
        searching_number =request.query_params['number']
        if isinstance(searching_number, str):     
            queryset = Impount_lot_car.objects.filter(number=searching_number)
            serializer = Impount_lot_car_Serializer(queryset, many=True)
            return Response(serializer.data)
        else:
            return Response([])





