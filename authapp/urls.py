
from django.urls import path
from authapp.views import login, register, logout, profile


app_name = 'authapp'

urlpatterns = [
    path('login/', login.as_view(), name='login'),
    path('register/', register.as_view(), name='register'),
    path('logout/', logout.as_view(), name='logout'),
    path('profile/', profile.as_view(), name='profile'),
]