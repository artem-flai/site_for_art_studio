from django import forms
from django.core.exceptions import ValidationError
from captcha.fields import CaptchaField
from .models import *


class FormWrite(forms.ModelForm):
    captcha = CaptchaField()

    def __init__(self, num_mk, num_pict, *args, **kwargs):
        super().__init__(*args, **kwargs)
        set_mk = MasterClass.objects.get(pk=num_mk)
        self.fields['local'].initial = set_mk.local
        self.fields['date_mk'].initial = set_mk.date_mk
        self.fields['time_mk'].initial = set_mk.time_mk
        self.fields['price'].initial = set_mk.price

        if num_pict == 0:
            self.fields['name_picture'].initial = MasterClass.objects.get(pk=num_mk).name_picture
        else:
            self.fields['name_picture'].initial = Gallery_picture.objects.get(pk=num_pict).name_picture

    class Meta:
        model = MasterClass_Clients
        fields = ('local', 'date_mk', 'time_mk', 'price', 'name_picture', 'name_guest', 'tel_guest', 'email_guest',
                  'mobil_code')
        widgets = {
            "local": forms.TextInput(attrs={'readonly': 'readonly'}),
            "date_mk": forms.TextInput(attrs={'readonly': 'readonly'}),
            "time_mk": forms.TextInput(attrs={'readonly': 'readonly'}),
            "price": forms.TextInput(attrs={'readonly': 'readonly'}),
            "name_picture": forms.TextInput(attrs={'readonly': 'readonly'}),
        }

    def clean_tel_guest(self):
        tel_guest = self.cleaned_data['tel_guest']
        if len(tel_guest) < 7:
            raise ValidationError('Номер телефона должен состоять из 7 цифр')
        try:
            tel_guest = int(tel_guest)
        except:
            raise ValidationError('Номер телефона должен состоять из 7 цифр')
        return str(tel_guest)
