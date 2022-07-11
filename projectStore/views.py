from multiprocessing import context
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django .db .models import Q
from django.core.paginator import Paginator
from .forms import HireWriterForm
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView




def home(request):
    dept = Department.objects.all()
    context = {'dept': dept}
    return render(request, 'home.html', context)


def department(request):
    dept = Department.objects.all()
    context = {"dept": dept}
    return render(request, 'projectstore/department.html', context)

def category(request, depts):
    dept = Department.objects.all()
    category_project = Project.objects.filter(
        departments__name__contains=depts
    )
    context = {'depts': depts,
               'category_project':category_project,
               'dept': dept}
    return render(request, 'projectstore/courses.html', context)   



def projectList(request):
    dept = Department.objects.all()
    p = Paginator(Project.objects.all().order_by('?'), 2)
    page = request.GET.get('page') 
    list_of_project = p.get_page(page)
    context = {'list_of_project':list_of_project, 
               'dept': dept}
    return render(request, 'projectstore/list_of_all_project.html', context)




class ProjectDetail(DetailView):
    
    model = Project
    template_name = 'projectstore/project_detail.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    

def hirewriterform(request):
    
    dept = Department.objects.all()
    
    if request.method == 'POST':
        form = HireWriterForm(request.POST)
        if form.is_valid():
            full_name = form.cleaned_data['full_name']
            phone_number =form.cleaned_data['phone_number']
            email = form.cleaned_data['email']
            select_work_type = form.cleaned_data['select_work_type']
            clasification = form.cleaned_data['clasification']
            job_discribtion = form.cleaned_data['job_discribtion']
            
            
            form.save()
            return render(request, 'contactus/hire_success.html')
    form = HireWriterForm()
    context = {'form': form,
               'dept': dept}
    return render(request, 'projectstore/hirewriter.html', context)




def payment(request):
    dept = Department.objects.all()
    context = {'dept': dept}
    return render(request, 'projectstore/payment.html', context)


def about(request):
    dept = Department.objects.all()
    context = {'dept': dept}
    return render(request, 'projectstore/about.html', context)