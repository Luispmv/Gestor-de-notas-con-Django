from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.http import HttpResponse
from .models import Note
from django.template import loader
from django.db.models import F
from django.urls import reverse

# Create your views here.
def index(request):
    notas = Note.objects.all()
    context = {
        "notas": notas
    }
    return render(request, "notes_MujicaTavera/index.html", context)

def individual(request, nota_id):
    nota = get_object_or_404(Note, pk=nota_id)
    context = {
        "nota": nota
    }
    return render(request, "notes_MujicaTavera/individual.html", context)

