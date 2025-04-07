# Create your models here.
from django.db import models
class Position(models.Model):
   title = models.CharField(max_length=200)
class Crud(models.Model):
    titre = models.CharField(max_length=255)
    contenu = models.TextField(max_length=200)
    date_publicatiôn = models.DateTimeField('La Date de publication')
    auteur =models.ForeignKey(Position,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images',null=True,blank=True)
    


    