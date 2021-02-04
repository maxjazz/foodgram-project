from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import CreationForm
from django.contrib.auth.forms import PasswordChangeForm, PasswordResetForm
from django.contrib import messages


class SignUp(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy("login")
    template_name = "signup.html"


def ChangePassword(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,
                             'Your password was successfully updated!')
            return redirect('signup')
        else:
            messages.error(request,
                           'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request,
                  'changePassword.html',
                  {'form': form})


def PasswordResetView(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,
                             'Your password was successfully updated!')
            return redirect('signup')
        else:
            messages.error(request,
                           'Please correct the error below.')
    else:
        form = PasswordResetForm()
    return render(request,
                  'resetPassword.html',
                  {'form': form})
