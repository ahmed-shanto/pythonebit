from django.shortcuts import render,redirect
from .models import *
from django.http import HttpResponse
from django.http import Http404
from django.contrib import messages
import random
from django.core.mail import send_mail,EmailMultiAlternatives,EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import FileSystemStorage

# Create your views here.

def home(request):
    projects=Projects.objects.filter(status = True).order_by("ordering") 
    module=Modules.objects.filter(status = True).order_by("ordering")
    homesetting=HomeSetting.objects.all()
    client=Client.objects.filter(status = True).order_by("ordering")
    user=User.objects.filter(status = True).order_by("ordering")
    features=Features.objects.filter(status = True).order_by("ordering")
    news=News.objects.filter(status = True).order_by("ordering")
    solutionstandard=SolutionStandard.objects.filter(status = True).order_by("ordering")
    if request.method== 'POST':
     email=request.POST.get('email')
     subscribe=Subscrib.objects.create(email=email)
     return HttpResponse()
            # sentmail=request.POST['email']
            # subject='Welcome from E-Bit'
            # message='Dear Sir, Thanks for showing interest on us'
            # from_email=settings.EMAIL_HOST_USER
            # recipient_list=[sentmail]
            # subscribe.save()

            # send_mail(subject,message,from_email,recipient_list,fail_silently=False)
    
            
    context = {
        'projects':projects, 
        'modules': module,
        'homesetting':homesetting,
        'client':client,
        'user':user,
        'features':features,
        'news':news,
        'solutionstandard':solutionstandard,

    }

    #  send_mail(
    #  'Hi',
    #  'This is Test Mail',
    #  'mesba9311@outlook.com',
    #  [Subscrib.email],
    #  fail_silently=False,
    #   )
   


    return render(request, 'website/index.html',context)
 
def about_us(request):
    homesetting=HomeSetting.objects.all()
    about=About.objects.filter(status = True).order_by("ordering") 
    projects=Projects.objects.filter(status = True).order_by("ordering") 
    module=Modules.objects.filter(status = True).order_by("ordering") 
    solutionstandard=SolutionStandard.objects.filter(status = True).order_by("ordering")
    context = {
        'projects':projects, 
        'modules': module,
        'homesetting':homesetting,
        'about':about,
        'solutionstandard':solutionstandard
        
    }
    return render(request, 'website/about-us.html',context )

def contact(request):
    projects=Projects.objects.filter(status = True).order_by("ordering") 
    module=Modules.objects.filter(status = True).order_by("ordering") 
    solutionstandard=SolutionStandard.objects.filter(status = True).order_by("ordering")
    context = {
        'projects':projects, 
        'podules': module,
        'solutionstandard':solutionstandard

        
    }
    if request.method == 'POST' :
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        comments = request.POST['comments']
       
        contact =Contact.objects.create(name = name, email=email,phone=phone,comments=comments)
      

   
    return render(request, 'website/contact.html',  context )

def projects(request):
    projects=SolutionStandard.objects.filter(status = True).order_by("ordering")
    module=Modules.objects.filter(status = True).order_by("ordering") 
    solutionstandard=SolutionStandard.objects.filter(status = True).order_by("ordering")
    context = {
        'project_list':projects, 
        'podules': module,
        'solutionstandard':solutionstandard
    }
    
    return render(request, 'website/projects.html', context)


def module(request,name):
    projects=Projects.objects.filter(status = True).order_by("ordering") 
    modules=Modules.objects.filter(status = True).order_by("ordering")
    solutionstandard=SolutionStandard.objects.filter(status = True).order_by("ordering")
    module= name.replace('-', ' ')

    description= Modules.objects.filter(name__icontains=module)


    all_modules=list(Modules.objects.all())
    recent_modules=random.sample(all_modules,4)
    
   
    context = {
        "name":module,
        "description":description,
        'projects':projects, 
        'modules': modules,
        'solutionstandard':solutionstandard,
        'recent_modules': recent_modules,
        'module':module
    }
    
    
    return  render (request, 'website/module_details.html',context)



def career(request):
    homesetting=HomeSetting.objects.all()
    projects=Projects.objects.filter(status = True).order_by("ordering") 
    module=Modules.objects.filter(status = True).order_by("ordering") 
    solutionstandard=SolutionStandard.objects.filter(status = True).order_by("ordering")
    
    jobs=Jobs.objects.filter(status = True).order_by("ordering")    

    context = {
        'projects':projects, 
        'podules': module,
        'homesetting':homesetting,
        'jobs':jobs,
        'solutionstandard':solutionstandard
        
        
    }

    return render(request, 'website/career.html',context)

def jobs(request,id): 
    projects=Projects.objects.filter(status = True).order_by("ordering") 
    module=Modules.objects.filter(status = True).order_by("ordering") 
    jobs=Jobs.objects.filter(id = id).first()
    solutionstandard=SolutionStandard.objects.filter(status = True).order_by("ordering")
    
    context = {
        'projects':projects, 
        'podules': module,
        'jobs':jobs,
        'solutionstandard':solutionstandard

        
    }
    if request.method == 'POST' :
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        resume2 = request.FILES['resume']
        applyjob=ApplyJob.objects.create(linked_jobs_id = id,name = name, email=email,phone=phone,resume=resume2)
        

            
        return redirect('success')

         

    return render(request, 'website/job.html',context)


def success(request):
    projects=Projects.objects.filter(status = True).order_by("ordering") 
    module=Modules.objects.filter(status = True).order_by("ordering") 
    solutionstandard=SolutionStandard.objects.filter(status = True).order_by("ordering")
    context = {
        'projects':projects, 
        'podules': module,
        'solutionstandard':solutionstandard      
    }

   
    return render(request, 'website/success.html',context)

def get_email(request):
       if request.method== 'POST':
        email=request.POST.get('email')
        subscribe=Subscrib.objects.create(email=email)
        return HttpResponse()
