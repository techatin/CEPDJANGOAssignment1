from django import forms
from .models import Subject, Homework
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field

class HomeworkForms(forms.ModelForm):
    """name = forms.CharField(max_length=255)
    description = forms.TextField(default="A homework to be done")
    subject = forms.ModelChoiceField(Subject.objects.all)"""
    
    class Meta:
        model = Homework
        
    helper = FormHelper()
    helper.form_method = 'POST'
    helper.add_input(Submit('Save', 'Save', css_class='btn-primary'))
