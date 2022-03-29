from asyncio.log import logger
from re import template
from django.shortcuts import redirect, render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy


from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin #restricts access from unauthenticated users 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from .models import Engagement, Task
import logging

class CustomLoginView(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('engagements')

class RegisterPage(FormView):
    template_name = 'base/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('engagements')

    def form_valid(self, form):
        user = form.save()
        if user is not None: #if user was successfully created, it will be logged in
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)
    
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('engagements') #if a user is authenticated, redirect them to engagement list
        return super(RegisterPage, self).get(*args, **kwargs)

class EngagementList(LoginRequiredMixin, ListView):
    model = Engagement
    context_object_name = 'engagements'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['engagements'] = context['engagements'].filter(user=self.request.user) 
        print("should get engagements")
        print(context['engagements'].filter(user=self.request.user))
        context['count'] = context['engagements'].count()
        

        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['engagements'] = context['engagements'].filter(
                name__icontains=search_input)

        context['search_input'] = search_input

        return context

    

class TaskList(LoginRequiredMixin, ListView):
    model = Task #looks for _task_list template
    context_object_name = 'tasks' 
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #ensures a user can only get their own data
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        # This will query the colection from the sql db, it will filter tasks based on the query param
        # the query parm is then used to filter to retrieve the tasks for each associated engagment.
        context['tasks'] = context['tasks'].filter(engagement = self.request.GET['engagementid'])

        context['count'] = context['tasks'].filter(complete=False).count()
        

        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['tasks'] = context['tasks'].filter(
                title__icontains=search_input)

        context['search_input'] = search_input

        return context
   


class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'base/task.html'

class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('tasks') 
    #redirects to list view page once form is submitted
    

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)
    #displays tasks that are created for specific users


class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('tasks')
  

class DeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')