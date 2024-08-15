from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.urls import reverse_lazy
from .forms import SignUpForm, EditProfileForm

class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    #form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'
    
class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    #form_class = UserCreationForm
    success_url = reverse_lazy('home')
    template_name = 'registration/edit_profile.html'
    
    def get_object(self):
        return self.request.user
