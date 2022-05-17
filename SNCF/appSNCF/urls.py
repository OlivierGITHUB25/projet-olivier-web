from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index),
    path('ajout/', views.ajout),
    path('traitement/', views.traitement),
    path('affiche/<int:id>/',views.affiche),
    path('update/<int:id>/',views.update_train),
    path('stock/', views.listTOTALtrain),
    path('suprTrain/<int:id>/', views.deleteTrain),
    path('traitementMarque/', views.traitementMarque),
    path('ajoutMarque/', views.ajoutMarque),
    path('updateMarque/<int:id>/', views.update_marque),
    path('suprMarque/<int:id>/', views.deleteMarque),
    path('traitementupdatemarque/<int:id>/',views.traitementupdatemarque),
    path('traitementupdate/<int:id>/',views.traitementupdate),
]