from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

# from .models import Subject
from .models import Subject

# Create your views here.
def index(request):
    return render(request, "reg/index.html", {
        "Subject": Subject.objects.all()
})
