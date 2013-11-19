from django import forms
from volunteer.base.models import Volunteer
from django.contrib.auth.forms import UserCreationForm


class VolunteerForm(UserCreationForm):
    
    def __init__(self, *args, **kwargs):
        super(VolunteerForm, self).__init__(*args, **kwargs)
        self.fields['availibility'].help_text = None
        self.fields['last_login'].widget = forms.HiddenInput()
        self.fields['date_joined'].widget = forms.HiddenInput()
        self.fields['is_active'].widget = forms.HiddenInput()
        self.fields['password'].widget = forms.HiddenInput()
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
        self.fields['email'].required = True
        self.fields['password'].required = False
    
    def save(self, commit=True):
        user = UserCreationForm.save(self, commit=commit)
        self.save_m2m();
        return user
    
    class Meta:
        model = Volunteer
        
class UpdateVolunteerForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(UpdateVolunteerForm, self).__init__(*args, **kwargs)
        self.fields['availibility'].help_text = None
        self.fields['last_login'].widget = forms.HiddenInput()
        self.fields['date_joined'].widget = forms.HiddenInput()
        self.fields['is_active'].widget = forms.HiddenInput()
        self.fields['password'].widget = forms.HiddenInput()
                
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
        self.fields['email'].required = True
    
    class Meta:
        model = Volunteer
    