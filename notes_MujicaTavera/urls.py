from django.urls import path
from . import views

app_name = "notes_MujicaTavera"

urlpatterns = [
    #notas --> mostrar todas las notas existentes
    path("", views.index, name="index")
]