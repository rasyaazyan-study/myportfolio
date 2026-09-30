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
from django.db.models import F

from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.http import Http404

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
        "experience_list": Experience.objects.order_by(F("ended_at").desc(nulls_first=True), "-started_at"),
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

@login_required
@permission_required('main.view_experience', raise_exception=True)
def get_experiences_json(request):
    title_query = request.GET.get("title", "").strip()
    experiences = Experience.objects.prefetch_related("starred_by").all()

    if title_query:
        experiences = experiences.filter(title__icontains=title_query)

    data = []
    for exp in experiences:
        starred_users = list(exp.starred_by.all())
        starred_ids = {u.pk for u in starred_users}
        
        if exp.thumbnail:
            thumbnail = exp.thumbnail.url
        elif exp.thumbnail_url:
            thumbnail = exp.thumbnail_url
        else:
            thumbnail = None

        data.append({
            "pk": str(exp.id),
            "fields": {
                "title": exp.title,
                "organization": exp.organization,
                "description": exp.description,
                "category": exp.category,
                "category_display": exp.get_category_display(),
                "thumbnail": thumbnail,
                "started_at": exp.started_at.isoformat(),
                "ended_at": exp.ended_at.isoformat() if exp.ended_at else None,
                "is_ongoing": exp.is_ongoing,
                "star_count": len(starred_users),
                "is_starred": request.user.is_authenticated and request.user.pk in starred_ids,
                "starred_by_names": ", ".join(u.username for u in starred_users),
            },
        })

    return JsonResponse(data, safe=False)

@login_required(login_url="/login/")
@require_POST
def toggle_star_experience(request, id):
    experience = get_object_or_404(Experience, pk=id)

    if experience.starred_by.filter(pk=request.user.pk).exists():
        experience.starred_by.remove(request.user)
        messages.success(request, f"Star dihapus dari \"{experience.title}\".")
    else:
        experience.starred_by.add(request.user)
        messages.success(request, f"Star diberikan untuk \"{experience.title}\"!")

    return redirect("main:show_experience")

#=== Education ===

