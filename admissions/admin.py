from django.contrib import admin
from .models import Admission
# Register your models here.
class AdmissionAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'date_of_birth', 'address')

admin.site.register(Admission, AdmissionAdmin)