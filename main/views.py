from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

from main.models import Experience
from main.models import Education
from main.forms import ExperienceForm
from main.forms import EducationForm

from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

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

def create_experience(request):
    form = ExperienceForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Pengalaman Organisasi baru berhasil ditambahkan!")
        return redirect("main:show_experience")

    context = {
        "name": "Rasya",
        "form": form,
    }
    return render(request, "experience_form.html", context)

def create_education(request):
    form = EducationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Riwayat Pendidikan baru berhasil ditambahkan!")
        return redirect("main:show_education")

    context = {
        "name": "Rasya",
        "form": form,
    }
    return render(request, "education_form.html", context)