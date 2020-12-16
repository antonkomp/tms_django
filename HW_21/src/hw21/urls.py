from django.urls import path
from hw21.views import home, add_user, detail_user, edit_user, delete_user

urlpatterns = [
    path('home/', home, name='home'),
    path('add_user/', add_user, name='add_user'),
    path('detail_user/<int:user_id>/', detail_user, name='detail_user'),
    path('edit_user/<int:user_id>/', edit_user, name='edit_user'),
    path('delete_user/<int:user_id>/', delete_user, name='delete_user'),
]