def show_education(request):
    context = {
        "name": "Rasya Azyan Kautsar",
        "education_form": EducationForm(),
        "institution_query": request.GET.get("institution", "").strip(),
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
    
def get_educations_json(request):
    institution_query = request.GET.get("institution", "").strip()
    educations = Education.objects.order_by(F("ended_at").desc(nulls_first=True), "-started_at")

    if institution_query:
        educations = educations.filter(institution__icontains=institution_query)

    data = []
    for edu in educations:
        if edu.thumbnail:
            thumbnail = edu.thumbnail.url
        elif edu.thumbnail_url:
            thumbnail = edu.thumbnail_url
        else:
            thumbnail = None

        data.append({
            "pk": str(edu.id),
            "fields": {
                "institution": edu.institution,
                "description": edu.description,
                "category": edu.category,
                "category_display": edu.get_category_display(),
                "thumbnail": thumbnail,
                "started_at": edu.started_at.isoformat(),
                "ended_at": edu.ended_at.isoformat() if edu.ended_at else None,
                "is_ongoing": edu.is_ongoing,
            },
        })

    return JsonResponse(data, safe=False)

@require_POST
def create_education_ajax(request):
    if not request.user.is_superuser:
        return JsonResponse(
            {"message": "Hanya pemilik portofolio yang dapat menambahkan pendidikan."},
            status=403,
        )

    form = EducationForm(request.POST, request.FILES)
    if form.is_valid():
        education = form.save()
        return JsonResponse(
            {"message": "Pendidikan berhasil ditambahkan.", "pk": str(education.pk)},
            status=201,
        )

    return JsonResponse({"errors": form.errors.get_json_data()}, status=400)
    
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

    data = [
        {
            "pk": str(contact.id),
            "fields": {
                "name": contact.name,
                "category": contact.category,
                "category_display": contact.get_category_display(),
                "value": contact.value,
                "url": contact.url,
            },
        }
        for contact in contacts
    ]

    return JsonResponse(data, safe=False)

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

@login_required
@permission_required('main.view_message', raise_exception=True) 
def get_messages_json(request):
    messages_qs = Message.objects.prefetch_related("starred_by").all()

    data = []
    for message in messages_qs:
        starred_users = list(message.starred_by.all())
        starred_ids = {u.pk for u in starred_users}

        data.append({
            "pk": str(message.id),
            "fields": {
                "created_at": message.created_at.isoformat(),
                "sender": message.sender,
                "to": message.to,
                "value": message.value,
                "star_count": len(starred_users),
                "is_starred": request.user.is_authenticated and request.user.pk in starred_ids,
                "starred_by_names": ", ".join(u.username for u in starred_users),
            },
        })

    return JsonResponse(data, safe=False)

@login_required(login_url="/login/")
@require_POST
def toggle_star_message(request, id):
    message = get_object_or_404(Message, pk=id)

    if message.starred_by.filter(pk=request.user.pk).exists():
        message.starred_by.remove(request.user)
        messages.success(request, f"Star dihapus dari pesan.")
    else:
        message.starred_by.add(request.user)
        messages.success(request, f"Star diberikan untuk pesan.")

    return redirect("main:show_message")

#=== Project===
def show_project(request):
    context = {
        "name": "Rasya Azyan Kautsar",
        "project_list": Project.objects.all(),
        "design_list": Design.objects.all(),
        "project_form": ProjectForm(),
        "design_form": DesignForm(),
        "create_url_name": "main:create_project",
    }
    return render(request, "project.html", context)

@login_required(login_url="/login/")
@permission_required('main.add_project', raise_exception=True)
def create_project(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Proyek baru berhasil ditambahkan!")
            return redirect("main:show_project")
        messages.error(request, "Proyek baru gagal ditambahkan!")
    else:
        form = ProjectForm()

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

@login_required
@permission_required('main.view_project', raise_exception=True) 
def get_projects_json(request):
    title_query = request.GET.get("title", "").strip()
    projects = Project.objects.prefetch_related("starred_by").all()

    if title_query:
        projects = projects.filter(title__icontains=title_query)

    data = []
    for project in projects:
        starred_users = list(project.starred_by.all())
        is_starred = (request.user in starred_users if request.user.is_authenticated else False)

        data.append({
            "pk": str(project.id),
            "fields": {
                "title": project.title,
                "role": project.role,
                "role_display": project.get_role_display(),
                "description": project.description,
                "tech_stack": project.tech_stack,
                "project_url": project.project_url,
                "project_image_url": project.project_image_url,
                "star_count": len(starred_users),
                "is_starred": is_starred,
                "starred_by_names": ", ".join(u.username for u in starred_users),
            },
        })

    return JsonResponse(data, safe=False)

@login_required(login_url="/login/")
@require_POST
def toggle_star_project(request, id):
    project = get_object_or_404(Project, pk=id)

    if project.starred_by.filter(pk=request.user.pk).exists():
        project.starred_by.remove(request.user)
        messages.success(request, f"Star dihapus dari \"{project.title}\".")
    else:
        project.starred_by.add(request.user)
        messages.success(request, f"Star diberikan untuk \"{project.title}\".")

    return redirect("main:show_project")

@login_required(login_url="/login/")
@permission_required('main.add_design', raise_exception=True)
def create_design(request):
    if request.method == "POST":
        form = DesignForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Design baru berhasil ditambahkan!")
            return redirect("main:show_project")
        messages.error(request, "Design baru gagal ditambahkan!")
    else:
        form = DesignForm()

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

@login_required
@permission_required('main.view_design', raise_exception=True) 
def get_designs_json(request):
    title_query = request.GET.get("title", "").strip()
    designs = Design.objects.prefetch_related("starred_by").all()

    if title_query:
        designs = designs.filter(title__icontains=title_query)

    data = []
    for design in designs:
        starred_users = list(design.starred_by.all())
        starred_ids = {u.pk for u in starred_users}

        data.append({
            "pk": str(design.id),
            "fields": {
                "title": design.title,
                "tools": design.tools,
                "category": design.category,
                "category_display": design.get_category_display(),
                "project_url": design.project_url,
                "project_image_url": design.project_image_url,
                "star_count": len(starred_users),
                "is_starred": request.user.pk in starred_ids,
                "starred_by_names": ", ".join(u.username for u in starred_users),
            },
        })

    return JsonResponse(data, safe=False)

@login_required(login_url="/login/")
@require_POST
def toggle_star_design(request, id):
    design = get_object_or_404(Design, pk=id)

    if design.starred_by.filter(pk=request.user.pk).exists():
        design.starred_by.remove(request.user)
        messages.success(request, f"Star dihapus dari \"{design.title}\".")
    else:
        design.starred_by.add(request.user)
        messages.success(request, f"Star siberikan untuk \"{design.title}\".")

    return redirect("main:show_project")

#=== Star ===
STAR_TARGETS = {
    "experience": (Experience, "main:show_experience"),
    "message":    (Message,    "main:show_message"),
    "project":    (Project,    "main:show_project"),
    "design":     (Design,     "main:show_project"),
}

@login_required(login_url="/login/")
@require_POST
def toggle_star(request, kind, id):
    if kind not in STAR_TARGETS:
        raise Http404
    model, redirect_name = STAR_TARGETS[kind]
    obj = get_object_or_404(model, pk=id)

    if obj.starred_by.filter(pk=request.user.pk).exists():
        obj.starred_by.remove(request.user)
    else:
        obj.starred_by.add(request.user)

    return redirect(redirect_name)