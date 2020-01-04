from django.urls import path
from apps.General.views import index, login

urlpatterns = [
    path('', index, name='inicio'),
    path('login/', login, name='login'),
]
