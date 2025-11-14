from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('project/<slug:slug>/', views.project_detail, name='project_detail'),
    path('blog/<slug:slug>/', views.blog_detail, name='blog_detail'),
]