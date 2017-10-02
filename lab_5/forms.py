from django import forms

class Todo_Form(forms.Form):
	error_desc = {
		'required': 'Please fill the description with real thing.',
	}
	error_title = {
		'required': 'Please fill the title with real thing.',
	}
	title_attrs = {
		'type': 'text',
		'class': 'todo-form-input',
		'placeholder':'Insert title here...'
	}
	description_attrs = {
		'type': 'text',
		'cols': 50,
		'rows': 4,
		'class': 'todo-form-textarea',
		'placeholder':'Insert description here...'
	}

	title = forms.CharField(label='', required=True, max_length=27, widget=forms.TextInput(attrs=title_attrs), error_messages=error_title)
	description = forms.CharField(label='', required=True, widget=forms.Textarea(attrs=description_attrs), error_messages=error_desc)
