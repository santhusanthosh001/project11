from django.contrib import admin
from .models import Reg


# Register your models here.
class Admin(admin.ModelAdmin):
    list_display = ('First_name', 'Last_name', 'user_name', 'password', 'cpassword', 'emailid','mobilenumber')
    list_filter = ('First_name', 'Last_name', 'user_name', 'password', 'cpassword', 'emailid','mobilenumber')
admin.site.register(Reg, Admin)