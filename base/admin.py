from django.contrib import admin
from .models import Task
from .models import Engagement
# Register your models here.

admin.site.register(Engagement) #registers model with admin panel
admin.site.register(Task) #registers model with admin panel