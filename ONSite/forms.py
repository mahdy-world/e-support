from django import forms
from Core.models import *

class CreateIssueForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = ['id', 'title', 'issue_type', 'channel', 'module',
                  'device_serial', 'description', 'supscription_type', 'affects_version', 'train', ]
        widgets = {
            'title' : forms.TextInput(attrs={'class':'form-control shadow p-3 mb-5', 'id':'title', 'name':'title'}),
            'issue_type' : forms.Select(attrs={'class':'form-control shadow p-3 mb-5 issue_type', 'id':'issue_type', 'name':'issue_type'}),
            # 'priority' : forms.Select(attrs={'class':'form-control shadow p-3 mb-5', 'id':'priority', 'name':'priority'}),
            'channel' : forms.Select(attrs={'class':'form-control shadow p-3 mb-5', 'id':'channel', 'name':'channel'}),
            'id' : forms.Select(attrs={'class':'form-control shadow p-3 mb-5',  'name':'id'}),
            'module' : forms.Select(attrs={'class':'form-control shadow p-3 mb-5', 'id':'module', 'name':'module'}),
            'device_serial' : forms.Select(attrs={'class':'form-control shadow p-3 mb-5', 'id':'device_serial', 'name':'device_serial'}),
            'description' : forms.Textarea(attrs={'class':'form-control shadow p-3 mb-5', 'id':'description', 'name':'description'}),
            'supscription_type' : forms.TextInput(attrs={'class':'form-control shadow p-3 mb-5', 'id':'supscription_type', 'name':'supscription_type'}),
            'affects_version' : forms.TextInput(attrs={'class':'form-control shadow p-3 mb-5', 'id':'affects_version', 'name':'affects_version'}),
            'train' : forms.TextInput(attrs={'class':'form-control shadow p-3 mb-5', 'id':'train', 'name':'train'}),
            # 'file' : forms.ClearableFileInput(attrs={'class':'custom-file-input shadow p-3 mb-5', 'id':'file', 'multiple':'True', 'name':'file'}),
        }