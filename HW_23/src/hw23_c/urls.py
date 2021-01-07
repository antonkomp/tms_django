from django.urls import path
from hw23_c.views import CarCreateApi, CarApi, CarUpdateApi, CarDeleteApi


urlpatterns = [
    path('car/create/', CarCreateApi.as_view()),
    path('car/', CarApi.as_view()),
    path('car/<int:pk>/', CarUpdateApi.as_view()),
    path('car/<int:pk>/delete/', CarDeleteApi.as_view()),
]
