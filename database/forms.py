from database.models import *
from django import forms
from django.utils.translation import ugettext_lazy as _


class studentform(forms.ModelForm):

    class Meta:
        model=student
        fields='__all__'
        labels = {
            'name': _('Name'),
            'rollno':_('Roll-No'),
            'cpi':_('CPI'),
            'category':_('Category'),
            'currentbranch':_('Current Branch'),
            'branchops':_('Branch Options')
        }
        help_texts={
            'name':_('Enter your name'),
            'rollno':_('Enter your IITB rollno'),
            'cpi':_('Enter you 1st year CPI.'),
            'category':_('Enter your birth category'),
        }
        error_messages = {
            'name': {
                'max_length': _("User's name is too long."),
            },
            'rollno':{
                'max_length': _('Roll no is too long.'),
                'Badprefix':_('Invalid roll no')
            }

        }




    def clean_rollno(self):
        rollno=self.cleaned_data['rollno'].strip()
        if not rollno.startswith("15"):
            raise forms.ValidationError('Invalid RollNo',code="Badprefix")
        return rollno



