from django.shortcuts import render
from django.views.generic import ListView
from exemplo.models import Cliente

# Create your views here.

class ClienteList(ListView):
    model = Cliente
    queryset = Cliente.objects.all()
    # pode especificar o arquivo html ou busca automatica na pasta templates pelo arquivo cliente_list.html
    # Configurar para buscar a pasta templates mo arquivo settings.py TEMPLATES = [{ 'DIRS': [os.path.join(BASE_DIR, 'templates')], }]
    