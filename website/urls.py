from django.urls import path,include
from website import views
from django.conf.urls.static import static

urlpatterns=[
    path('', views.home, name='home'),
    path('about-us/', views.about_us, name='about_us'),
    path('projects/', views.projects, name='projects'),
    path('contact/', views.contact, name='contact'),
    path('module/<str:name>/', views.module, name='module'),
    path('career/', views.career, name='career'),
    path('jobs/<int:id>/', views.jobs, name='jobs'),
    path('success/', views.success, name='success'),
    path('get-email/', views.get_email, name='get_email'),

   
]