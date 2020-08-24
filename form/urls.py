from django.contrib import admin
from django.urls import path
from django.conf.urls import *

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'', include('app1.urls')),
]
