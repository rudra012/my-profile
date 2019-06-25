from django.contrib import admin

from .models import Project, Technology, ProjectImage

admin.site.register(Project)
admin.site.register(ProjectImage)
admin.site.register(Technology)
