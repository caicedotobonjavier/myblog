from django.shortcuts import render
#
from .models import User
#
from rest_framework.authtoken.models import Token
#
from applications.favoritos.models import Favorites
#
from django.views.generic import CreateView, FormView, View, TemplateView, UpdateView
#
from .forms import CreateUserForm, LoginForm, UpdateUserForm, ChangePasswordForm
#
from django.contrib.auth import login, logout, authenticate
#
from django.urls import reverse, reverse_lazy
#
from django.http import HttpResponseRedirect
#
from rest_framework.generics import ListAPIView, RetrieveAPIView
#
from rest_framework.views import APIView
#
from rest_framework.response import Response
#
from .serializers import SerializadorUser, SerializadorLoginUser
# Create your views here.


class CreateUserView(FormView):
    template_name = 'users/create-user.html'
    form_class = CreateUserForm
    success_url = reverse_lazy('users_app:create_user')


    def form_valid(self, form):
        email = form.cleaned_data['email']
        password1 = form.cleaned_data['password1']        

        user = User.objects.create_user(
            form.cleaned_data['email'],
            form.cleaned_data['password1'],      
            full_name = form.cleaned_data['full_name'],
            ocupation = form.cleaned_data['ocupation'],
            genero = form.cleaned_data['genero'],
            date_birth = form.cleaned_data['date_birth'],
        )        

        return super(CreateUserView, self).form_valid(form)



class LoginView(FormView):
    form_class = LoginForm
    template_name = 'users/login.html'
    success_url = reverse_lazy('home_app:index')

    def form_valid(self, form):
        usuario = form.cleaned_data['email']
        contrasena = form.cleaned_data['password']

        print(usuario, contrasena)

        user = authenticate(
            email=usuario, 
            password=contrasena
        )

        print(user)

        login(self.request, user)

        return super(LoginView, self).form_valid(form)


class LogoutView(View):
    
    def get(self, request, *args, **kwargs):

        logout(request)        

        return HttpResponseRedirect(
            reverse(
                'users_app:login'
            )
        )


class PerfilUserView(TemplateView):
    template_name = 'users/perfil.html'
    
    def get_context_data(self, **kwargs):
        context = super(PerfilUserView, self).get_context_data(**kwargs)
        usuario = self.request.user        
        context["favoritos"] = Favorites.objects.filter(user=usuario)
        
        return context


class UpdateInfoUserView(UpdateView):
    template_name = 'users/update-user.html'
    form_class = UpdateUserForm
    model = User
    success_url = reverse_lazy('users_app:perfil')



class ChangePasswordUserView(FormView):
    template_name = 'users/change-password.html'
    form_class = ChangePasswordForm
    success_url = reverse_lazy('users_app:login')


    def get_form_kwargs(self):
        kwargs = super(ChangePasswordUserView, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs


    def form_valid(self, form):
        usuario = self.request.user
        contrasena = form.cleaned_data['password1']
        new_password = form.cleaned_data['password2']

        user = authenticate(
            email=usuario,
            password = contrasena
        )

        if user:
            user.set_password(new_password)
            user.save()
        
        logout(self.request)

        return super(ChangePasswordUserView, self).form_valid(form)
    


#API
class ListaUsersApi(ListAPIView):
    serializer_class = SerializadorUser

    def get_queryset(self):
        resultado = User.objects.all()
        return resultado


class DetailUserApi(RetrieveAPIView):
    serializer_class = SerializadorUser

    def get_queryset(self):
        dato = self.kwargs['pk']
        resultado = User.objects.filter(id=dato)
        return resultado



class LoginUserApi(APIView):
    serializer_class = SerializadorLoginUser


    def post(self, request, *args, **kwargs):
        serializador = self.serializer_class(data=request.data)
        serializador.is_valid(raise_exception=True)

        usuario = serializador.validated_data['user']
        contrasena = serializador.validated_data['password']

        user = authenticate(email=usuario, password=contrasena)

        if user:
            token, created = Token.objects.get_or_create(
                user = user
            )

            token_user = {
                "token" : token.key,  
                "created" : token.created           
            }

            login_user = {
                "username" : user.email,
                "nombre" : user.full_name,
                "ocupacion" : user.ocupation,
                "fecha_nacimiento" : user.date_birth,
                "genero" : user.get_genero_display(),
                "usuario_activo" : user.is_active,
                "usuerio_administrador" : user.is_superuser,                
                "ultimo_logueo" : user.last_login
                
            }

            return Response(
                {
                    'access' : "successful",
                    'user_info' : login_user,
                    'token': token_user
                }
            )
        else:
            return Response(
                {
                    'access' : "denied",
                    "answer" : "No se encontro el usuario"
                }
            )