from django.urls import path
from hw23_b.views import CarsView, CarDetail


urlpatterns = [
    path('cars/', CarsView.as_view()),
    path('cars/<int:id>/', CarDetail.as_view()),
]
