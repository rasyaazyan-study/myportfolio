# Create your views here.
from django.shortcuts import render

from main.models import Experience
from main.models import Education
from main.models import Contact

from main.forms import ExperienceForm
from main.forms import EducationForm
from main.forms import ContactForm

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
        "create_url_name": "main:create_experience",
    }
    return render(request, "experience.html", context)

def create_experience(request):
    form = ExperienceForm(request.POST or None, request.FILES or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Pengalaman Organisasi baru berhasil ditambahkan!")
        return redirect("main:show_experience")

    context = {
        "name": "Rasya Azyan Kautsar",
        "form": form,
    }
    return render(request, "experience_form.html", context)

def edit_experience(request, id):
    experience = get_object_or_404(Experience, pk=id)
    form = ExperienceForm(request.POST or None, request.FILES or None, instance=experience)
    
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Pengalaman Organisasi berhasil diperbarui!")
        return redirect("main:show_experience")
    
    context = {
        "name": "Rasya Azyan Kautsar",
        "form": form,
    }
    return render(request, "experience_form.html", context)

def delete_experience(request, id):
    experience = get_object_or_404(Experience, pk=id)
    
    if request.method == "POST":
        experience.delete()
        messages.success(request, "Pengalaman Organisasi telah terhapus!")
        
    return redirect("main:show_experience")

def show_education(request):
    context = {
        "name": "Rasya Azyan Kautsar",
        "education_list": Education.objects.all(),
        "create_url_name": "main:create_education",
    }
    return render(request, "education.html", context)

def create_education(request):
    form = EducationForm(request.POST or None, request.FILES or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Riwayat Pendidikan baru berhasil ditambahkan!")
        return redirect("main:show_education")

    context = {
        "name": "Rasya Azyan Kautsar",
        "form": form,
    }
    return render(request, "education_form.html", context)

def edit_education(request, id):
    education = get_object_or_404(Education, pk=id)
    form = EducationForm(request.POST or None, request.FILES or None, instance=education)
    
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Riwayat Pendidikan berhasil diperbarui!")
        return redirect("main:show_education")
    
    context = {
        "name": "Rasya Azyan Kautsar",
        "form": form,
    }
    return render(request, "education_form.html", context)

def delete_education(request, id):
    education = get_object_or_404(Education, pk=id)
    
    if request.method == "POST":
        education.delete()
        messages.success(request, "Riwayat Pendidikan telah terhapus!")
        return redirect("main:show_education")
    
def show_contact(request):
    context = {
        "name": "Rasya Azyan Kautsar",
        "contact_list": Contact.objects.all(),
        "create_url_name": "main:create_contact",
    }
    return render(request, "contact.html", context)
    
def create_contact(request):
    form = ContactForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Kontak baru berhasil ditambahkan!")
        return redirect("main:show_contact")

    context = {"name": "Rasya Azyan Kautsar", "form": form}
    return render(request, "contact_form.html", context)

def edit_contact(request, id):
    contact = get_object_or_404(Contact, pk=id)
    form = ContactForm(request.POST or None, instance=contact)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Kontak berhasil diperbarui!")
        return redirect("main:show_contact")

    context = {
        "name": "Rasya Azyan Kautsar",
        "form": form,
    }
    return render(request, "contact_form.html", context)


def delete_contact(request, id):
    contact = get_object_or_404(Contact, pk=id)

    if request.method == "POST":
        contact.delete()
        messages.success(request, "Kontak telah terhapus!")

    return redirect("main:show_contact")