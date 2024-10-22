from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from .models import Note
from random import choice

# Función auxiliar para obtener un usuario aleatorio
def get_random_user():
    user = choice(User.objects.all())
    return user.id, user.username

def list(request):
    # Obtenemos el ID y el username del usuario aleatorio de la sesión, si no existe, generamos uno
    random_user_id, random_username = request.session.get('random_user', get_random_user())
    # Guardamos el ID y el username en la sesión si es la primera vez
    request.session['random_user'] = (random_user_id, random_username)

    # Filtramos las notas por el usuario aleatorio
    notes = Note.objects.filter(user_id=random_user_id)
    
    # Renderizamos la plantilla con las notas y el username
    return render(request, "notes_MujicaTavera/note_list_MujicaTavera.html", 
                  {'notes': notes, 'username': random_username})

def change_user(request):
    # Generamos un nuevo usuario aleatorio y lo guardamos en la sesión
    random_user_id, random_username = get_random_user()
    request.session['random_user'] = (random_user_id, random_username)
    # Redirigimos nuevamente a la vista de lista de notas
    return redirect('notes_MujicaTavera:list')



def detail(request, pk):
    random_user_id = request.session.get('random_user_id')
    note = get_object_or_404(Note, pk=pk, user_id=random_user_id)
    return render(request, "notes_MujicaTavera/note_detail_MujicaTavera.html", {'note': note})


def create(request):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        random_user_id = request.session.get('random_user_id')
        user = get_object_or_404(User, id=random_user_id)
        Note.objects.create(title=title, content=content, user=user)
        return redirect('notes_MujicaTavera:list')
    return render(request, "notes_MujicaTavera/note_edit_MujicaTavera.html")


def edit(request, pk):
    random_user_id = request.session.get('random_user_id')
    note = get_object_or_404(Note, pk=pk, user_id=random_user_id)

    if request.method == "POST":
        note.title = request.POST.get('title')
        note.content = request.POST.get('content')
        note.save()
        return redirect('notes_MujicaTavera:detail', pk=note.pk)
    return render(request, "notes_MujicaTavera/note_edit_MujicaTavera.html", {'note': note})


def delete(request, pk):
    random_user_id = request.session.get('random_user_id')
    note = get_object_or_404(Note, pk=pk, user_id=random_user_id)

    if request.method == "POST":
        note.delete()
        return redirect('notes_MujicaTavera:list')
    return render(request, "notes_MujicaTavera/note_delete_MujicaTavera.html", {'note': note})
