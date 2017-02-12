from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render

from django.shortcuts import render

# Create your views here.
from django.urls import reverse

from backend.forms import UserForm


def index(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)

        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True
        else:
            print(user_form.errors)
    else:
        user_form = UserForm()
    return render(request, "backend/index.html", {'user_form': user_form, 'registered' : registered})


def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                request.session["username"] = username
                request.session["password"] = password
                return HttpResponseRedirect(reverse('controlpanel'))
            else:
                return render(request, "backend/login.html", {"error": "Account deactivated!!"})
        else:
            return render(request, "backend/login.html", {"error": "Incorrect username or password!!"})
    else:
        return render(request, 'backend/login.html', {})


def controlpanel(request):
    return render(request, 'backend/controlpanel.html', {})