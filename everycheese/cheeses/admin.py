from django.contrib import admin
from .models import Cheese


# Register your models here.
admin.site.register(Cheese)

#The above code gives us admin UI for entering cheeses, accessible from the Cheeses section