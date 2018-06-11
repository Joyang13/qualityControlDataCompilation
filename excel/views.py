from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, render, redirect
from django import forms 
from django.conf import settings
from django.core.files.storage import FileSystemStorage

from .models import Inner_Excel, Outter_Excel, Final_Excel
from .forms import Inner_Form, Outter_Form, Final_Form
from .utils import combine

def home(request):
    inner_files = Inner_Excel.objects.all()
    print(inner_files)
    outter_files = Outter_Excel.objects.all()
    print(outter_files)

    # print(Final_Excel.final_excel.url)
    combine()

    # Final_Excel.save()
    
    final_files = Final_Excel.objects.all()
    # print(final_files)
    return render(request, 'excel/home.html', { 'inner_files': inner_files, 'outter_files': outter_files, 'final_files': final_files, })

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
    print('hi')
    if request.method == 'POST':
        form = Outter_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('outter')
    else:
        files = Outter_Excel.objects.all()
        form = Outter_Form()
    return render(request, 'excel/outter.html', {'outter_form': form, 'files': files})