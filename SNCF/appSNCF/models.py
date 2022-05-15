from django.db import models


class train(models.Model):
    modele = models.CharField(max_length=100)
    date_sortie = models.DateField(blank=True, null = True)
    nombre_en_stock= models.IntegerField(blank=False)
    resume = models.TextField(null = True, blank = True) # champs de type text long
    marque = models.ForeignKey("marque", on_delete=models.CASCADE, default=None)

    def __str__(self):
            chaine = f"{self.modele} fabriqué par {self.marque} sortie le {self.date_sortie}"
            return chaine
    def dico(self):
        return {"modele": self.modele, "date_sortie": self.date_sortie,"nombre_en_stock":self.nombre_en_stock,"resume":self.resume,"marque": self.marque}


class marque(models.Model):
    marque = models.CharField(max_length = 100)

    def __str__(self):
        chaine = f"{self.marque}"
        return chaine
    def dico(self):
        return {"marque": self.marque}