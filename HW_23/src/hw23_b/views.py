from hw23_b.models import Car
from hw23_b.serializers import CarSerializer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response


class CarsView(APIView):
    def get(self, request):
        cars = Car.objects.all()
        serializer = CarSerializer(cars, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CarDetail(APIView):
    def get(self, request, id):
        car = Car.objects.get(pk=id)
        serializer = CarSerializer(car)
        return Response(serializer.data)

    def put(self, request, id):
        car = Car.objects.get(pk=id)
        serializer = CarSerializer(car, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        car = Car.objects.get(pk=id)
        car.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
