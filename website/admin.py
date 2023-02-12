from django.contrib import admin
from .models import * 
# Register your models here.

mymodels = [HomeSetting]
admin.site.register(mymodels)

class ProjectsAdmin(admin.ModelAdmin):
    list_display = ["solutionstandard",'name','ordering','status']
    list_filter = ['solutionstandard','status']
    search_fields=['name','ordering']

admin.site.register(Projects,ProjectsAdmin)

class ModulesAdmin(admin.ModelAdmin):
    list_display=["project",'name','ordering', 'status']
    list_filter=['status','project',]
    search_fields=['name','ordering']

admin.site.register(Modules,ModulesAdmin)

class ApplyJobAdmin(admin.ModelAdmin):
    list_display=["linked_jobs",'name','email','phone','resume','date']
    list_filter=['linked_jobs','date']
    search_fields=['name','email','phone','date']

admin.site.register(ApplyJob,ApplyJobAdmin)

#start

class ContactAdmin(admin.ModelAdmin):
    list_display=['name','phone','email','comments','date']
    list_filter=['date']
    search_fields=['name','email','phone']
admin.site.register(Contact,ContactAdmin)

class NewsAdmin(admin.ModelAdmin):
    list_display=['title','shortdesc','link','dateyear','month','photo','status','ordering']
    list_filter=['title','dateyear','status']
    search_fields=['title','shortdesc','link','dateyear','ordering']
admin.site.register(News,NewsAdmin)

class SubscribAdmin(admin.ModelAdmin):
    list_display=['email','date']
    list_filter=['date']
    search_fields=['email','date']
admin.site.register(Subscrib,SubscribAdmin)

class ClientAdmin(admin.ModelAdmin):
    list_display=['title','clientlogo','ordering','status']
    list_filter=['title','status']
    search_fields=['title','ordering']

admin.site.register(Client,ClientAdmin)

class UserAdmin(admin.ModelAdmin):
    list_display=['name','number','ordering','status']
    list_filter=['name','status']
    search_fields=['name','number','ordering']
    
admin.site.register(User,UserAdmin)

class FeaturesAdmin(admin.ModelAdmin):
    list_display=['name','shortdesc','icon','ordering','status']
    list_filter=['name','status']
    search_fields=['name','shortdesc','ordering']
admin.site.register(Features,FeaturesAdmin)

class SolutionStandardAdmin(admin.ModelAdmin):
    list_display=['name','ordering','status']
    list_filter=['name','status']
    search_fields=['name','ordering']
admin.site.register(SolutionStandard,SolutionStandardAdmin)

class JobsAdmin(admin.ModelAdmin):
    list_display=['jobname','shortdesc','ordering','status']
    list_filter=['jobname','status']
    search_fields=['jobname','shortdesc','ordering','status']
admin.site.register(Jobs,JobsAdmin)

class AboutAdmin(admin.ModelAdmin):
    list_display=['valuename','valuedesc','ordering','status']
    list_filter=['valuename','status']
    search_fields=['valuename','valuedesc','ordering','status']

admin.site.register(About,AboutAdmin)






