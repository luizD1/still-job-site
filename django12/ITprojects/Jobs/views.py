from django.shortcuts import render,redirect
from django.http import HttpResponse
from Jobs.models import JobVacancy
from Jobs.forms import ApplicationForm

# Create your views here.
def index(request):
    return render (request=request,
                    template_name='job/index.html',)

def vacancy(request):
    vacs = JobVacancy.objects.all()
    return render (request=request,
                    template_name='job/vacancy.html',
                    context={'vac':vacs})
                    
                    
def about(request):
    return render (request=request,
                    template_name='job/about.html')

    
def submit(request):
    form = ApplicationForm()
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            # request succes(request)

    return render (request=request,
                    template_name='job/submit.html',
                    context={'form':form})


def succes(request):
    return render (request=request,
                    template_name='job/succes.html',)
