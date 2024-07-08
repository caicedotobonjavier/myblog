from django.urls import path, re_path, include
#
from . import views

app_name = 'users_app'


urlpatterns = [
    path('crear-usuario/', views.CreateUserView.as_view(), name='create_user'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('loguot/', views.LogoutView.as_view(), name='logout'),
    path('perfil/', views.PerfilUserView.as_view(), name='perfil'),
    path('update/<pk>/', views.UpdateInfoUserView.as_view(), name='update_user'),
    path('change-password/', views.ChangePasswordUserView.as_view(), name='change_password'),
    #API
    path('api/users/list/', views.ListaUsersApi.as_view(), name='list'),
    path('api/users/detail/<pk>/', views.DetailUserApi.as_view(), name='detail'),
]