from django.shortcuts import render
from .models import Job

# Create your views here.

def job_lists(request):
    job_list = Job.objects.all()
    print(job_list)
    context={'jobs' : job_list}
    return render( request , 'job/job_list.html' , context )

def job_detial(request , id):
    job_detail = Job.objects.get(id=id)
    context={'job' : job_detail}
    return render( request , 'job/job_details.html' , context )
