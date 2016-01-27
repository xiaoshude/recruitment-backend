__author__ = 'fjywan'

from rest_framework import serializers
from .models import *


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = (
        'job_title', 'job_category', 'recruiting_category', 'work_loc', 'requirement', 'duty', 'more_info', 'created')


class RecruitingCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = RecruitingCategory
        fields = ('id', 'category')


class WorkLocSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkLoc
        fields = ('id', 'category')