from django.db import models

# Create your models here.
class Greeting(models.Model):
    when = models.DateTimeField('date created', auto_now_add=True)

class padres(models.Model):
    Nombre_Padre = models.CharField(max_length=250)
    Apellidos_Padre = models.CharField(max_length=250)
    Cedula_Padre = models.CharField(unique=True,max_length=20)
    Email_Padre = models.EmailField(unique=True)
    Nombre_Abuelo_Paterno = models.CharField (max_length=500)
    Nombre_Abuela_Paterna = models.CharField (max_length=500)
    Nombre_Madre = models.CharField(max_length=500)
    Apellidos_Madre = models.CharField(max_length=500)
    Cedula_Madre = models.CharField(unique=True,max_length=20)
    Email_Madre = models.EmailField(unique=True)
    Nombre_Abuelo_Materno = models.CharField (max_length=500)
    Nombre_Abuela_Materna = models.CharField (max_length=500)

    def __unicode__(self):
        return u"%s %s - %s %s" % (self.Nombre_Padre, self.Apellidos_Padre,self.Nombre_Madre,self.Apellidos_Madre)

    @models.permalink
    def get_absolute_url(self):
        return ('padres_detail', [self.pk])

# class madre(models.Model):

#    Nombre_Madre = models.CharField(max_length=500)
#    Apellidos_Madre = models.CharField(max_length=500)
#    Cedula_Madre = models.CharField(blank=True, unique=True,max_length=20)
#    Email_Madre = models.EmailField(unique=True)
#    Nombre_Abuelo_Materno = models.CharField (max_length=500)
#    Nombre_Abuela_Materna = models.CharField (max_length=500)

#    def __unicode__(self):
#        return self.Nombre_Madre 

#     @models.permalink
#     def get_absolute_url(self):
#         return ('padre_detail', [self.pk])


class bautizado(models.Model):
    Casado = '1'
    Soltero = '2'
    Viudo = '3'
    estado_civil = (
          (Casado,'Casado'),
          (Soltero,'Soltero'),
          (Viudo, 'Viudo'),
    )
    # def validate_even(value):
    # if value % 2 != 0:
    #     raise ValidationError('%s is not an even number' % value)

    Nombre_Bautizado = models.CharField(max_length=500)
    Apellidos_Bautizado = models.CharField(max_length=500)
    Id_Reg_Civil = models.CharField(max_length=15,unique=True)
    Fecha_Nacimiento = models.DateField(auto_now=False, auto_now_add=False)
    Lugar_Nacimiento = models.CharField(max_length=255)
    Telefono = models.CharField(max_length=7)
    Celular = models.CharField(max_length=10)
    Direccion = models.CharField(max_length=500)
    Registro_civil = models.ImageField(upload_to='Registro_Civil')
    Padres = models.ForeignKey(padres)
    Nombre_Padrino = models.CharField(max_length=500, blank=True)
    Apellidos_Padrino = models.CharField(max_length=500, blank=True )
    Cedula_Padrino = models.CharField(blank=True, unique=True,max_length=20 )
    Estado_Civil_Padrino = models.CharField(max_length=1,choices=estado_civil,default=Soltero,blank=True)
    Email_Padrino = models.EmailField(blank=True)
    Fotocopia_Cedula_Padrino = models.ImageField(upload_to='Fot_Celula_Padrino',blank=True)
    Nombre_Madrina = models.CharField(max_length=500, blank=True)
    Apellidos_Madrina = models.CharField(max_length=500, blank=True )
    Cedula_Madrina = models.PositiveIntegerField(blank=True,null=True,unique=True)
    Estado_Civil_Madrina = models.CharField(max_length=1,choices=estado_civil,default=Soltero,blank=True)
    Email_Madrina = models.EmailField(blank=True)
    Fotocopia_Cedula_Madrina = models.ImageField(upload_to='Fot_Celula_Madrina',blank=True)
    Aprobado = models.NullBooleanField(blank=True)
    ya_Bautizado = models.NullBooleanField(blank=True)
    Fecha_del_Bautizo = models.DateField(auto_now=False, auto_now_add=False,blank=True,null=True)

    def __unicode__(self):
        return u"%s %s" % (self.Nombre_Bautizado, self.Apellidos_Bautizado)

    @models.permalink
    def get_absolute_url(self):
        return ('bautizado_detail', [self.pk])

# class Book(models.Model):
#     author = models.ForeignKey(Author)
#     title = models.CharField(max_length=100)

#     def __unicode__(self):
#         return self.title

#     @models.permalink
#     def get_absolute_url(self):
#         return ('book_detail', [self.pk])

