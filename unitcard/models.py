from django.db import models
from django.core.validators import RegexValidator
import os

# Create your models here.

class Card(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    company = models.CharField(max_length=50, blank=True)
    title = models.CharField(max_length=50, blank=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")

    phone = models.CharField(validators=[phone_regex], max_length=17, blank=True)  # validators should be a list
    email = models.EmailField(max_length=255, blank=True)
    website = models.CharField(max_length=255, blank=True)
    def __str__(self):
        return self.first_name


class Vcard(models.Model):
    filecard = models.FileField(upload_to = 'card/')
    imgcard = models.ImageField(upload_to = 'img/', default='img01.png')
    # def filename(self):
    #     return os.path.basename(self.filecard.name)


# class Scard(models.Model):
#     imgcard = models.ImageField(upload_to = 'img/', default='img01.png')