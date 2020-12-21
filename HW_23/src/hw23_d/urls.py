from django.urls import path, include
from hw23_d.views import APICarViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('cars', APICarViewSet)

urlpatterns = [
    path('meta/', include(router.urls))
]
