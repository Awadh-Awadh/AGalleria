from django import forms
from .models import Images
'''
form creation that will will inherit from forms.Models
include an inner class meta that defines which model to reference 
and generate field based on model
'''

class PictureForm(forms.ModelForm):
  class Meta:
    model = Images
    fields = '__all__'