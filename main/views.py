# Create your views here.
from django.shortcuts import render

from main.models import Experience
from main.models import Education
from main.models import Contact
from main.models import Message

from main.forms import ExperienceForm
from main.forms import EducationForm
from main.forms import ContactForm
from main.forms import MessageForm

from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import redirect, render

from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied

import datetime

#=== Login & Register ===

def register(request):
    form = UserCreationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Akun berhasil dibuat. Silakan login.")
        return redirect("main:login")

    context = {
        "name": "Rasya Azyan Kautsar",
        "form": form,
    }
    return render(request, "register.html", context)

def login_user(request):
    form = AuthenticationForm(request, data=request.POST or None)

    if request.method == "POST" and form.is_valid():
        user = form.get_user()
        login(request, user)
        response = redirect("main:show_main")
        response.set_cookie('last_login', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return response

    context = {
        "name": "Rasya Azyan Kautsar",
        "form": form,
    }
    return render(request, "login.html", context)

def logout_user(request):
    logout(request)
    response = redirect("main:show_main")
    response.delete_cookie('last_login')
    return response

#=== Main ===

def show_main(request):
    last_login = request.COOKIES.get('last_login', 'Belum ada sesi login / Cookie tidak ditemukan')
    context = {
        "name": "Rasya Azyan Kautsar",
        "npm": "2506538981",
        "study_program": "S1 Sistem Informasi",
        "bio": (
            "IS Student @ Fasilkom UI "
            ""
        ),
        "last_login": last_login,
    }
    return render(request, "index.html", context)

#=== Organizational Experience ===

def show_experience(request):
    context = {
        "name": "Rasya Azyan Kautsar",
        "experience_list": Experience.objects.all(),
        "create_url_name": "main:create_experience",
    }
    return render(request, "experience.html", context)

@login_required(login_url="/login/")
def create_experience(request):
    if not request.user.is_superuser:
        raise PermissionDenied
    
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

@login_required(login_url="/login/")
def edit_experience(request, id):
    if not request.user.is_superuser:
        raise PermissionDenied
    
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

@login_required(login_url="/login/")
def delete_experience(request, id):
    if not request.user.is_superuser:
        raise PermissionDenied
    
    experience = get_object_or_404(Experience, pk=id)
    
    if request.method == "POST":
        experience.delete()
        messages.success(request, "Pengalaman Organisasi telah terhapus!")
        
    return redirect("main:show_experience")

@login_required(login_url="/login/")
def toggle_star_experience(request, id):
    experience = get_object_or_404(Experience, pk=id)

    if request.method == "POST":
        if request.user in experience.starred_by.all():
            experience.starred_by.remove(request.user)
        else:
            experience.starred_by.add(request.user)

    return redirect("main:show_experience")

#=== Education ===

def show_education(request):
    context = {
        "name": "Rasya Azyan Kautsar",
        "education_list": Education.objects.all(),
        "create_url_name": "main:create_education",
    }
    return render(request, "education.html", context)

@login_required(login_url="/login/")
def create_education(request):
    if not request.user.is_superuser:
        raise PermissionDenied
    
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

@login_required(login_url="/login/")
def edit_education(request, id):
    if not request.user.is_superuser:
        raise PermissionDenied
    
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

@login_required(login_url="/login/")
def delete_education(request, id):
    if not request.user.is_superuser:
        raise PermissionDenied
    
    education = get_object_or_404(Education, pk=id)
    
    if request.method == "POST":
        education.delete()
        messages.success(request, "Riwayat Pendidikan telah terhapus!")
        return redirect("main:show_education")
    
#=== Contact ===

@login_required(login_url="/login/")
def show_contact(request):
    context = {
        "name": "Rasya Azyan Kautsar",
        "contact_list": Contact.objects.all(),
        "create_url_name": "main:create_contact",
    }
    return render(request, "contact.html", context)

@login_required(login_url="/login/")    
def create_contact(request):
    if not request.user.is_superuser:
        raise PermissionDenied
    
    form = ContactForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Kontak baru berhasil ditambahkan!")
        return redirect("main:show_contact")

    context = {"name": "Rasya Azyan Kautsar", "form": form}
    return render(request, "contact_form.html", context)

@login_required(login_url="/login/")
def edit_contact(request, id):
    if not request.user.is_superuser:
        raise PermissionDenied
    
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

@login_required(login_url="/login/")
def delete_contact(request, id):
    if not request.user.is_superuser:
        raise PermissionDenied
    
    contact = get_object_or_404(Contact, pk=id)

    if request.method == "POST":
        contact.delete()
        messages.success(request, "Kontak telah terhapus!")

    return redirect("main:show_contact")

#=== Message ===

def show_message(request):
    form = MessageForm(request.POST or None)
    
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Pesan berhasil ditambahkan!")
        return redirect("main:show_message")
    
    context = {
        "name": "Rasya Azyan Kautsar",
        "form": form,
        "message_list": Message.objects.all(),
        "create_url_name": "main:create_message",
    }
    return render(request, "message.html", context)

@login_required(login_url="/login/")
def delete_message(request, id):
    message = get_object_or_404(Message, pk=id)

    if request.method == "POST":
        message.delete()
        messages.success(request, "Pesan telah terhapus!")

    return redirect("main:show_message")

@login_required(login_url="/login/")
def toggle_star_message(request, id):
    message = get_object_or_404(Message, pk=id)

    if request.method == "POST":
        if request.user in message.starred_by.all():
            message.starred_by.remove(request.user)
        else:
            message.starred_by.add(request.user)

    return redirect("main:show_message")