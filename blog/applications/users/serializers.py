from rest_framework import serializers
#
from .models import User
#
from applications.entrada.models import Entry
#
from applications.entrada.serializers import SerializerEntry2



class SerializadorUser(serializers.ModelSerializer):

    entradas_creadas = serializers.SerializerMethodField()
    genero = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = (
            'id',
            'email',
            'full_name',
            'ocupation',
            'genero',
            'date_birth',        
            'is_staff',
            'is_active',
            'is_superuser',
            "entradas_creadas",
        )

    def get_genero(self, obj):
        return obj.get_genero_display()


    def get_entradas_creadas(self, obj):
        queryset = Entry.objects.filter(user__id = obj.id)
        serializador = SerializerEntry2(queryset, many=True).data
        return serializador