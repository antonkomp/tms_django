from django.urls import path
from hw20.views import book_tickets

urlpatterns = [
    path('book/', book_tickets, name='book_tickets')
]
