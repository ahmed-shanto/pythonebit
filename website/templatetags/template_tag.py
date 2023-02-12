from django import template
from django.shortcuts import render, redirect
from django.db.models import Sum, Count, Q
from website import models

register = template.Library()

@register.filter(name='head_foots')
def head_foot(request):
    info  = models.HomeSetting.objects.filter(status = True).order_by("-id")
    return info

@register.filter(name='str2url')
def string_to_url_convert(data):
    #use in view: category = cat.replace('-', ' ')
    # use in html: text|str2url
    data = str(data)    
    return data.replace(' ', '-')