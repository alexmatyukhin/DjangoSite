from django.shortcuts import render
from django.http import Http404
# from jinja2 import Environment, select_autoescape, Template, PackageLoader
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse

import datetime

# def index(request):
#     tempt = get_template('index.jinja')
#     html = tempt.render()
#     return HttpResponse(html)

def index(request):
    tempt_name = "index.djt"
    cont = {}
    return render(request, tempt_name, context=cont, content_type="text/html")

