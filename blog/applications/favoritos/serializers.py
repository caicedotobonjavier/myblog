from rest_framework import serializers
#
from .models import Favorites


class SerializerFavorites(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Favorites
        fields = (
            'id',
            'user',
            'entry',
        )
    
        extra_kwargs = {
            'user' : {'view_name' : 'users_app:detail', 'lookup_field' : 'pk'},
            'entry' : {'view_name' : 'entrada_app:detalle_entrada', 'lookup_field' : 'pk'}
        }