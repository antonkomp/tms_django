from rest_framework import generics
from hw23_c.serializers import CarSerializer
from hw23_c.models import Car


class CarCreateApi(generics.ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class CarApi(generics.ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class CarUpdateApi(generics.RetrieveUpdateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class CarDeleteApi(generics.RetrieveDestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
