from django.db import models

# Create your models here.
class certificado_medico(models.Model):

    Nombre= models.CharField(max_length=50)
    Fecha= models.DateTimeField()
    Foto=models.ImageField(upload_to="cars")


