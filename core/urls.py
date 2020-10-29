from django.urls import path
from .views import index, galeria, registro, registroInsumo
urlpatterns = [
    path('', index, name="index"),
    path('galeria/', galeria, name="galeria"),
    path('registro/', registro, name="registro"),
    path('registroInsumo/', registroInsumo, name="registroInsumo"),
]