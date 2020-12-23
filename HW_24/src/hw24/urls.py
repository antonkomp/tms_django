from django.urls import path
from .views import home, save_picture, send_email

urlpatterns = [
    path('home_page/', home, name='home'),
    path('save_picture/', save_picture, name='save_picture'),
    path('send_email/', send_email, name='send_email')
]
