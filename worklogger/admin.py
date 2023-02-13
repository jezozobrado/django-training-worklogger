from django.contrib import admin
from .models import Log
from django.db.models.aggregates import Sum
from . import models
from django.db.models import F


@admin.register(models.Project)
class ProjectAdmin(admin.ModelAdmin):

    list_display = ['project_name', 'total_hours']

    def total_hours(self, instance):
        summary = Log.objects.values(Project=F('project__project_name')).annotate(
            hours=Sum('hours')).get(project__project_name=instance.project_name)
        return summary['hours']


admin.site.register(Log)
