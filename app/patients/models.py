from secrets import choice
from django.db import models
from django.forms import model_to_dict
from django.core.validators import RegexValidator
from app.patients.choices import genders_choices,hobbies_choices,stratum_choices

#Regex:Realiza las validaciones a los campos
REGEX_NAME = RegexValidator()
# Create your models here.

class Hobbies(models.Model):
    hob_nombre= models.CharField(max_length=30, null=False,choices=hobbies_choices,verbose_name='Hobbies')
    
    def __str__(self):
        return self.hob_nombre

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name = 'Hobbie'
        verbose_name_plural = 'Hobbies'


class Patient(models.Model):
    
    pac_nit = models.IntegerField(null=False,blank=False,verbose_name='Documento de identidad',
        validators=[
            RegexValidator(
                regex='^([\d]{1,5})\s?([\d]){5,7}$',
                message='El numero de identificacion es incorrecto,verifique que no contenga letras o simbololos',
            
            ),
        ])
    
    pac_nombre = models.CharField(null=False,max_length=50, verbose_name='Nombre',         
        validators=[
            RegexValidator(
                regex='^[A-Za-z ]{3,50}$',
                message='Nombre invalido,verifique que no contenga letras o simbolos',
            ),
        ])

    pac_apellido = models.CharField(max_length=50, null=False, verbose_name='Apellidos',         
        validators=[
            RegexValidator(
                regex='^[A-Za-z ]{3,50}$',
                message='El apellido ingresado es invalido,verifique que no contenga letras o simbolos',
            ),
        ])

    pac_direccion = models.CharField(max_length=70, null=False, verbose_name='Direccion',         
            validators=[
                RegexValidator(
                    regex='^[A-Za-z0-9 #-.]{10,100}$',
                    message='Direccion incorrecta, verifique que esta bien escrita',
            ),
        ])

    pac_telefono= models.CharField(max_length=15, null=False, blank=False, verbose_name='Telefono', 
            validators=[
                RegexValidator(
                    regex='^([\d]{5,5})\s?([\d]){5,5}$',
                    message='Numero telefonico digitado incorrectamente, verifique que no tenga letras ni simbolos',
            ),
        ])

    pac_email = models.EmailField(max_length=254, null=False,verbose_name="Email")

    hob_nombre= models.ManyToManyField(Hobbies)

    gen_nombre = models.CharField(max_length=30, null=False,choices=genders_choices,verbose_name='Genero')

    estr_nombre = models.CharField(max_length=30, null=False,choices=stratum_choices,verbose_name='Estrato')

    def __str__(self):
        return self.pac_nombre
    
    def names(self):
        return '{}  {}'.format(self.pac_nombre, self.pac_apellido) 

    def toJSON(self):
        item = model_to_dict(self)
        item['names'] = self.names()
        return item
    

    class Meta:
        verbose_name = 'Paciente'
        verbose_name_plural = 'Pacientes'
        ordering = ['id']


class medicalRecords(models.Model):

    pac = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Paciente')
    
    hist_motv = models.CharField(max_length=500, null=True, blank=True, verbose_name='Motivo de Visita')
    
    hist_esfod= models.CharField(max_length=50, null=False, verbose_name='Esfera OD')
    
    hist_cilod = models.CharField(max_length=50, null=False,verbose_name= 'Cilindro OD')
    
    hist_ejeod = models.CharField(max_length=50, null=False,verbose_name= 'Eje OD')
    
    hist_esfoi =  models.CharField(max_length=50, null=False,verbose_name= 'Esfera OI')
    
    hist_ciloi = models.CharField(max_length=50, null=False,verbose_name= 'Cilindro OI')
    
    hist_ejeoi = models.CharField(max_length=50, null=False,verbose_name= 'Eje OI')
    
    hist_diaod = models.CharField(max_length=50, null=False,verbose_name= 'Diagnostico ojo derecho')

    hist_diaoi = models.CharField(max_length=50, null=False,verbose_name= 'Diagnostico ojo izquierdo')
    
    hist_recom = models.CharField(max_length=500, null=True, blank=True, verbose_name='Recomendaciones')
    
    
    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name = 'Historia Clinica'
        verbose_name_plural = 'Historias Clinicas'


