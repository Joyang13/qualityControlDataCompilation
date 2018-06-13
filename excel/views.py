import os
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, render, redirect
from django import forms 
from io import BytesIO as IO
from django.conf import settings
from django.core.files.storage import FileSystemStorage

from .models import Inner_Excel, Outter_Excel
from .forms import Inner_Form, Outter_Form
from .utils import combine
import pandas as pd
from numpy import NaN

def home(request):
    inner_files = Inner_Excel.objects.all()
    outter_files = Outter_Excel.objects.all()
    print(type(Outter_Excel.objects.all()))

    #this combine thing saves the final excel file in /QA/media/temp
    combine()
    #now we gotta load the temp/final onto the final/final

    return render(request, 'excel/home.html', { 'inner_files': inner_files, 'outter_files': outter_files })

def upload(request):
    if request.method == 'POST':
        form = Inner_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('inner')
    else:
        files = Inner_Excel.objects.all()
        form = Inner_Form()
    return render(request, 'excel/inner.html', {'inner_form': form, 'files': files})

def outter(request):
    if request.method == 'POST':
        form = Outter_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('outter')
    else:
        files = Outter_Excel.objects.all()
        form = Outter_Form()
    return render(request, 'excel/outter.html', {'outter_form': form, 'files': files})

def final(request):
    #changing path to final.xlsx
    cur = os.path.dirname(__file__)
    path_to_file = cur + '/../media/final_files/final.xlsx'
    if os.path.exists(path_to_file):
        with open(path_to_file, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(path_to_file)
            return(response)
    raise Http404
    # return render(request, 'excel/final.html')

