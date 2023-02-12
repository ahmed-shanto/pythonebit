from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class SolutionStandard(models.Model):
    name        = models.CharField(max_length=50,blank=True,null=True)
    title       =RichTextField(blank=True,null=True)
    ordering    = models.IntegerField(default=1)
    status      = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Solution Standard"
        verbose_name_plural = "Solution Standard"

    def __str__(self) :
        return self.name
        


class Projects(models.Model):
    solutionstandard     = models.ForeignKey(SolutionStandard, on_delete=models.CASCADE, related_name='Projects')
    name        = models.CharField(max_length=50)
    ordering    = models.IntegerField(default=1)
    status      = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Solution Catagory"
        verbose_name_plural = "Solution Catagory"

    def __str__(self) :
        return self.name
        

class Modules(models.Model):
    project     = models.ForeignKey(Projects, on_delete=models.CASCADE, related_name='modules')
    name        = models.CharField(max_length=50)
    icon         = models.CharField(max_length=25, blank=True, null=True)
    photo       = models.ImageField(upload_to="static/modules/", blank=True, null=True)
    description = RichTextField()
    ordering    = models.IntegerField(default=1)
    status      = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Module"
        verbose_name_plural = "Modules"

    def __str__(self) :
        return self.name


class Contact(models.Model):
    name     = models.CharField(max_length=50)
    email    = models.EmailField(max_length=100)
    phone    = models.CharField(max_length=13)
    comments  =models.TextField(max_length=1000)
    date= models.DateTimeField(auto_now_add=True)

    def __str__(self) :
        return str('Message From '+ self.name)

class HomeSetting(models.Model):
    title1= models.CharField(max_length=100,blank=True, null=True)
    title2=models.CharField(max_length=100,blank=True, null=True) 
    shape=models.ImageField(upload_to="static/modules/",blank=True, null=True)
    banner=models.ImageField(upload_to="static/modules/",blank=True, null=True)
    # Clintnumber= models.CharField(max_length=10,blank=True, null=True)
    featuretitle=models.CharField(max_length=100,blank=True, null=True)
    storyaboutustitle=models.CharField(max_length=100,blank=True,null=True)
    storyaboutusitem1=models.CharField(max_length=100,blank=True,null=True)
    storyaboutusdesc1=models.TextField(max_length=1000,blank=True,null=True)
    storyaboutusitem2=models.CharField(max_length=50,blank=True,null=True)
    storyaboutusdesc2=models.TextField(max_length=1000,blank=True,null=True)
    storyaboutusbanner1=models.ImageField(upload_to="static/modules/",blank=True, null=True)
    storyaboutusbanner2=models.ImageField(upload_to="static/modules/",blank=True, null=True)
    singuptitle=models.CharField(max_length=100,blank=True,null=True)
    signupdesc=models.TextField(max_length=100,blank=True,null=True)
    chooseustitle=models.CharField(max_length=100,blank=True,null=True)
    chooseusdesc=models.TextField(max_length=1000,blank=True,null=True)
    sucessrate=models.IntegerField(null=True,blank=True )
    logo=models.ImageField(upload_to="static/modules/",blank=True, null=True)
    logodesc=models.TextField(max_length=500,blank=True,null=True)
    carrerbanner=models.ImageField(upload_to="static/modules/",blank=True, null=True)
    carrertitle=models.CharField(max_length=50,blank=True,null=True)
    carrerdesc=models.TextField(max_length=2000,blank=True,null=True)
    carrerjobtitle=models.CharField(max_length=50,blank=True,null=True)
    abouttitle =models.CharField(max_length=50,blank=True,null=True)
    aboutdesc=models.TextField(max_length=500,blank=True,null=True)
    aboutbanner=models.ImageField(upload_to="static/modules/",blank=True, null=True)
    aboutmission=models.TextField(max_length=1000,blank=True,null=True)
    aboutvision=models.TextField(max_length=1000,blank=True,null=True)

    
    status      = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Home_Setting"
        verbose_name_plural = "Home_Setting"

    def __str__(self) :
        return str('Home_Setting')

class Client(models.Model):
    clientlogo=models.ImageField(upload_to="static/modules/",blank=True, null=True)
    title=models.CharField(max_length=100,blank=True,null=True)
    ordering    = models.IntegerField(default=1)
    status      = models.BooleanField(default=True)
    

    class Meta:
        verbose_name = "Client"
        verbose_name_plural = "Client"

    def __str__(self) :
        return str(self.title)


class User(models.Model):
    name= models.CharField(max_length=100,blank=True, null=True)
    number=models.IntegerField(null=True,blank=True )
    ordering    = models.IntegerField(default=1)
    status      = models.BooleanField(default=True)

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "User"

    def __str__(self) :
        return self.name

class Features(models.Model):
    name=models.CharField(max_length=50,blank=True,null=True)
    shortdesc=models.TextField(max_length=500,blank=True,null=True)
    icon=models.CharField(max_length=50,blank=True,null=True)
    ordering    = models.IntegerField(default=1)
    status      = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Features"
        verbose_name_plural = "Features"

    def __str__(self):
        return str(self.name)

class News(models.Model):
    photo=models.ImageField(upload_to="static/modules/",blank=True, null=True)
    title=models.CharField(max_length=50,blank=True,null=True)
    shortdesc=models.TextField(max_length=500,blank=True,null=True)
    link=models.CharField(max_length=500,blank=True,null=True)
    dateyear=models.CharField(max_length=20,blank=True,null=True)
    month=models.CharField(max_length=20,blank=True,null=True)
    ordering    = models.IntegerField(default=1)
    status      = models.BooleanField(default=True)

    class Meta:
        verbose_name = "News"
        verbose_name_plural = "News"

    def __str__(self):
        return str(self.title)

class Subscrib(models.Model):
    email    = models.EmailField(max_length=100)
    date= models.DateTimeField(auto_now_add=True)

    def __str__(self) :
        return self.email

class About(models.Model):
    valuename=models.CharField(max_length=100,blank=True,null=True)
    valuedesc=models.TextField(max_length=1500,blank=True,null=True)
    ordering    = models.IntegerField(default=1)
    status      = models.BooleanField(default=True)


    class Meta:
        verbose_name = "About Value"
        verbose_name_plural = "About Value"

    def __str__(self):
        return self.valuename

class Jobs(models.Model):
    jobname=models.CharField(max_length=100,blank=True,null=True)
    shortdesc=models.TextField(max_length=500,blank=True,null=True)
    jobdesc=RichTextField()
    ordering    = models.IntegerField(default=1)
    status      = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Add Jobs"
        verbose_name_plural = "Add Jobs"

    def __str__(self):
        return str(self.jobname)

class ApplyJob(models.Model):
    linked_jobs     = models.ForeignKey(Jobs, on_delete=models.CASCADE, related_name='applyjob',blank=True,null=True)
    name     = models.CharField(max_length=50)
    email    = models.EmailField(max_length=100)
    phone    = models.CharField(max_length=13)
    resume   = models.FileField(upload_to="static/resumes/")
    date= models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Cantidate Details"
        verbose_name_plural = "Cantidate Details"

    def __str__(self) :
        return str('Resume Of '+ self.name)