from django.shortcuts import render

from django.views.generic import ListView, DetailView
from django.views.decorators.http import require_http_methods
from rest_framework import status, permissions
from .serializers import *
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import *

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def index(request):
    workLoc = request.query_params.get('workLoc', None)
    recruiting_category = request.query_params.get('recruiting_category', None)

    if workLoc and recruiting_category:
        job_data_raw = Job.objects.filter(work_loc_id=workLoc).filter(recruiting_category_id=recruiting_category).order_by('-created')
    elif workLoc:
        job_data_raw = Job.objects.filter(work_loc_id=workLoc).order_by('-created')
    elif recruiting_category:
        job_data_raw = Job.objects.filter(recruiting_category_id=recruiting_category).order_by('-created')
    else:
        job_data_raw = Job.objects.all().order_by('-created')

    workloc_data_raw = WorkLoc.objects.all()

    recruiting_category_data_raw = RecruitingCategory.objects.all()

    data = {}
    data['jobs'] = JobSerializer(job_data_raw, many=True).data
    data['workLoc'] = WorkLocSerializer(workloc_data_raw, many=True).data
    data['recruiting_category'] = RecruitingCategorySerializer(recruiting_category_data_raw, many=True).data

    return Response(data)


class IndexView(ListView):
    model = Job
    template_name = 'job/index.html'

