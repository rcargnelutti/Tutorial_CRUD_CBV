from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from exemplo.models import Cliente
from django.urls import reverse_lazy

# Create your views here.


class ClienteList(ListView):
    model = Cliente
    queryset = Cliente.objects.all()
    # pode especificar o arquivo html ou busca automatica na pasta templates pelo arquivo cliente_list.html
    # Configurar para buscar a pasta templates mo arquivo settings.py TEMPLATES = [{ 'DIRS': [os.path.join(BASE_DIR, 'templates')], }]


class ClienteCreate(CreateView):
    model = Cliente
    fields = '__all__'
    success_url = reverse_lazy('exemplo:list')
    # Por padrão utiliza o arquivo cliente_form.html


class ClienteUpdate(UpdateView):
    model = Cliente
    fields = '__all__'
    success_url = reverse_lazy('exemplo:list')
    # Utiliza o mesmo arquivo da CreateView - cliente_form.html


class ClienteDetail(DetailView):
    queryset = Cliente.objects.all()


class ClienteDelete(DeleteView):
    queryset = Cliente.objects.all()
    success_url = reverse_lazy('exemplo:list')
