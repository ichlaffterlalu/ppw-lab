from django import forms

class Message_Form(forms.Form):
    error_messages = {
        'required': 'I am sad if you are not filling this field :(',
        'invalid': 'Well... I think you have put in something wrong :(',
    }
    attrs_name = {
        'class': 'form-control',
        'placeholder': 'Dennis Dien Pardede'
    }
    attrs_email = {
        'class': 'form-control',
        'placeholder': 'example@example.com'
    }
    attrs_message = {
        'class': 'form-control',
        'placeholder': 'This is a message for you.'
    }

    name = forms.CharField(label='Name', required=True, max_length=27, empty_value='Anonymous', widget=forms.TextInput(attrs=attrs_name))
    email = forms.EmailField(required=False, widget=forms.EmailInput(attrs=attrs_email))
    message = forms.CharField(widget=forms.Textarea(attrs=attrs_message), required=True)
