from django.db import models

from API.models.planeacion import Planeacion

class Ejecucion(models.Model):
    
    proceso = models.ForeignKey(Planeacion, related_name='Id del Proceso+', on_delete=models.CASCADE)
    numero_contrato = models.CharField('# del contrato ganador', max_length=20)
    contratista = models.CharField('Contratista Seleccionado', max_length=50)
    inicio_contrato = models.DateField('Fecha de Inicio de Contrato')
    vencimiento_contrato = models.DateField('Fecha de Finalización de contrato', null=True)
    porcentaje_avance = models.IntegerField('Porcentaje de Progreso', default=0)
    fecha_1 = models.DateField('Revisión 1 del contrato', null=True)
    seguimiento_1 = models.TextField('Notas de la revision 1 al contrato', null=True)
    fecha_2 = models.DateField('Revisión 2 del contrato', null=True)
    seguimiento_2 = models.TextField('Notas de la revision 2 al contrato', null=True)
    fecha_3 = models.DateField('Revisión 2 del contrato', null=True)
    seguimiento_3 = models.TextField('Notas de la revision 3 al contrato', null=True)
    observaciones = models.TextField('Observaciones', max_length=3000, null=True)
    
    def __str__(self):
        return self.numero_contrato
    
    class Meta:
        verbose_name = 'Ejecucion'
        verbose_name_plural = 'Ejecuciones'