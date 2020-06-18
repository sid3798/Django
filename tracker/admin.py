from django.contrib import admin
from .models import Patient

class PatientAdmin(admin.ModelAdmin):
    list_display=('name','age','diagnoses','created_on')
    search_fields=['name','diagnoses']
    ordering =('name',)

admin.site.register(Patient,PatientAdmin)