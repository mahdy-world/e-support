from django import forms
from .models import Issue, Files
from AdminMedule.models import Station

class CreateIssueForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = ['id', 'title', 'issue_type', 'channel', 'module','device_serial',
                  'description', 'affects_version', 'train', 'priority', 'station', 'subscription_type', 'subscription_number',
                    'subscription_expiry_date', 'teller_name', 'teller_phone', 'trans_number' ]
        widgets = {
            'title' : forms.TextInput(attrs={'class':'form-control border border-primary', 'id':'title', 'name':'title'}),
            'priority' : forms.Select(attrs={'class':'form-control shadow p-3 mb-5', 'id':'priority', 'name':'priority'}),
            'channel' : forms.Select(attrs={'class':'form-control border border-primary ', 'id':'channel', 'name':'channel'}),
            'id' : forms.Select(attrs={'class':'form-control border border-primary ',  'name':'id'}),
            'module' : forms.Select(attrs={'class':'form-control border border-primary ', 'id':'module', 'name':'module'}),
            'device_serial' : forms.Select(attrs={'class':'form-control  border border-primary', 'id':'device_serial', 'name':'device_serial'}),
            'description' : forms.Textarea(attrs={'class':'form-control border border-primary ', 'id':'description', 'name':'description'}),
            'affects_version' : forms.TextInput(attrs={'class':'form-control border border-primary ', 'id':'affects_version', 'name':'affects_version'}),
            'train' : forms.Select(attrs={'class':'form-control border border-primary ', 'id':'train', 'name':'train'}),
            'station' : forms.Select(attrs={'class':'form-control border border-primary ', 'id':'train', 'name':'station'}),
            'subscription_type':forms.TextInput(attrs={'class':'form-control border border-primary ', 'id':'subscription_type', 'name':'subscription_type'}),
            'subscription_number':forms.NumberInput(attrs={'class':'form-control border border-primary ', 'id':'subscription_number', 'name':'subscription_number'}),
            'subscription_expiry_date':forms.DateInput(attrs={'class':'form-control border border-primary ', 'type':'date', 'id':'subscription_expiry_date', 'name':'subscription_expiry_date'}),
            'teller_name': forms.TextInput( attrs={'class': 'form-control border border-primary', 'id': 'teller_name', 'name': 'teller_name'}),
            'teller_phone': forms.TextInput(attrs={'class': 'form-control border border-primary', 'id': 'teller_phone', 'name': 'teller_phone'}),
            'trans_number': forms.TextInput(attrs={'class': 'form-control border border-primary', 'id': 'trans_number', 'name': 'trans_number'}),
        }



class FilesForm(forms.ModelForm):
    class Meta:
        model = Files
        fields = ['files', 'issue']


class AssignForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = ['reporter']

        widgets = {
            'reporter': forms.Select(attrs={'class':'form-control border border-primary', 'id':'reporter', 'name':'reporter'})
        }



