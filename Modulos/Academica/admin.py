from django.contrib import admin
from Modulos.Academica.models import Idioma, Estudiante, Docente, Nivel, Matricula

admin.site.register(Idioma)

class NivelAdmin(admin.ModelAdmin):
    list_display = ('horario',"idioma", 'frecuencia', 'docente')

admin.site.register(Nivel, NivelAdmin)

class MatriculaAdmin(admin.ModelAdmin):
    raw_id_fields = ('estudiante',)
    list_display = ('dni_estudiante', 'nombre_completo_estudiante', 'nombre_idioma', 'estado', 'horario', 'niveles', 'fechaMatricula', 'pago', 'frecuencia')
    search_fields = ('estudiante__dni', 'estudiante__apellidoPaterno', 'estudiante__apellidoMaterno', 'estudiante__nombres', 'pago')
    list_filter = ('horario', 'niveles', 'estudiante__idioma', 'pago')

    def dni_estudiante(self, obj):
        return obj.estudiante.dni
    dni_estudiante.short_description = 'DNI del estudiante'

    def nombre_completo_estudiante(self, obj):
        return obj.estudiante.nombreCompleto()
    nombre_completo_estudiante.short_description = 'Nombre del estudiante'

    def nombre_idioma(self, obj):
        return obj.estudiante.idioma.nombre
    nombre_idioma.short_description = 'Idioma'

    def estado(self, obj):
        return "ACTIVO" if obj.estudiante.vigencia else "INACTIVO"
    estado.short_description = 'Estado'

    def frecuencia(self, obj):
        return obj.horario.frecuencia
    frecuencia.short_description = 'Frecuencia'

admin.site.register(Matricula, MatriculaAdmin)




class EstudianteAdmin(admin.ModelAdmin):
    search_fields = ['dni', 'apellidoPaterno', 'apellidoMaterno', 'nombres']
    list_display = ['dni', 'apellidoPaterno', 'apellidoMaterno', 'nombres', 'numeroCelular', 'correoElectronico', 'region', 'estado']

    def estado(self, obj):
        # Lógica para determinar el estado
        return "ACTIVO" if obj.vigencia else "INACTIVO"

admin.site.register(Estudiante, EstudianteAdmin)

class DocenteAdmin(admin.ModelAdmin):
    list_display = ['dni', 'apellidoPaterno', 'apellidoMaterno', 'nombres', 'numeroCelular', 'correoElectronico', 'estado']

    def estado(self, obj):
        # Lógica para determinar el estado
        return "ACTIVO" if obj.vigencia else "INACTIVO"

admin.site.register(Docente, DocenteAdmin)