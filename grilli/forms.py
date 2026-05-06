from django import forms
from .models import EmailModel, TableModel

class EmailForm(forms.ModelForm):
    class Meta:
        model = EmailModel
        fields = ['email_address']

class TableForm(forms.ModelForm):
    class Meta:
        model = TableModel
        fields = ['name', 'phone', 'person', 'date', 'time', 'message']