from django import forms
from .models import Tarea

from django import forms
from .models import Tarea

class TareaForm(forms.ModelForm):
    fecha_vencimiento = forms.DateTimeField(
            input_formats=['%d/%m/%Y %H:%M', '%d/%m/%y %H:%M','%d-%m-%Y %H:%M', '%d-%m-%y %H:%M','%d/%m/%Y', '%d/%m/%y','%d-%m-%Y', '%d-%m-%y'],
            widget=forms.TextInput(attrs={
            'placeholder': 'dd/mm/yyyy HH:MM',
            'readonly': 'readonly',  # Deshabilita la entrada manual
        })
        )
    class Meta:
        model = Tarea
        fields = ['titulo', 'fecha_vencimiento', 'tarea', 'is_concluida']
        
