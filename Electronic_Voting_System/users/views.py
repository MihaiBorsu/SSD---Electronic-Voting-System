from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views.generic import TemplateView, View
import  re

User = get_user_model()
from .forms import CustomUserCreationForm

from .firebase import auth, db

class LoginView(TemplateView, View):
    template_name = 'users/login.html'

    def get(self, request, *args, **kwargs):
        return self.render_to_response({})

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,
                           password=password)

        if user is not None:
           if user.is_active:
               login(request, user)
               messages.success(request, "You are now logged in!")
           else:
               messages.warning(request, "The password is valid, but the account has been disabled!")
        else:
            # the django authentication system was unable to verify the username and password, we try with firebase
            try:
                firebase_user = auth.sign_in_with_email_and_password(request.POST.get('username'), request.POST.get('password'))
                firebase_user = auth.refresh(firebase_user['refreshToken'])
                user = User.objects.create_user(
                    username=username,
                    email=username,
                    password=password
                )
                user.save()
                if user is not None:
                    if user.is_active:
                        login(request, user)
                        messages.success(request, "You are now logged in with firebase!")
                    else:
                        messages.warning(request, "The password is valid, but the account has been disabled!")
                else:
                    messages.warning(request, "There's been a problem with the authentication system!")
            except:
                messages.warning(request, "The username and password were incorrect.")

        return redirect(request.POST.get('next','home'))


class LogoutView(View):
    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            return redirect('home')

        logout(request)
        messages.success(request, "You are now logged out!")
        return redirect('home')


class RegisterView(TemplateView):
    template_name = 'users/register.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            messages.warning(request, "You are already logged in!")
            return redirect('home')
        return self.render_to_response({'form': CustomUserCreationForm()})

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password1')
        if re.match("[^@]+@[^@]+\.[^@]+",username):
            if str(password).__len__() >=6:
                form = CustomUserCreationForm(data=request.POST)
                try:
                    firebase_user = auth.create_user_with_email_and_password(email=username,
                                                                             password=password)
                    messages.success(request, "Your firebase user has been created sucessfully!")
                except:
                    messages.warning(request, "Firebase user couldn't be created!")
                if form.is_valid():
                    form.save()
                    messages.success(request, "You can now login!")
                    return redirect('home')
                else:
                    return self.render_to_response({'form': form})
            else:
                messages.warning(request, "password is too weak")
                return redirect(request.POST.get('next', 'register'))
        else:
            messages.warning(request, "Please insert a valid email adress")
            return redirect(request.POST.get('next', 'register'))



class MembersView(LoginRequiredMixin, TemplateView, View):
    template_name = 'users/members_only.html'

    def get(self, request, *args, **kwargs):
        return self.render_to_response({})
