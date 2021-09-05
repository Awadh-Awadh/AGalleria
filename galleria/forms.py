from django import forms
from .models import Images


class PictureForm(forms.ModelForm):
  class Meta:
    model = Images
    fields = '__all__'