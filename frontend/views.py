from django.shortcuts import render, get_object_or_404
from .models import Project, Skill, Hobby, Blog, About, SiteSettings

def home(request):
    projects = Project.objects.all()
    skills = Skill.objects.all()
    hobbies = Hobby.objects.all()
    blogs = Blog.objects.all()
    about = About.objects.first()
    site_settings = SiteSettings.load()
    context = {
        'projects': projects,
        'skills': skills,
        'hobbies': hobbies,
        'blogs': blogs,
        'about': about,
        'site_settings': site_settings,
    }
    return render(request, 'home.html', context)

def project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug)
    site_settings = SiteSettings.load()
    context = {
        'project': project,
        'site_settings': site_settings,
    }
    return render(request, 'project_detail.html', context)

def blog_detail(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    site_settings = SiteSettings.load()
    context = {
        'blog': blog,
        'site_settings': site_settings,
    }
    return render(request, 'blog_detail.html', context)
