from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, update_session_auth_hash
from .forms import *
from django.contrib.auth.decorators import login_required

def index(request):

  return render(request, 'app/index.html')




class SignUp_View(View):
    form_class = SignUpForm
    pform = ProfileForm
    initial = {'key': 'value'}
    template_name = 'app/signup.html'
    
    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        pform = self.pform(initial=self.initial)
        return render(request, self.template_name, {'form': form, 'pform':pform})
    

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        pform = self.pform(request.POST)
        form_valid = form.is_valid()
        pform_valid = pform.is_valid()
        if form_valid and pform_valid:
            user = form.save()
            request.session['username'] = request.POST['username']
            user.refresh_from_db()  # load the profile instance created by the signal
            user.is_active = True
            user.save()
            profile = pform.save(commit=False)
            profile.user = user
            profile.save()
            raw_password = form.cleaned_data.get('password1')
            login(request, user)
            
            return redirect('profile')
        return render(request, self.template_name, {'form': form, 'pform':pform})

@login_required
def profile_user(request):
    return render(request, 'app/profile.html')


@login_required
def medprofile(request):
    return render(request, 'app/medprofile.html')

class Practitioner_View(View):
    form_class = DoctorsForm
    pform = Practitioner_Form
    initial = {'key': 'value'}
    template_name = 'app/dsignup.html'
    
    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        pform = self.pform(initial=self.initial)
        return render(request, self.template_name, {'form': form, 'pform':pform})
    

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        pform = self.pform(request.POST)
        form_valid = form.is_valid()
        pform_valid = pform.is_valid()
        if form_valid and pform_valid:
            user = form.save()
            request.session['username'] = request.POST['username']
            user.refresh_from_db()  # load the profile instance created by the signal
            user.is_active = True
            user.save()
            profile = pform.save(commit=False)
            profile.user = user
            profile.is_staff = True
            profile.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('medprofile')
        return render(request, self.template_name, {'form': form, 'pform':pform})



def statistics(request):
    malaria = Profile.objects.filter(type_of_sickness = 'Malaria').count()
    typhoid = Profile.objects.filter(type_of_sickness = 'Typhoid').count()
    diarrhea = Profile.objects.filter(type_of_sickness = 'Diarrhea').count()
    headaches = Profile.objects.filter(type_of_sickness = 'Headaches').count()
    cholera = Profile.objects.filter(type_of_sickness = 'Cholera').count()
    ebola = Profile.objects.filter(type_of_sickness = 'Ebola').count()

    data = {
        'malaria':malaria,
        'typhoid':typhoid,
        'diarrhea':diarrhea,
        'headaches':headaches,
        'cholera':cholera,
        'ebola':ebola
    }
    
    
    return render(request, 'app/statistics.html', {'data':data})



def records(request):
    profile = Profile.objects.exclude(type_of_sickness = None)
    data = {
        'profile':profile
    }
    return render(request, 'app/records.html', data)

       


def filters (request):
    result = request.GET.get('filter')
    filter_ = Profile.objects.filter (type_of_sickness = result)

    data = {
        'filters':filter_
    }
    return render(request,'app/filter.html', data)