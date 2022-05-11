from django.shortcuts import render
from .forms import trainForm, marqueForm
from . import models
from django.http import HttpResponseRedirect

# Create your views here.

def index(request):
    return render(request, 'sncf/index.html')

def ajout(request):
    if request.method == "POST":
        form = trainForm(request)
        if form.is_valid(): # validation du formulaire.
            train = form.save() # sauvegarde dans la base
            return render(request,"sncf/affiche.html",{"train" : train})
        else:
            return render(request,"sncf/ajout.html",{"form": form})
    else :
        form = trainForm() # création d'un formulaire vide
        return render(request,"sncf/ajout.html",{"form" : form})

def traitement(request):
    Tform = trainForm(request.POST)
    if Tform.is_valid():
        train = Tform.save()
        return render(request,"sncf/affiche.html",{"train" : train})
    else:
        return render(request,"sncf/ajout.html",{"form": Tform})

def affiche(request, id):
    train = models.train.objects.get(pk=id)
    return render(request, "sncf/affiche.html", {"train": train})

def traitementupdate(request, id):
    Tform = trainForm(request.POST)
    if Tform.is_valid():
        train = Tform.save(commit=False)
        train.id = id
        train.save()
        return HttpResponseRedirect("/sncf/")
    else:
        return render(request, "sncf/update.html", {"form": Tform, "id": id})

def listTOTALtrain(request):
    liste = models.train.objects.all()
    return render(request, "sncf/stock.html", {"liste": liste})
def deleteTrain(request, id):
    train = models.train.objects.get(pk=id)
    train.delete()
    return HttpResponseRedirect ("/appSNCF/stock/")

def traitementMarque(request):
    Mform = marqueForm(request.POST)
    if Mform.is_valid():
        marque = Mform.save()
        return render(request,"sncf/affiche-marque.html",{"marque" : marque})
    else:
        return render(request,"sncf/ajout-marque.html",{"form": Mform})

def ajoutMarque(request):
    form = marqueForm() # création d'un formulaire vide
    listeMarque = models.marque.objects.all()
    return render(request,"sncf/ajout-marque.html",{"form" : form, "listeMarque": listeMarque})

def traitementupdatemarque(request, id):
    Mform = marqueForm(request.POST)
    if Mform.is_valid():
        marque = Mform.save(commit=False)
        marque.id = id
        marque.save()
        return HttpResponseRedirect("/sncf/")
    else:
        return render(request, "sncf/update-marque.html", {"form": Mform, "id": id})
def deleteMarque(request, id):
    marque = models.marque.objects.get(pk=id)
    marque.delete()
    return HttpResponseRedirect ("/appSNCF/ajoutMarque/")


