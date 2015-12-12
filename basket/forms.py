from django.forms import ModelForm
from .models import Otlojit


class OtlojitForm(ModelForm):
    class Meta:
        model = Otlojit
        exclude = ['created_at']
        fields = ['zakaz']
