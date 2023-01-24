from django.urls import reverse
from django.db import models

# Create your models here.

class MasterClass(models.Model):
    local = models.CharField(max_length=180)
    date_mk = models.DateField()
    time_mk = models.TimeField()
    price = models.CharField(max_length=80)
    view_of_clients = models.CharField(max_length=120)
    foto = models.ImageField(upload_to="picture")
    name_picture = models.CharField(max_length=16, null=True)
    activation = models.BooleanField(default=True)

    def get_absolute_url(self):
        return reverse('gallery_picture', kwargs={'ip_mk': self.pk})

    def get_absolute_url_form(self):
        return reverse('form_writer', kwargs={'ip_mk': self.pk})

    class Meta:
        verbose_name = "Мастер-классы"
        verbose_name_plural = "Мастер-классы"


class MasterClass_Clients(models.Model):
    code = [('+37533', '(33)'), ('+37544', '(44)'), ('+37529', '(29)'), ('+37525', '(25)')]
    local = models.CharField(max_length=50, verbose_name='Адрес провения мастер-класса')
    date_mk = models.DateField(verbose_name='Дата проведения мастер-класса')
    time_mk = models.TimeField(verbose_name='Время проведения мастер-класса')
    price = models.CharField(max_length=20, verbose_name='Стоимость мастер-класса')
    name_picture = models.CharField(max_length=16, null=True, verbose_name='Название картины')
    name_guest = models.CharField(max_length=50, verbose_name='Ваше имя')
    tel_guest = models.CharField(max_length=7, verbose_name='Ваш номер телефона')
    email_guest = models.EmailField(blank=True, null=True, verbose_name='Ваш е-маил (необязательно)')
    mobil_code = models.CharField(max_length=6, null=True, choices=code, verbose_name='mobil_code')


    def __str__(self):
        return self.name_picture

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"


class Gallery_picture(models.Model):
    name_picture = models.CharField(max_length=180)
    foto = models.ImageField(upload_to="picture")

    def __str__(self):
        return self.name_picture

    def get_absolute_url(self):
        return reverse('form_writer', kwargs={'ip_pict': self.pk})

    class Meta:
        verbose_name = "Галерея"
        verbose_name_plural = "Галерея"