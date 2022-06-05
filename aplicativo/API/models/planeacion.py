from django.db import models

from API.models import Gestores

class Planeacion(models.Model):
    
    PROCESS_TYPES = (
        ('clausula', 'Cláusula Adicional'),
        ('contratacion','Proceso de Contratación'),
        ('orden', 'Orden de Entrega'),
    )
    
    MONEDA_TYPES = (
        ('COP', 'COP - pesos'),
        ('USD','USD - dolares'),
        ('BRL', 'BRL - reales'),
        ('PEN', 'PEN - sol'),
    )
    
    STATE_TYPES = (
        ('Proceso Nuevo', 'Proceso Nuevo'),
        ('Reunión Inicio','Reunión Inicio'),
        ('Solicitud de Ofertas', 'Solicitud de Ofertas'),
        ('Evaluación de Ofertas', 'Evaluación de Ofertas'),
        ('Adjudicación', 'Adjudicación'),
        ('Contrato', 'Contrato'),
        ('Entrega Contrato', 'Entrega Contrato'),
    )
    
    empresa = models.CharField('Empresa', max_length=40)
    tipo_proceso = models.CharField('Tipo de Proceso', max_length=20, choices=PROCESS_TYPES)
    subcategoria = models.CharField('Subcategoría de Compra', max_length=40)
    area = models.CharField('Área Cliente', max_length=40)
    moneda = models.CharField('Moneda', max_length=3, choices=MONEDA_TYPES)
    presupuesto = models.IntegerField('Presupuesto')
    estado = models.CharField('Estado Proyecto', choices=STATE_TYPES, default='Proceso Nuevo', max_length=40)
    gestor = models.ForeignKey(Gestores, related_name='Asignado A+', on_delete=models.CASCADE)
    fecha_inicio = models.DateField()
    fecha_vencimiento = models.DateField()
    
    def __str__(self):
        return str(self.id)
    
    
    class Meta:
        verbose_name = 'Planeacion'
        verbose_name_plural = 'Planeaciones'