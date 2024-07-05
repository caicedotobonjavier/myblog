#
from applications.home.models import Home


def home_contact(request):
    home = Home.objects.latest('created')
    return {
        'telefono' : home.phone,
        'correo' : home.contat_email,
    }

