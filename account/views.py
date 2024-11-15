from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from django.contrib.auth import logout, login, authenticate
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
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


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return render(request, 'registration/register_done.html', {'user': user})
    else:
        form = UserRegisterForm()
    return render(request, "registration/register.html", {'form': form})


@login_required
def edit_user(request):
    if request.method == "POST":
        user_form = UserEditForm(request.POST, instance=request.user, files=request.FILES)
        if user_form.is_valid():
            user_form.save()
            # return redirect('social:profile')
            return redirect('shop:products_list')
    else:
        user_form = UserEditForm(instance=request.user)
    context = {
        "user_form": user_form
    }
    return render(request, 'registration/edit_user.html', context)


@login_required
def password_change(request):
    if request.method == 'POST':
        form = CustomPasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            # messages.success(request, 'پسورد شما با موفقیت تغییر کرد.')
            return redirect('done/')  # به صفحه‌ای که می‌خواهید بعد از تغییر به آن بروید
    else:
        form = CustomPasswordChangeForm(user=request.user)

    return render(request, 'registration/password_change_form.html', {'form': form})


def password_change_done(request):
    return render(request, 'registration/password_change_done.html')
