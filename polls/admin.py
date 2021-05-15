from django.contrib import admin
from . import models
# Register your models here.

class Register(admin.ModelAdmin):
    list_display = ['name', 'blood_group', 'state', 'city', 'home_address']

admin.site.register(models.donor_Registration, Register)

admin.site.register(models.sea_rch)

class Contact(admin.ModelAdmin):
    list_display = ['name', 'email']

admin.site.register(models.con_tact, Contact)


