import json

from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render

from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

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


def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('controlpanel'))
            else:
                return render(request, "backend/login.html", {"error": "Account deactivated!!"})
        else:
            return render(request, "backend/login.html", {"error": "Incorrect username or password!!"})
    else:
        return render(request, 'backend/login.html', {})


def controlpanel(request):
    return render(request, 'backend/controlpanel.html', {})


@csrf_exempt
def website(request):
    useful = User.objects.get(id=request.user.id).userprofile.sites.filter(website.url == request.POST.get("url")).first().useful
    
    return HttpResponse("success")