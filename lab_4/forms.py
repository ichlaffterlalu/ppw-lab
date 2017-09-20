from django import forms

class Message_Form(forms.Form):
    error_messages = {
        'required': 'Tolong isi input ini',
        'invalid': 'Isi input dengan email',
    }
    attrs = {
        'class': 'form-control'
    }

    name = forms.CharField(label='Nama', required=False, max_length=27, empty_value='Anonymous', widget=forms.TextInput(attrs=attrs))
    email = forms.EmailField(required=False, widget=forms.EmailInput(attrs=attrs))
    message = forms.CharField(widget=forms.Textarea(attrs=attrs), required=True)
