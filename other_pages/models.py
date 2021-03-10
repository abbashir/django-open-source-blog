from django.db import models
from ckeditor.fields import RichTextField
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.


class About(models.Model):
    title = models.CharField(max_length=200)
    content = RichTextField()

    def __str__(self):
        return self.title


class Contact(models.Model):
    title = models.CharField(max_length=200)
    sub_text = RichTextField()
    email = models.EmailField(max_length=200)
    phone = PhoneNumberField()
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class ContactMessage(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.name


class GeneralSettings(models.Model):
    name = models.CharField(max_length=200)
    slogan = models.CharField(max_length=200)
    logo = models.ImageField(upload_to='general_settings/')
    faveicon = models.ImageField(upload_to='general_settings/')
    footer_text = models.CharField(max_length=200)
    base_color = models.CharField(max_length=100, help_text="Enter color code")

    def __str__(self):
        return self.name
