from django.db import models
from django.contrib.auth.models import User

#Engagement Model
class Engagement(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

#Task Model
class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    engagement = models.ForeignKey(Engagement, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['complete']
        #complete items are sent to bottom of list

#any time changes are made we need to run the python manage.py makemigrations....python manage.py migrate