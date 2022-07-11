from django import forms
from .models import Contact
from contactus .models import HireWriter


class ContactForm(forms.ModelForm):
    

    class Meta:
        model = Contact
        fields = ('__all__')
        


class HireWriterForm(forms.ModelForm):
    
    class Meta:
        model = HireWriter
        fields = ( '__all__')