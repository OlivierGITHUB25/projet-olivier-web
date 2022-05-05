from django.shortcuts import render
from .forms import LivreForm
from . import models

# Create your views here.

def index(request):
    return render(request, 'sncf/index.html')



def ajout(request):
    if request.method == "POST":
        form = LivreForm(request)
        if form.is_valid(): # validation du formulaire.
            livre = form.save() # sauvegarde dans la base
            return render(request,"/appSNCF/affiche.html",{"train" : train})
        else:
            return render(request,"sncf/ajout.html",{"form": form})
    else :
        form = LivreForm() # création d'un formulaire vide
        return render(request,"sncf/ajout.html",{"form" : form})
