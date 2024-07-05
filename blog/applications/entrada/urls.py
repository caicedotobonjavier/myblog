from django.urls import path, re_path, include
#
from . import views

app_name = 'entrada_app'


urlpatterns = [
    path('blog/', views.EntryListView.as_view(), name='blog'),
    path('detalle-entrada/<pk>/', views.DetailEntryView.as_view(), name='detalle'),
]
