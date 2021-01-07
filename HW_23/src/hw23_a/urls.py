from django.urls import path
from hw23_a.views import cars_view, car_detail


urlpatterns = [
    path('cars/', cars_view),
    path('cars/<int:id>/', car_detail),
]
