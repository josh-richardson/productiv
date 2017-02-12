from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render

from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "backend/base.html", {})
