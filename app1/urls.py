from django.contrib import admin
from django.urls import path
from django.conf.urls import *
from .views import table_form, customized_crispy_form, crispy_form

urlpatterns = [
    
    path('crispyform/', crispy_form.as_view(),name="crispy-form"),
    path('customizedcrispyform/', customized_crispy_form.as_view(),name="customized-crispy-form"),
    path('', table_form.as_view(),name="table-form"),
]
