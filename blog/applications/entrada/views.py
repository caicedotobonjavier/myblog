from typing import Any
from django.shortcuts import render
#
from django.views.generic import ListView, DetailView
#
from .models import Entry, Category, Tag
#
from applications.favoritos.models import Favorites
#
from django.contrib.auth.mixins import LoginRequiredMixin
#
from .serializers import SerializerEntry, Paginador, SerializerCategory, SerializadorEntradaNueva
#
from rest_framework.generics import ListAPIView, ListCreateAPIView, CreateAPIView
#
from rest_framework.views import APIView
#
from rest_framework.response import Response
# Create your views here.


class EntryListView(LoginRequiredMixin, ListView):
    template_name = 'entrada/blog.html'
    context_object_name = "entradas"
    paginate_by = 6
    login_url = 'users_app:login'

    def get_queryset(self):
        entrada = self.request.GET.get('kword')
        categoria = self.request.GET.get('categoria')
        if entrada or categoria:
            resultado = Entry.objects.buscar_entrada(entrada, categoria)
            return resultado
        else:
            return Entry.objects.filter(public=True)
    

    def get_context_data(self, **kwargs) :
        context = super(EntryListView, self).get_context_data(**kwargs)
        
        context['categorias'] = Category.objects.all()
        return context


class DetailEntryView(LoginRequiredMixin, DetailView):

    template_name = 'entrada/detalle-entrada.html'
    context_object_name = 'detalles'
    login_url = 'users_app:login'

    
    def get_queryset(self):
        dato = self.kwargs['pk']
        resultado = Entry.objects.filter(
            id = dato
        )        
        return resultado


#API
class ListaEntradasApi(ListAPIView):
    serializer_class = SerializerEntry
    pagination_class = Paginador
    
    def get_queryset(self):
        resultado = Entry.objects.all()
        return resultado


class CrearCategoriaApi(ListCreateAPIView):
    serializer_class = SerializerCategory

    def get_queryset(self):
        return Category.objects.all()



class CrearNuevaEntradaApi(APIView):
    serializer_class = SerializadorEntradaNueva

    def post(self, request, *args, **kwargs):
        serializador = self.serializer_class(data=request.data)
        serializador.is_valid(raise_exception=True)
        
        category = Category.objects.get(id=serializador.validated_data['category'])
        tag = Tag.objects.filter(id__in = serializador.validated_data['tag'])
        title = serializador.validated_data['title']
        resume = serializador.validated_data['resume']
        content = serializador.validated_data['content']
        image = self.request.FILES['image']

        entrada = Entry.objects.create(
            user =self.request.user,
            category = category,
            title = title,
            resume = resume,
            content = content,
            image = image
        )

        for t in tag:
            entrada.tag.add(t)
            entrada.save()


        return Response(
            {
                'Entrada' : 'Guardada Exitosamente'
            }
        )