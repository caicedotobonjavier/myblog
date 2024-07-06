from django.urls import path, re_path, include
#
from . import views

app_name = 'favoritos_app'


urlpatterns = [
    path('add-favorito/<pk>/', views.AddFavorite.as_view(), name='add_favorito'),   
    path('delete/<pk>/', views.DelteFavoriteView.as_view(), name='delete_favorito'),  
]