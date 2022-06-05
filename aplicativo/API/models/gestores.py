from django.db import models

class Gestores(models.Model):
    
    nombre = models.CharField('Nombre', max_length=50)
    edad = models.IntegerField('Edad')
    cargo = models.CharField('Cargo', max_length=30)
    fecha_inicio = models.DateField('Fecha de Inicio Contrato')
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = 'Gestor'
        verbose_name_plural = 'Gestores'