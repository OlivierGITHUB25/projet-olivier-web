from django.shortcuts import render
from .forms import trainForm
from . import models

# Create your views here.

def index(request):
    return render(request, 'sncf/index.html')



def ajout(request):
    if request.method == "POST":
        form = trainForm(request)
        if form.is_valid(): # validation du formulaire.
            train = form.save() # sauvegarde dans la base
            return render(request,"/SNCF/affiche.html",{"train" : train})
        else:
            return render(request,"sncf/ajout.html",{"form": form})
    else :
        form = trainForm() # création d'un formulaire vide
        return render(request,"sncf/ajout.html",{"form" : form})

def traitement(request):
    lform = trainForm(request.POST)
    if lform.is_valid():
        train = lform.save()
        return render(request,"/sncf/affiche.html",{"train" : train})
    else:
        return render(request,"sncf/ajout.html",{"form": lform})

