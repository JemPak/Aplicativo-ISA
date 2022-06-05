# Generated by Django 4.0 on 2022-06-05 22:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gestores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('edad', models.IntegerField(verbose_name='Edad')),
                ('cargo', models.CharField(max_length=30, verbose_name='Cargo')),
                ('fecha_inicio', models.DateField(verbose_name='Fecha de Inicio Contrato')),
            ],
        ),
        migrations.CreateModel(
            name='Planeacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empresa', models.CharField(max_length=40, verbose_name='Empresa')),
                ('tipo_proceso', models.CharField(choices=[('clausula', 'Cláusula Adicional'), ('contratacion', 'Proceso de Contratación'), ('orden', 'Orden de Entrega')], max_length=20, verbose_name='Tipo de Proceso')),
                ('subcategoria', models.CharField(max_length=40, verbose_name='Subcategoría de Compra')),
                ('area', models.CharField(max_length=40, verbose_name='Área Cliente')),
                ('moneda', models.CharField(choices=[('COP', 'COP - pesos'), ('USD', 'USD - dolares'), ('BRL', 'BRL - reales'), ('PEN', 'PEN - sol')], max_length=3, verbose_name='Moneda')),
                ('presupuesto', models.IntegerField(verbose_name='Presupuesto')),
                ('estado', models.CharField(choices=[('Proceso Nuevo', 'Proceso Nuevo'), ('Reunión Inicio', 'Reunión Inicio'), ('Solicitud de Ofertas', 'Solicitud de Ofertas'), ('Evaluación de Ofertas', 'Evaluación de Ofertas'), ('Adjudicación', 'Adjudicación'), ('Contrato', 'Contrato'), ('Entrega Contrato', 'Entrega Contrato')], default='Proceso Nuevo', max_length=40, verbose_name='Estado Proyecto')),
                ('fecha_inicio', models.DateField()),
                ('fecha_vencimiento', models.DateField()),
                ('gestor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Asignado A+', to='API.gestores')),
            ],
        ),
        migrations.CreateModel(
            name='Ejecucion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_contrato', models.CharField(max_length=20, verbose_name='# del contrato ganador')),
                ('contratista', models.CharField(max_length=50, verbose_name='Contratista Seleccionado')),
                ('inicio_contrato', models.DateField(verbose_name='Fecha de Inicio de Contrato')),
                ('vencimiento_contrato', models.DateField(null=True, verbose_name='Fecha de Finalización de contrato')),
                ('porcentaje_avance', models.IntegerField(default=0, verbose_name='Porcentaje de Progreso')),
                ('fecha_1', models.DateField(null=True, verbose_name='Revisión 1 del contrato')),
                ('seguimiento_1', models.TextField(null=True, verbose_name='Notas de la revision 1 al contrato')),
                ('fecha_2', models.DateField(null=True, verbose_name='Revisión 2 del contrato')),
                ('seguimiento_2', models.TextField(null=True, verbose_name='Notas de la revision 2 al contrato')),
                ('fecha_3', models.DateField(null=True, verbose_name='Revisión 2 del contrato')),
                ('seguimiento_3', models.TextField(null=True, verbose_name='Notas de la revision 3 al contrato')),
                ('observaciones', models.TextField(max_length=3000, null=True, verbose_name='Observaciones')),
                ('proceso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Id del Proceso+', to='API.planeacion')),
            ],
        ),
        migrations.CreateModel(
            name='Diagnostico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reunion', models.DateField(null=True, verbose_name='Reunión de Inicio')),
                ('notas_reunion', models.TextField(verbose_name='Notas de Reunion con el comprador')),
                ('id_oferta_ariba', models.CharField(max_length=30, null=True, verbose_name='Id de proceso en Ariba')),
                ('fecha_invitacion', models.DateField(null=True, verbose_name='Fecha de Invitación a Ofertar')),
                ('recepcion_oferta', models.DateField(null=True, verbose_name='Máxima Fecha para Recepción de Ofertas')),
                ('proceso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Id del Proceso+', to='API.planeacion')),
            ],
        ),
    ]
