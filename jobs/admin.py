from django.contrib import admin

from .models import JobMeta, JobDetail


admin.site.register(JobDetail)
admin.site.register(JobMeta)
