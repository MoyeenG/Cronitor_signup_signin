from django.contrib import admin

# Register your models here.
from .models import Signup, Signin

admin.site.register(Signup)
admin.site.register(Signin)
