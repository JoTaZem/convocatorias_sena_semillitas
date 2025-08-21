from django.db import models
from django.contrib.auth.models import AbstractUser


roles = [
    ('Líder','Líder'),
    ('Funcionario','Funcionario'),
    ('Aprendiz','Aprendiz')
]

resultadoPostulacion = [
    ('Beneficiado','Beneficiado'),
    ('No Beneficiado','No Beneficiado')
]
# Create your models here.
class TipoConvocatoria(models.Model):
    tipNombre = models.CharField(max_length=50, unique=True)
    
     
    def __str__(self):
        return self.tipNombre
    
class Convocatoria(models.Model):
    conNombre = models.CharField(max_length=200)
    conTipo = models.ForeignKey(TipoConvocatoria, on_delete=models.PROTECT)
    conCantidadBeneficiarios = models.IntegerField()
    conFechaInicio=models.DateTimeField()
    conFechaFinal=models.DateTimeField()
    conFechaCreacion = models.DateTimeField(auto_now_add=True)
    conDocumento=models.FileField(upload_to='documentos/',blank=True, null= True)
    
    def __str__(self):
        return self.conNombre

class Usuario(AbstractUser):
    usuIdentificacion = models.CharField(max_length=15, unique=True)
    usuRol = models.CharField(max_length=50,choices=roles)
    
    def __str__(self):
        return self.username
    
class Funcionario(models.Model):
    funUsuario = models.ForeignKey(Usuario, on_delete=models.PROTECT)
    funCargo = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.funUsuario.first_name} {self.funUsuario.last_name}"
    
class Aprendiz(models.Model):
    aprUsuario = models.ForeignKey(Usuario, on_delete=models.PROTECT)
    aprFicha = models.CharField(max_length=10)
    aprPrograma = models.CharField(max_length=50)
    
    def __str__(self):
         return f"{self.aprUsuario.first_name} {self.aprUsuario.last_name}"
     
class Postulacion(models.Model):
    posAprendiz = models.ForeignKey(Aprendiz, on_delete=models.PROTECT)
    posConvocatoria = models.ForeignKey(Convocatoria, on_delete=models.PROTECT)
    posFechaHoraPostulacion= models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.posAprendiz}-{self.posConvocatoria}"
    
class ResultadoPostulacion(models.Model):
    resPostulacion = models.ForeignKey(Postulacion, on_delete=models.PROTECT)
    resValoracion=models.IntegerField()
    resResultado=models.CharField(max_length=16, choices=resultadoPostulacion, 
                                  null=True, default=None)
    resFechaActualizacion=models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return f"{self.resValoracion} {self.resResultado}"