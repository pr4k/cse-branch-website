from django import forms
from .models import Document,Email

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('name','email','insta_handle', 'bio','upload', )

class EmailForm(forms.ModelForm):
    class Meta:
        model=Email
        fields=('email',)