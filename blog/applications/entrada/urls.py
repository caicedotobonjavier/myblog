from django.urls import path, re_path, include
#
from . import views

app_name = 'entrada_app'


urlpatterns = [
    path('blog/', views.EntryListView.as_view(), name='blog'),
    path('detalle-entrada/<pk>/', views.DetailEntryView.as_view(), name='detalle'),
    #api
    path('api/entry/list/', views.ListaEntradasApi.as_view(), name='list'),
    path('api/category/new/', views.CrearCategoriaApi.as_view(), name='new_category'),
    path('api/category/new/entry/', views.CrearNuevaEntradaApi.as_view(), name='nueva_emtrada'),
]
