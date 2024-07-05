from django.shortcuts import render
#
from django.views.generic import View
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

        Favorites.objects.create(
            user = usuario,
            entry = entrada
        )


        return HttpResponseRedirect(
            reverse(
                'home_app:index'
            )
        )  