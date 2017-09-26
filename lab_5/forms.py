from django import forms

class Todo_Form(forms.Form):
    error_messages = {
        'required': 'Tolong isi input ini',
    }
    title_attrs = {
        'type': 'text',
        'class': 'todo-form-input',
        'placeholder':'Masukan judul...'
    }
    description_attrs = {
        'type': 'text',
        'cols': 50,
        'rows': 4,
        'class': 'todo-form-textarea',
        'placeholder':'Masukan deskripsi...'
    }

    title = forms.CharField(label='', required=True, max_length=27, widget=forms.TextInput(attrs=title_attrs))
    description = forms.CharField(label='', required=True, widget=forms.Textarea(attrs=description_attrs))
