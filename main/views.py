# Create your views here.
from django.shortcuts import render

from main.models import Experience, Education, Contact, Message, Project, Design

from main.forms import ExperienceForm, EducationForm, ContactForm, MessageForm, ProjectForm, DesignForm

from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import redirect, render

from django.contrib.auth.decorators import login_required, permission_required

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
@permission_required('main.add_experience', raise_exception=True)
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

@login_required(login_url="/login/")
@permission_required('main.change_experience', raise_exception=True)
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

@login_required(login_url="/login/")
@permission_required('main.delete_experience', raise_exception=True)
def delete_experience(request, id):
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

@login_required
@permission_required('main.view_experience', raise_exception=True)
def get_experiences_json(request):    
    title_query = request.GET.get("title", "").strip()
    experiences = Experience.objects.all()

    if title_query:
        experiences = experiences.filter(title__icontains=title_query)

    experiences_json = serializers.serialize("json", experiences)
    return HttpResponse(experiences_json, content_type="application/json")

#=== Education ===

def show_education(request):
    context = {
        "name": "Rasya Azyan Kautsar",
        "education_list": Education.objects.all(),
        "create_url_name": "main:create_education",
    }
    return render(request, "education.html", context)

@login_required(login_url="/login/")
@permission_required('main.add_education', raise_exception=True)
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

@login_required(login_url="/login/")
@permission_required('main.change_education', raise_exception=True)
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

@login_required(login_url="/login/")
@permission_required('main.delete_education', raise_exception=True)
def delete_education(request, id):
    education = get_object_or_404(Education, pk=id)
    
    if request.method == "POST":
        education.delete()
        messages.success(request, "Riwayat Pendidikan telah terhapus!")
    
    return redirect("main:show_education")
    
@login_required
@permission_required('main.view_education', raise_exception=True)
def get_educations_json(request):    
    category_query = request.GET.get("category", "").strip()
    educations = Education.objects.all()

    if category_query:
        educations = educations.filter(category__icontains=category_query)

    educations_json = serializers.serialize("json", educations)
    return HttpResponse(educations_json, content_type="application/json")
    
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
@permission_required('main.add_contact', raise_exception=True)   
def create_contact(request):
    form = ContactForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Kontak baru berhasil ditambahkan!")
        return redirect("main:show_contact")

    context = {"name": "Rasya Azyan Kautsar", "form": form}
    return render(request, "contact_form.html", context)

@login_required(login_url="/login/")
@permission_required('main.change_contact', raise_exception=True)   
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

@login_required(login_url="/login/")
@permission_required('main.delete_contact', raise_exception=True)  
def delete_contact(request, id):
    contact = get_object_or_404(Contact, pk=id)

    if request.method == "POST":
        contact.delete()
        messages.success(request, "Kontak telah terhapus!")

    return redirect("main:show_contact")

@login_required
@permission_required('main.view_contact', raise_exception=True)  
def get_contacts_json(request):
    contacts = Contact.objects.all()
    contacts_json = serializers.serialize("json", contacts)
    return HttpResponse(contacts_json, content_type="application/json")

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

@login_required
@permission_required('main.view_message', raise_exception=True) 
def get_messages_json(request):
    messages_qs = Message.objects.all()
    messages_json = serializers.serialize("json", messages_qs)
    return HttpResponse(messages_json, content_type="application/json")

#=== Project===
def show_project(request):
    context = {
        "name": "Rasya Azyan Kautsar",
        "project_list": Project.objects.all(),
        "design_list": Design.objects.all(),
        "create_url_name": "main:create_project",
    }
    return render(request, "project.html", context)

@login_required(login_url="/login/") 
@permission_required('main.add_project', raise_exception=True)  
def create_project(request):
    form = ProjectForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Proyek baru berhasil ditambahkan!")
        return redirect("main:show_project")

    context = {
        "name": "Rasya Azyan Kautsar",
        "form": form,
        "item_type": "project",
        "page_title": "Add New Project",
    }
    return render(request, "portfolio_form.html", context)

@login_required(login_url="/login/")
@permission_required('main.change_project', raise_exception=True) 
def edit_project(request, id):
    project = get_object_or_404(Project, pk=id)
    form = ProjectForm(request.POST or None, instance=project)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Project berhasil diperbarui!")
        return redirect("main:show_project")

    context = {
        "name": "Rasya Azyan Kautsar",
        "form": form,
    }
    return render(request, "portfolio_form.html", context)

@login_required(login_url="/login/")
@permission_required('main.delete_project', raise_exception=True) 
def delete_project(request, id):
    project = get_object_or_404(Project, pk=id)
    
    if request.method == "POST":
        project.delete()
        messages.success(request, "Project telah terhapus!")
    
    return redirect("main:show_project")
    
@login_required(login_url="/login/")
def toggle_star_project(request, id):
    project = get_object_or_404(Project, pk=id)

    if request.method == "POST":
        if request.user in project.starred_by.all():
            project.starred_by.remove(request.user)
        else:
            project.starred_by.add(request.user)

    return redirect("main:show_project")

@login_required
@permission_required('main.view_project', raise_exception=True) 
def get_projects_json(request):
    title_query = request.GET.get("title", "").strip()
    projects = Project.objects.all()

    if title_query:
        projects = projects.filter(title__icontains=title_query)

    projects_json = serializers.serialize("json", projects)
    return HttpResponse(projects_json, content_type="application/json")

@login_required(login_url="/login/")  
@permission_required('main.add_design', raise_exception=True) 
def create_design(request):
    form = DesignForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Design baru berhasil ditambahkan!")
        return redirect("main:show_project")

    context = {
        "name": "Rasya Azyan Kautsar",
        "form": form,
        "item_type": "design",
        "page_title": "Add New Design",
    }
    return render(request, "portfolio_form.html", context)

@login_required(login_url="/login/")
@permission_required('main.change_design', raise_exception=True) 
def edit_design(request, id):
    design = get_object_or_404(Design, pk=id)
    form = DesignForm(request.POST or None, instance=design)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Design berhasil diperbarui!")
        return redirect("main:show_project")

    context = {
        "name": "Rasya Azyan Kautsar",
        "form": form,
    }
    return render(request, "portfolio_form.html", context)

@login_required(login_url="/login/")
@permission_required('main.delete_design', raise_exception=True) 
def delete_design(request, id):
    design = get_object_or_404(Design, pk=id)
    
    if request.method == "POST":
        design.delete()
        messages.success(request, "Design telah terhapus!")
    
    return redirect("main:show_project")
    
@login_required(login_url="/login/")
def toggle_star_design(request, id):
    design = get_object_or_404(Design, pk=id)

    if request.method == "POST":
        if request.user in design.starred_by.all():
            design.starred_by.remove(request.user)
        else:
            design.starred_by.add(request.user)

    return redirect("main:show_project")

@login_required
@permission_required('main.view_design', raise_exception=True) 
def get_designs_json(request):
    title_query = request.GET.get("title", "").strip()
    designs = Design.objects.all()

    if title_query:
        designs = designs.filter(title__icontains=title_query)

    designs_json = serializers.serialize("json", designs)
    return HttpResponse(designs_json, content_type="application/json")