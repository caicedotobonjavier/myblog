from django.urls import path, re_path, include
#
from . import views

app_name = 'users_app'


urlpatterns = [
    path('crear-usuario/', views.CreateUserView.as_view(), name='create_user'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('loguot/', views.LogoutView.as_view(), name='logout'),
]