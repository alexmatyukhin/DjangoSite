from django.shortcuts import render
from django.http import Http404

from datetime import datetime
import locale

def mainpage(request):

    # Russian time format setting
    if locale.getlocale(locale.LC_TIME) != ('ru_RU', 'UTF-8'):
        locale.setlocale(locale.LC_ALL, "ru_RU.UTF-8")
        
    dt = datetime.now().strftime("%A, %d %B, %I:%M %p")
    tempt_name = "mainpage.jinja"
    cont = {'datetime': dt}
    return render (request, tempt_name, context=cont)
