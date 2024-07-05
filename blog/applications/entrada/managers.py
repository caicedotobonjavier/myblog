#
from django.db import models


class EntryManagers(models.Manager):

    def entrada_portada(self):
        resultado = self.filter(
            public = True,
            portada = True,
        ).order_by('-created').first()
        #con first me devuelve el primer valor, no retorna un queryset sino un objecto

        return resultado


    def articulos_home(self):
        resutlado = self.filter(
            public = True,
            in_home = True
        ).order_by('-created')[:4]

        return resutlado


    def articulos_recientes(self):
        resultado = self.filter(
            public = True
        ).order_by('-created')[:6]

        return resultado
    

    def buscar_entrada(self, kword, categoria):
        if categoria:
            consulta = self.filter(
                category__short_name = categoria,                
                public = True
            )
            return consulta
        else:
            return self.filter(
                title__icontains = kword,
                public = True
            )
            



class CategoryManager():

    def all_categories(self):
        return self.all()
    

