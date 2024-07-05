from typing import Any
from django.shortcuts import render
#
from django.views.generic import ListView, DetailView
#
from .models import Entry, Category
# Create your views here.


class EntryListView(ListView):
    template_name = 'entrada/blog.html'
    context_object_name = "entradas"

    def get_queryset(self):
        entrada = self.request.GET.get('kword')
        categoria = self.request.GET.get('categoria')
        if entrada or categoria:
            resultado = Entry.objects.buscar_entrada(entrada, categoria)
            return resultado
        else:
            return Entry.objects.all()
    

    def get_context_data(self, **kwargs) :
        context = super(EntryListView, self).get_context_data(**kwargs)
        
        context['categorias'] = Category.objects.all()
        return context


class DetailEntryView(DetailView):
    template_name = 'entrada/detalle-entrada.html'
    context_object_name = 'detalles'
    
    def get_queryset(self):
        dato = self.kwargs['pk']
        resultado = Entry.objects.filter(
            id = dato
        )
        return resultado