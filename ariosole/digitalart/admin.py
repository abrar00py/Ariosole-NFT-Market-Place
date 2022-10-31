import imp
import site
from django.contrib import admin

# Register your models here.
from .models import digitalart

admin.site.register(digitalart)