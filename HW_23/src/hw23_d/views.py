from hw23_d.models import Car
from hw23_d.serializers import CarSerializer
from rest_framework import viewsets


class APICarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

