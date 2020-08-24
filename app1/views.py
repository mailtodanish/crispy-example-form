from django.shortcuts import render
from django.views.generic.edit import FormView
from .form import AddressForm
from django.urls import reverse_lazy


class customized_crispy_form(FormView):
    form_class = AddressForm
    template_name = 'app1/customized_crispy_form.html'

class table_form(FormView):
    template_name = 'app1/form_as_table.html'
    form_class = AddressForm
    

class crispy_form(FormView):
    form_class = AddressForm
    template_name = 'app1/form_as_crispy.html'
    