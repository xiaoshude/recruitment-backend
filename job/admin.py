from django.contrib import admin

from .models import Job


class JobAdmin(admin.ModelAdmin):
    change_form_template = 'job/admin/change_form.html'


admin.site.register(Job, JobAdmin)
