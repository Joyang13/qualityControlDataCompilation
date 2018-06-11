from django.contrib import admin
from .models import Inner_Excel
from .models import Outter_Excel, Final_Excel

admin.site.register(Inner_Excel)
admin.site.register(Outter_Excel)
admin.site.register(Final_Excel)

# Register your models here.
