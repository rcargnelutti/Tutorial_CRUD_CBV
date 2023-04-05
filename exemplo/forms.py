from django.forms import ModelForm

from exemplo.models import Cliente

class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'
