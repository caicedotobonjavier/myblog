from django.shortcuts import render
#
from django.views.generic import TemplateView, View, CreateView, FormView
#
from django.contrib.auth.mixins import LoginRequiredMixin
#
from django.urls import reverse, reverse_lazy
#
from .models import Suscribers, Contact
#
from applications.entrada.models import Entry
#
from .forms import SuscribersForm, ContactoForm
# Create your views here.


class HomePageView(TemplateView):
    template_name = 'home/index.html'


    def get_context_data(self, **kwargs):
        context = super(HomePageView,self).get_context_data(**kwargs)

        #contexto portada
        context["portada"] = Entry.objects.entrada_portada()
        #contexto in_home
        context['home'] = Entry.objects.articulos_home()
        #contexto articulos recientes
        context['recientes'] = Entry.objects.articulos_recientes()    
        #
        context['form'] = SuscribersForm


        return context


#este registro con solo el createview funcionaria y el formvalid sobraria
class RegistrarSuscriptorViw(FormView):
    form_class = SuscribersForm
    success_url = reverse_lazy('home_app:index')

    def form_valid(self, form):
        email = form.cleaned_data['email']
        Suscribers.objects.create(
            email = email
        )
        return super(RegistrarSuscriptorViw, self).form_valid(form)


#este registro con solo el createview funcionaria y el formvalid sobraria
class ContactView(FormView):
    form_class = ContactoForm
    success_url = reverse_lazy('home_app:index')

    def form_valid(self, form):
        full_name = form.cleaned_data['full_name']
        email = form.cleaned_data['email']
        messagge = form.cleaned_data['messagge']
        Contact.objects.create(
            full_name = full_name,
            email = email,
            messagge = messagge
        )
        return super(ContactView, self).form_valid(form)
    