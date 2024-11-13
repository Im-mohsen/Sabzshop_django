from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from django.contrib.auth import logout, login, authenticate
from django.http import HttpResponse
# Create your views here.


def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    # return redirect("social:profile")
                    return redirect("shop:products_list")
                else:
                    return HttpResponse("Your account is disabled.")
            else:
                return HttpResponse("Invalid login.")
    else:
        form = LoginForm()
    return render(request, "registration/login.html", {'form': form})


def log_out(request):
    logout(request)
    return render(request, 'registration/logged_out.html')
