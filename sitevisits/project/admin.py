from django.contrib import admin
from .models import Project

class AdminProject(admin.ModelAdmin):
    model = Project
    list_display = ('title', 'visits', 'key', 'url')


admin.site.register(Project, AdminProject)
