from django.shortcuts import render
#
from django.views.generic import View, DeleteView
#
from django.urls import reverse, reverse_lazy
#
from django.http import HttpResponseRedirect
#
from applications.entrada.models import Entry
#
from .models import Favorites
# Create your views here.


class AddFavorite(View):    

    def post(self, request, *args, **kwargs):
        entrada = Entry.objects.get(id=self.kwargs['pk'])
        usuario = self.request.user

        Favorites.objects.get_or_create(
            user = usuario,
            entry = entrada
        )


        return HttpResponseRedirect(
            reverse(
                'users_app:perfil'
            )
        )  



class DelteFavoriteView(View):    

    def post(self, request, *args, **kwargs):
        pk = self.kwargs['pk']

        favorito = Favorites.objects.filter(
            id=pk,
        )

        print(favorito)
        
        favorito.delete()
        

        return HttpResponseRedirect(
            reverse(
                'users_app:perfil'
            )
        )