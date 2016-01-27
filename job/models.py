from django.db import models
from tinymce.models import HTMLField


class JobCategory(models.Model):
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.category


class RecruitingCategory(models.Model):
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.category


class WorkLoc(models.Model):
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.category


class Job(models.Model):
    job_title = models.CharField(max_length=100)
    job_category = models.ForeignKey(JobCategory, on_delete=models.CASCADE)
    recruiting_category = models.ForeignKey(RecruitingCategory, on_delete=models.CASCADE)
    recruiting_numbers = models.IntegerField()
    work_loc = models.ForeignKey(WorkLoc, on_delete=models.CASCADE)
    requirement = HTMLField()
    duty = HTMLField()
    more_info = HTMLField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.job_title







