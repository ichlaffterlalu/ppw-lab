from django import forms

class Message_Form(forms.Form):
    error_default = {
        'required': 'I am sad if you are not filling the message field with real messages... :(',
        'invalid': 'Well... I think you have put something wrong to the email field. Check again, please... :(',
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

    name = forms.CharField(label='Name', max_length=27, empty_value='Anonymous', widget=forms.TextInput(attrs=attrs_name), required=False, error_messages=error_default)
    email = forms.EmailField(widget=forms.EmailInput(attrs=attrs_email), required=False, error_messages=error_default)
    message = forms.CharField(widget=forms.Textarea(attrs=attrs_message), required=True, error_messages=error_default)
