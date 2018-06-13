from django import forms
from .models import Inner_Excel, Outter_Excel

class Inner_Form(forms.ModelForm):
    class Meta:
        model = Inner_Excel
        fields = ('inner_excel', )

class Outter_Form(forms.ModelForm):
    class Meta:
        model = Outter_Excel
        fields = ('outter_excel', )
