from django.urls import path
from controlecaixa.views import controlecaixa, logout

urlpatterns = [
    path ('caixa', controlecaixa, name='controlecaixa'),
    path ('logout', logout, name ="logout"),
]