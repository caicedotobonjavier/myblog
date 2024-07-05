from django.urls import path, re_path, include
#
from . import views

app_name = 'home_app'


urlpatterns = [
    path('', views.HomePageView.as_view(), name='index'),
    path('suscribirse', views.RegistrarSuscriptorViw.as_view(), name='suscribirse'),
    path('contacto/', views.ContactView.as_view(), name='contacto'),
]
