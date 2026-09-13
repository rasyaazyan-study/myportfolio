from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

from main.models import Experience
from main.models import Education


def show_main(request):
    context = {
        "name": "Rasya Azyan Kautsar",
        "npm": "2506538981",
        "study_program": "S1 Sistem Informasi",
        "bio": (
            "IS Student @ Fasilkom UI "
            ""
        ),
    }
    return render(request, "index.html", context)


def show_experience(request):
    context = {
        "name": "Rasya Azyan Kautsar",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)

def show_education(request):
    context = {
        "name": "Rasya Azyan Kautsar",
        "education_list": Education.objects.all(),
    }
    return render(request, "education.html", context)