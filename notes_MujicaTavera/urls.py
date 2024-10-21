from django.urls import path
from . import views

app_name = "notes_MujicaTavera"

urlpatterns = [
    # 127.0.0.1:8000/notes_MujicaTavera/
    path("", views.index, name="index"),

    # mostrar nota individual
    path("<int:nota_id>/", views.individual, name="individual")
]