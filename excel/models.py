import datetime

from django.db import models
from django.utils import timezone

class Inner_Excel(models.Model):
    inner_excel = models.FileField(upload_to='inner_files/', null = True)
    upload_date = models.DateTimeField(auto_now_add=True)

class Outter_Excel(models.Model):
    outter_excel = models.FileField(upload_to='outter_files/', null = True)
    upload_date = models.DateTimeField(auto_now_add=True)

class Final_Excel(models.Model):
    name = 'my final excel'
    final_excel = models.FileField(upload_to='final_files/', null = True)