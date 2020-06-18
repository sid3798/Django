  
from django import forms
from .models import Patient

class PatientAdmitForm(forms.ModelForm):

    name = forms.CharField(max_length=50)
    age = forms.IntegerField()
    diagnoses = forms.CharField(max_length=50)

    class Meta:
        model = Patient
        fields = ('name', 'age', 'diagnoses')