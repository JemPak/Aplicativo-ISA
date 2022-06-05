from django.contrib import admin

from API import models

@admin.register(models.Gestores)
class GestoresAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Ejecucion)
class EjecucionAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Planeacion)
class PlaneacionAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Diagnostico)
class DiagnosticoAdmin(admin.ModelAdmin):
    pass
