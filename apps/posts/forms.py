from django import forms
from .models import Posts


class PosteoForm(forms.ModelForm):

    class Meta:
        model = Posts
        fields = ['titulo','contenido','imagen']

        