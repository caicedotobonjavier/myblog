from rest_framework import serializers, pagination
#
from .models import Category, Tag, Entry
#



class SerializerCategory(serializers.ModelSerializer):

    entrada = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = (
            'id',
            'short_name',
            'name',
            'entrada',
        )
    
    def get_entrada(self, obj):
        queryset = Entry.objects.buscar_categorias(obj.id)
        serializador = SerializerEntry2(queryset, many=True).data
        return serializador



class SerializerTag(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = (
            'id',
            'name',
        )


class SerializerEntry(serializers.HyperlinkedModelSerializer):

    category = SerializerCategory()
    tag = SerializerTag(many=True)
    
    class Meta:
        model = Entry
        fields = (
            'id',
            'user',
            'category',
            'tag',
            'title',
            'resume',
            'content',
            'public',
            'image',       
        )
    
        extra_kwargs = {
            'user' : {'view_name' : 'users_app:detail', 'lookup_field' : 'pk'}
        }



class Paginador(pagination.PageNumberPagination):
    page_size = 2
    max_page_size = 100



class SerializerEntry2(serializers.ModelSerializer):
    class Meta:
        model = Entry
        fields = (
            'id',
            'user',
            'category',
            'tag',
            'title',
            'resume',
            'content',
            'public',
            'image',       
        )

class ListaTags(serializers.ListField):
    child = serializers.IntegerField()


class SerializadorEntradaNueva(serializers.Serializer):    
    category = serializers.CharField()
    tag = ListaTags()
    title = serializers.CharField()
    resume = serializers.CharField()
    content = serializers.CharField()
    image = serializers.ImageField()