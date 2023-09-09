from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.http import HttpRequest
from django.views import View
from django.contrib.auth.forms import UserCreationForm
from .models import *
from .forms import *
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate, mixins, get_user_model
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages


# Create your views here.

class home(View):
    def get(self, request: HttpRequest):
        return render(request, template_name='home.html')


# class loginPage(View):
#     def get(self,request: HttpRequest):
#         form = UserCreationForm()
#         context = {'form':form}
#         return render(request, template_name='loginPage.html')


class registerPage(CreateView):
    model = get_user_model()
    form_class = registerForm
    template_name = 'registerPage.html'
    success_url = reverse_lazy("thinkify:homeNext")

    # context_object_name = 'registerForm'

    def form_valid(self, form):
        username = self.request.POST.get("username")
        password = self.request.POST.get("password")
        print(username,password)
        user = form.save(commit=True)
        # user = authenticate(username=form.cleaned_data['username'],password=form.cleaned_data['password'])
        if user is None:
            self.form_invalid(form)
        login(request=self.request, user=user)
        return redirect(to=self.success_url)


class homeNext(View, mixins.LoginRequiredMixin):
    def get(self, request: HttpRequest):
        return render(request, template_name='homeNext.html')


class LoginPage(LoginView):
    template_name = 'loginPage.html'
    authentication_form = UserLogin
    success_url = reverse_lazy("thinkify:homeNext")
    redirect_authenticated_user = True
    # username = self.request.POST.get("username")
    # password = self.request.POST.get("password")
    # print(username, password)


    def get_default_redirect_url(self):

        return self.success_url

class Logout(LogoutView):
    next_page = reverse_lazy("thinkify:Home")

class Agri_Modernisation(View, mixins.LoginRequiredMixin):
    def get(self, request: HttpRequest):
        return render(request, template_name='Agri_Modernisation.html')

class Agri_Resources(View, mixins.LoginRequiredMixin):
    def get(self, request: HttpRequest):
        return render(request, template_name='Agri_Resources.html')

class AI_Drones(View, mixins.LoginRequiredMixin):
    def get(self, request: HttpRequest):
        return render(request, template_name='AI_Drones.html')

class contact(View, mixins.LoginRequiredMixin):
    def get(self, request: HttpRequest):
        return render(request, template_name='contact.html')

class Estimate(View, mixins.LoginRequiredMixin):
    def get(self, request: HttpRequest):
        return render(request, template_name='Estimate.html')

class Legal(View, mixins.LoginRequiredMixin):
    def get(self, request: HttpRequest):
        return render(request, template_name='Legal.html')

class Malware(View, mixins.LoginRequiredMixin):
    def get(self, request: HttpRequest):
        return render(request, template_name='Malware.html')

class Robotics(View, mixins.LoginRequiredMixin):
    def get(self, request: HttpRequest):
        return render(request, template_name='Robotics.html')

class Rural(View, mixins.LoginRequiredMixin):
    def get(self, request: HttpRequest):
        return render(request, template_name='Rural.html')

class Tweet (View, mixins.LoginRequiredMixin):
    def get(self, request: HttpRequest):
        return render(request, template_name='Robotics.html')

class Web_Design(View, mixins.LoginRequiredMixin):
    def get(self, request: HttpRequest):
        return render(request, template_name='Web_Design.html')

class regis_form(View, mixins.LoginRequiredMixin):
    def get(self, request: HttpRequest):
        return render(request, template_name='regis_form.html')
