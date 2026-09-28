from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from main.models import Experience, Education, Project
from main.forms import EducationForm, ProjectForm

import datetime


def show_main(request):
    last_login = request.COOKIES.get('last_login', 'Belum ada sesi login / Cookie tidak ditemukan')
    context = {
        "name": "Matthew Raeann Alexandra",
        "npm": "2506544763",
        "study_program": "S1 Ilmu Komputer",
        "bio": (
            "CS student at Universitas Indonesia."
        ),
        "last_login" : last_login,
    }
    return render(request, "index.html", context)


def show_experience(request):
    context = {
        "name": "Matthew Raeann Alexandra",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)


def show_educations(request):
    json_response = get_educations_json(request)

    educations = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    educations = [education.object for education in educations]
    institution_query = request.GET.get("institution", "").strip()

    context = {
        "name": "Matthew Raeann Alexandra",
        "education_list": educations,
        "institution_query": institution_query,
    }
    return render(request, "education.html", context)

def create_education(request):
    form = EducationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Riwayat pendidikan baru berhasil ditambahkan!")
        return redirect("main:show_educations")

    context = {
        "name": "Matthew Raeann Alexandra",
        "form": form,
    }
    return render(request, "education_form.html", context)

def update_education(request, education_id):
    education = get_object_or_404(Education, pk=education_id)

    if request.method == "POST":
        form = EducationForm(request.POST, instance=education)
        if form.is_valid():
            form.save()
            messages.success(request, 'Riwayat edukasi berasil diperbaharui!')
            return redirect("main:show_educations")
        
    elif request.method == "GET":
        form = EducationForm(instance=education)

    context = {
        'name': "Matthew Raeann Alexandra",
        'form': form, 
        'education': education
    }
    return render(request, "education_form.html", context)

def get_educations_json(request):
    institution_query = request.GET.get("institution", "").strip()
    educations = Education.objects.all().order_by('-start_year')

    if institution_query:
        educations = educations.filter(institution__icontains=institution_query)

    educations_json = serializers.serialize("json", educations)
    return HttpResponse(educations_json, content_type="application/json")

def delete_education(request, education_id):
    education = get_object_or_404(Education, pk=education_id)

    if request.method == "POST":
        education.delete()
        messages.success(request, "Education berhasil dihapus!")
        return redirect("main:show_educations")

    return redirect("main:show_educations")

def show_projects(request):
    json_response = get_projects_json(request)

    projects = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    projects = [project.object for project in projects]
    title_query = request.GET.get("title", "").strip()

    context = {
        "name": "Matthew Raeann Alexandra",
        "project_list": projects,
        "title_query": title_query,
    }
    return render(request, "project.html", context)

@login_required(login_url="/login/")
def create_project(request):
    if not request.user.is_superuser:
        raise PermissionDenied
    
    form = ProjectForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Proyek baru berhasil ditambahkan!")
        return redirect("main:show_projects")

    context = {
        "name": "Matthew Raeann Alexandra",
        "form": form,
    }
    return render(request, "projects_form.html", context)

def get_projects_json(request):
    title_query = request.GET.get("title", "").strip()
    projects = Project.objects.all()

    if title_query:
        projects = projects.filter(title__icontains=title_query)

    projects_json = serializers.serialize("json", projects, use_natural_foreign_keys=True)
    return HttpResponse(projects_json, content_type="application/json")

@login_required(login_url="/login/")
def delete_project(request, project_id):
    if not request.user.is_superuser:
        raise PermissionDenied
        
    project = get_object_or_404(Project, pk=project_id)

    if request.method == "POST":
        project.delete()
        messages.success(request, "Project berhasil dihapus!")
        return redirect("main:show_projects")

    return redirect("main:show_projects")

def register(request):
    form = UserCreationForm(request.POST or None)

    if (request.method == "POST" and form.is_valid()):
        form.save()
        messages.success(request, "Akun berhasil dibuat. Silahkan login.")
        return redirect("main:login")

    context = {
        "name": "Matthew Raeann Alexandra",
        "form": form,
    }
    return render(request, "register.html", context)

def login_user(request):
    form = AuthenticationForm(request, data=request.POST or None)

    if (request.method == "POST" and form.is_valid()):
        user = form.get_user()
        login(request, user)
        response = redirect('main:show_main')
        response.set_cookie('last_login', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return response

    context = {
        "name": "Matthew Raeann Alexandra",
        "form": form,
    }
    return render(request, "login.html", context)

def logout_user(request):
    logout(request)
    response = redirect('main:show_main')
    response.delete_cookie('last_login')
    return response

@login_required(login_url="/login/")
def toggle_star(request, project_id):
    project = get_object_or_404(Project, pk=project_id)

    if (request.method == "POST"):
        if (request.user in project.starred_by.all()):
            project.starred_by.remove(request.user)
        else:
            project.starred_by.add(request.user)

    return redirect('main:show_projects')