from django.urls import path
from hw19.views import index, task1, task2

urlpatterns = [
    path('', index, name='index'),
    path('task1/', task1, name='task1'),
    path('task2/', task2, name='task2')
]
