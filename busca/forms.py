from django import forms
from .models import Contato

class ContatoForm(forms.ModelForm):

    class Meta:
        model = Contato
        fields = ('contato_nome',
                  'description',
                  'contato_nascimento',
                  'contato_sexo',
                  'contato_email',
                  'contato_fone' )