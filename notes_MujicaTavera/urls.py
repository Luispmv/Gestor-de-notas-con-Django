from django.urls import path
from . import views

app_name = 'notes_MujicaTavera'

urlpatterns = [
    path('', views.list, name='list'),  # Lista de notas
    path('<int:pk>/', views.detail, name='detail'),  # Detalle de una nota
    path('new/', views.create, name='create'),  # Crear nota
    path('<int:pk>/edit/', views.edit, name='edit'),  # Editar nota
    path('<int:pk>/delete/', views.delete, name='delete'),  # Eliminar nota
    path('change_user/', views.change_user, name='change_user'),  # Cambiar usuario aleatorio
]
