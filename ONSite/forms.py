from django import forms
from .models import Issue, Files
from AdminMedule.models import Station

class CreateIssueForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = ['id', 'title', 'issue_type', 'channel', 'module','device_serial',
                'description', 'affects_version', 'train_number' , 'train_to', 'train_from',
                'priority', 'station', 'subscription_type', 'subscription_number',
                'subscription_expiry_date', 'teller_name', 'teller_phone', 'trans_number', 'trip_date' ]

        widgets = {
            'title' : forms.TextInput(
                attrs={
                    'class':'form-control border border-primary',
                    'id':'title',
                    'name':'title',
                    'placeholder':'Add title here.....',
                    'placeholder': 'Type Here...'
                }
            ),

            'priority' : forms.Select(
                attrs={
                    'class':'form-control shadow p-3 mb-5',
                    'id':'priority',
                    'name':'priority',
                    'placeholder': 'Type Here...'
                }
            ),

            'channel' : forms.Select(
                attrs={
                    'class':'form-control border border-primary',
                    'id':'channel',
                    'name':'channel',
                    'placeholder': 'Type Here...'
                }
            ),

            'id' : forms.Select(attrs={
                'class':'form-control border border-primary ',
                'name':'id'
                }
            ),

            'module' : forms.Select(attrs={
                'class':'form-control border border-primary ',
                'id':'module_div',
                'name':'module_div',
                'placeholder': 'Type Here...'
                }
            ),

            'device_serial' : forms.Select(attrs={
                'class':'form-control  border border-primary',
                'id':'device_serial',
                'name':'device_serial',
                'placeholder': 'Type Here...'
                }
            ),

            'description' : forms.Textarea(attrs={
                'class':'form-control border border-primary ',
                'id':'description',
                'name':'description',
                'placeholder': 'Type Here...'
                }
            ),

            'affects_version' : forms.TextInput(attrs={
                'class':'form-control border border-primary ',
                'id':'affects_version',
                'name':'affects_version',
                'placeholder': 'Type Here...'
                 }
            ),

            'train_number': forms.TextInput(attrs={
                'class': 'form-control border border-primary ',
                'id': 'train_number',
                'name': 'train_number',
                'placeholder': 'Type Here...'
                }
            ),

            'train_from': forms.TextInput(attrs={
                'class': 'form-control border border-primary '
                , 'id': 'train_from',
                'name': 'train_from',
                'placeholder': 'Type Here...'
                }
            ),

            'train_to': forms.TextInput(attrs={
                'class': 'form-control border border-primary ',
                'id': 'train_to',
                'name': 'train_to',
                'placeholder': 'Type Here...'
                }
            ),

            'station' : forms.Select(attrs={
                'class':'form-control border border-primary ',
                'id':'station',
                'name':'station',
                'placeholder': 'Type Here...'
                }
            ),

            'subscription_type':forms.TextInput(attrs={
                'class':'form-control border border-primary ',
                'id':'subscription_type',
                'name':'subscription_type',
                'placeholder': 'Type Here...'
                }
            ),

            'subscription_number':forms.NumberInput(attrs={
                'class':'form-control border border-primary ',
                'id':'subscription_number',
                'name':'subscription_number',
                'placeholder': 'Type Here...'
                }
            ),

            'subscription_expiry_date':forms.DateInput(attrs={
                'class':'form-control border border-primary ',
                'type':'date', 'id':'subscription_expiry_date',
                'name':'subscription_expiry_date',
                'placeholder': 'Type Here...'
                }
            ),

            'trip_date': forms.DateInput(attrs={
                'class': 'form-control border border-primary ',
                'type': 'date', 'id': 'trip_date',
                'name': 'trip_date',
                'placeholder': 'Type Here...'
            }
            ),

            'teller_name': forms.TextInput( attrs={
                'class': 'form-control border border-primary',
                'id': 'teller_name',
                'name': 'teller_name',
                'placeholder': 'Type Here...'
                }
            ),

            'teller_phone': forms.TextInput(attrs={
                'class': 'form-control border border-primary',
                'id': 'teller_phone',
                'name': 'teller_phone',
                'placeholder': 'Type Here...'
                }
            ),

            'trans_number': forms.TextInput(attrs={
                'class': 'form-control border border-primary',
                'id': 'trans_number',
                'name': 'trans_number',
                'placeholder': 'Type Here...'
                }
            ),
        }


# file form
class FilesForm(forms.ModelForm):
    class Meta:
        model = Files
        fields = ['files', 'issue']

# Assign to user form
class AssignForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = ['assignee']

        widgets = {
            'assignee': forms.Select(attrs={'class':'form-control border border-primary', 'id':'assignee', 'name':'assignee'})
        }

# Follwer form
class Follwer(forms.ModelForm):
    class Meta:
        model = Issue
        fields = ['actor']

        widgets = {
            'actor': forms.Select(attrs={'class':'form-control border border-primary', 'id':'actor', 'name':'actor'})
        }


