from django.shortcuts import redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin #restricts access from unauthenticated users 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from .models import Engagement, Task

#Login View 
class CustomLoginView(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    #If user was successfully logged in, they are redircted to their engagements 
    def get_success_url(self):
        return reverse_lazy('engagements')

#Register View 
class RegisterPage(FormView):
    template_name = 'base/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('engagements')

    def form_valid(self, form):
        user = form.save()

        #If user was successfully created, it will be logged in
        if user is not None: 
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)
    
    def get(self, *args, **kwargs):

        #If a user is authenticated, redirect them to engagement list
        if self.request.user.is_authenticated:
            return redirect('engagements') 
        return super(RegisterPage, self).get(*args, **kwargs)

#List View for Engagement
class EngagementList(LoginRequiredMixin, ListView):
    model = Engagement
    context_object_name = 'engagements'

    #Retrieves data for specific users
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['engagements'] = context['engagements'].filter(user=self.request.user) 
        context['count'] = context['engagements'].count()

        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['engagements'] = context['engagements'].filter(
                name__icontains=search_input)

        context['search_input'] = search_input

        return context

#List View for Task
class TaskList(LoginRequiredMixin, ListView):
    model = Task #looks for task_list template
    context_object_name = 'tasks' 
    template_name = 'base/task_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        #ensures a user can only get their own data
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        context['count'] = context['tasks'].filter(complete=False).count()
        
        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['tasks'] = context['tasks'].filter(
                title__icontains=search_input)

        context['search_input'] = search_input

        return context

    def get_queryset(self):
       #Retrieves the tasks associated to an engagement based on the route parameter 'pkt' in urls.py for task list
        return Task.objects.filter(engagement_id=self.kwargs['pkt'])

#Details View for Task
class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'base/task.html'

#Create View for Task
class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['title', 'description', 'complete', 'engagement']
    success_url = reverse_lazy('engagements') 
    #Redirects to engagements page once form is submitted
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)
    #Displays tasks that are created for specific users

#Update View for Task
class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['title', 'description', 'complete']

    #After succesfull update, display task detail
    def get_success_url(self):
        return reverse_lazy('task-update', kwargs={'pk': self.kwargs['pk']})
  
#Delete View for Task
class DeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    success_url = reverse_lazy('engagements')
    #redirects back to engagement page after task successfully deleted
  
    