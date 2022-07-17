from django import forms
from .models import Issue, Files

class CreateIssueForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = ['id', 'title', 'issue_type', 'channel', 'module',
                  'device_serial', 'description', 'supscription_type', 'affects_version', 'train', ]
        widgets = {
            'title' : forms.TextInput(attrs={'class':'form-control border border-primary', 'id':'title', 'name':'title'}),
            'issue_type' : forms.Select(attrs={'class':'form-control border border-primary  issue_type', 'id':'issue_type', 'name':'issue_type'}),
            # 'priority' : forms.Select(attrs={'class':'form-control shadow p-3 mb-5', 'id':'priority', 'name':'priority'}),
            'channel' : forms.Select(attrs={'class':'form-control border border-primary ', 'id':'channel', 'name':'channel'}),
            'id' : forms.Select(attrs={'class':'form-control border border-primary ',  'name':'id'}),
            'module' : forms.Select(attrs={'class':'form-control border border-primary ', 'id':'module', 'name':'module'}),
            'device_serial' : forms.Select(attrs={'class':'form-control  border border-primary', 'id':'device_serial', 'name':'device_serial'}),
            'description' : forms.Textarea(attrs={'class':'form-control border border-primary ', 'id':'description', 'name':'description'}),
            'supscription_type' : forms.TextInput(attrs={'class':'form-control border border-primary ', 'id':'supscription_type', 'name':'supscription_type'}),
            'affects_version' : forms.TextInput(attrs={'class':'form-control border border-primary ', 'id':'affects_version', 'name':'affects_version'}),
            'train' : forms.TextInput(attrs={'class':'form-control border border-primary ', 'id':'train', 'name':'train'}),
            # 'file' : forms.ClearableFileInput(attrs={'class':'custom-file-input shadow p-3 mb-5', 'id':'file', 'multiple':'True', 'name':'file'}),
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
