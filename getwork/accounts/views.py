from django.shortcuts import render, redirect
from .forms import UserLoginForm, UserRegisterForm
from django.contrib.auth import authenticate, get_user_model, login, logout


# Create your views here.
def login_view(request):
    next = request.GET.get('next')
    if 'username' in request.session:
        return redirect('/')
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request,user)
        request.session['username'] = username
        if next:
            return redirect(next)
        return redirect('/')
    context = {
        'form': form,
    }
    return render(request, "login.html", context)

def register_view(request):
    next = request.GET.get('next')
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get("password")
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        request.session['username'] = user.username
        if next:
            return redirect(next)
        return redirect('/')
    context = {
        'form': form,
    }
    return render(request, "signup.html", context)

def logout_view(request):
    if 'username' in request.session:
        del request.session['username']
    logout(request)
    return redirect('/')