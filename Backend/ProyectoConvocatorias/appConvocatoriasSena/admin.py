from django.contrib import admin
from appConvocatoriasSena.models import Usuario, Aprendiz, Funcionario, Convocatoria, TipoConvocatoria, Postulacion, ResultadoPostulacion

# Register your models here.
admin.site.register(Usuario)
admin.site.register(Aprendiz)
admin.site.register(Funcionario)
admin.site.register(Convocatoria)
admin.site.register(TipoConvocatoria)
admin.site.register(Postulacion)
admin.site.register(ResultadoPostulacion)