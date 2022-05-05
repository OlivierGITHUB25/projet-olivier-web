from django.db import models

class Livre(models.Model):
    modele = models.CharField(max_length=100)
    marque = models.CharField(max_length = 100)
    date_sortie = models.DateField(blank=True, null = True)
    nombre_en_stock= models.IntegerField(blank=False)
    resume = models.TextField(null = True, blank = True) # champs de type text long
    def __str__(self):
            chaine = f"{self.modele}fabriqué par{self.marque}sortie le{self.date_sortie}"
            return chaine