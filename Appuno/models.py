from django.db import models
from datetime import  datetime, date
# Create your models here.
class libros(models.Model):
    titulo=models.CharField(max_length=30, verbose_name='Titulo1')
    autor=models.CharField(max_length=30)
    tipoCategoria = [
        ('T', 'Terror'),
        ('C', 'Comedia'),
        ('F', 'Fantasia'),
    ]
    categoria=models.CharField(max_length=1,choices=tipoCategoria,default='T')
    edad=models.DateField(blank=True, null=True )

