from django.db import models

# Create your models here.

class CV(models.Model):
    firstname = models.CharField('Firstname', max_length=32)
    lastname = models.CharField('Lastname', max_length=32)
    short = models.CharField('Shortdesc', max_length=64)
    image = models.ImageField('Image', upload_to='media', default='media/default.jpg')
    about = models.TextField('About')

    def __str__(self):
        return self.firstname
    
    def save(self, *args, **kwargs):
        # Asigură că există doar un singur obiect CV în baza de date
        self.pk = 1
        super().save(*args, **kwargs)

    @classmethod
    def load(cls):
        # Returnează obiectul CV din baza de date sau creează unul nou dacă nu există
        obj, created = cls.objects.get_or_create(pk=1)
        return obj
    
    class Meta:
        verbose_name = 'Student'

class Galery(models.Model):
    image = models.ImageField('Image', upload_to='media', default='media/default.jpg')

    class Meta:
        verbose_name = 'Galery'