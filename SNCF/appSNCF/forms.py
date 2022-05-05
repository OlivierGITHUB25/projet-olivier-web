from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models

class trainForm(ModelForm):
    class Meta:
        model = models.train
        fields = ('modele', 'marque', 'date_sortie', 'nombre_en_stock','resume')
        labels = {
            'modele' : _('Modele'),
            'marque' : _('Marque') ,
            'date_sortie' : _('date_sortie'),
            'nombre_en_stock' : _('Nombre_en_stock'),
            'resume' : _('Résumé')
        }