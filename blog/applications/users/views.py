from django.shortcuts import render
#
from .models import User
#
from applications.favoritos.models import Favorites
#
from django.views.generic import CreateView, FormView, View, TemplateView, UpdateView
#
from .forms import CreateUserForm, LoginForm, UpdateUserForm
#
from django.contrib.auth import login, logout, authenticate
#
from django.urls import reverse, reverse_lazy
#
from django.http import HttpResponseRedirect
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