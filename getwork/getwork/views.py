from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    context = {
        "username": request.session.get('username', 'John Doe'),
    }
    return render(request, "home.html", context)