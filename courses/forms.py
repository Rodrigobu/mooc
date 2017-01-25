from django import forms

class ContractCourse(forms.Form):

    name = forms.CharField(label='Nome', max_length=100)
    email = forms.EmailField(label='Email')
    message = forms.CharField(label='Mensagem/Duvida', widget=forms.Textarea)
