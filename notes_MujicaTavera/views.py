from django.shortcuts import render
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