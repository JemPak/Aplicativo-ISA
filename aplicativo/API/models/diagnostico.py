from django.db import models

from API.models import Planeacion

class Diagnostico(models.Model):
    
    proceso = models.ForeignKey(Planeacion, related_name='Id del Proceso+', on_delete=models.CASCADE)
    reunion = models.DateField('Reunión de Inicio', null=True)
    notas_reunion = models.TextField('Notas de Reunion con el comprador')
    id_oferta_ariba = models.CharField('Id de proceso en Ariba', max_length=30, null=True)
    fecha_invitacion = models.DateField('Fecha de Invitación a Ofertar', null=True)
    recepcion_oferta = models.DateField('Máxima Fecha para Recepción de Ofertas', null=True)
    
    
    class Meta:
        verbose_name = 'Diagnostico'
        verbose_name_plural = 'Diagnosticos'