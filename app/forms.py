from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm




class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="Email", max_length=254,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter a correct email'}))
    username = forms.CharField(max_length=254,widget=forms.TextInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(max_length=254,widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=254,widget=forms.TextInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(label="Password",widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label="Confirm password",widget=forms.PasswordInput(attrs={'class':'form-control'}))
    

    
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['email'].required = True
        #self.fields.pop('username')
        #self.fields.pop('password2')

    def clean_email(self):
        # Get the email
        email = self.cleaned_data.get('email')
    
        # Check to see if any users already exist with this email as a username.
        try:
            match = User.objects.get(email=email)
        except User.DoesNotExist:
            # Unable to find a user, this is fine
            return email

        # A user was found with this as a username, raise an error.
        raise forms.ValidationError('This Email address is already in use.')
    
    def clean_username(self):
        # Get the email
        username = self.cleaned_data.get('username')
    
        wrong = '@'
        if wrong in username:
            raise forms.ValidationError('Username contains invalid characters')
        else:
            return username

    class Meta:
        model = User
        fields = ('username', 'first_name','last_name','email','password1', 'password2')

class ProfileForm(forms.ModelForm):
    radio_choice = [
        ('Male', 'Male'),
        ('Female', 'Female')
    ]
    field = (
        ('1',' AA'),
        ('2','AS'),
        ('3','AC'),
        ('4','SS'),
        ('5','SC'),
        ('6','CC'),

    )
    field = (
        ('Malaria','Malaria'),
        ('Typhoid','Typhoid Fever'),
        ('Diarrhea','Diarrhea'),
        ('Headaches','Headaches'),
        ('Cholera','Cholera'),
        ('Ebola','Ebola'),

    )
    gender = forms.ChoiceField(choices=radio_choice, widget=forms.RadioSelect)
    phone = forms.CharField(max_length=254,widget=forms.TextInput(attrs={'class':'form-control'}))
    type_of_sickness = forms.ChoiceField(label="Sickness",widget=forms.Select(attrs={'class':'form-control'}), choices=field)

    class Meta:
        model = Profile    
        fields = ("gender","phone","type_of_sickness")

class LoginForm(AuthenticationForm):
    username = forms.CharField(label=("Username or Email"), max_length=30, 
                               widget=forms.TextInput(attrs={'class': 'loginput'}))

class DoctorsForm(UserCreationForm):
    
    email = forms.EmailField(label="Email", max_length=254,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter a correct email'}))
    username = forms.CharField(max_length=254,widget=forms.TextInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(max_length=254,widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=254,widget=forms.TextInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(label="Password",widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label="Confirm password",widget=forms.PasswordInput(attrs={'class':'form-control'}))
    

    
    def __init__(self, *args, **kwargs):
        super(DoctorsForm, self).__init__(*args, **kwargs)
        self.fields['email'].required = True
        #self.fields.pop('username')
        #self.fields.pop('password2')

    def save(self, commit=True):
        user = super(DoctorsForm, self).save(commit=False)
        if commit:
            user.save()
        return user
    def clean_email(self):
        # Get the email
        email = self.cleaned_data.get('email')
    
        # Check to see if any users already exist with this email as a username.
        try:
            match = User.objects.get(email=email)
        except User.DoesNotExist:
            # Unable to find a user, this is fine
            return email

        # A user was found with this as a username, raise an error.
        raise forms.ValidationError('This Email address is already in use.')
    
    def clean_username(self):
        # Get the email
        username = self.cleaned_data.get('username')
    
        wrong = '@'
        if wrong in username:
            raise forms.ValidationError('Username contains invalid characters')
        else:
            return username

    class Meta:
        model = User
        fields = ('username', 'first_name','last_name','email', 'password1', 'password2',)



class Practitioner_Form(forms.ModelForm):
    radio_choice = [
        ('Male', 'Male'),
        ('Female', 'Female')
    ]
    field = (
        ('Anatomy',' Anatomy'),
        ('2','Biochemistry'),
        ('3',' Dentistry and Dental Surgery'),
        ('4','Human Anatomy'),
        ('5',' Human Nutrion and Dietetics'),
        ('6','Medical Laboraty Science'),
        ('7',' Medicine and Surgery'),
        ('8','Nursing/Nursing Science'),
         ('5',' Human Nutrion and Dietetics'),
        ('6','Optometry'),
        ('7',' Pharmacology and Therapeutic'),
        ('8','Pharmacy'),
         ('9',' Physiology'),
        ('10','Physiotherapy'),
        ('11',' Radiography')

    )
    gender = forms.ChoiceField(choices=radio_choice, widget=forms.RadioSelect)
    medical_practitioner = forms.ChoiceField(label="Select your field",widget=forms.Select(attrs={'class':'form-control'}), choices=field)

    class Meta:
        model = Profile    
        fields = ("gender","phone","medical_practitioner")