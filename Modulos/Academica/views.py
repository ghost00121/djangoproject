from django.shortcuts import render
from .models import Idioma
# Create your views here.

def home(request):
    idiomasListados= Idioma.objects.all()
    return render(request, "GestionCursos.html",{"idioma": idiomasListados})

