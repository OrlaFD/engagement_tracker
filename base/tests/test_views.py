from django.test import TestCase, Client
from django.urls import reverse
from base.models import Engagement, Task, User
from base.views import CustomLoginView, EngagementList, RegisterPage, TaskCreate, TaskDetail, TaskList, TaskUpdate, DeleteView, UserCreationForm

class TestViews(TestCase):

# self.view is equal to an instantiated object of EngagementList view
    def setUp(self):
        self.view = EngagementList

#setting attributes and coding in custom stuff for the attributes
    def test_engagement_list_attrs(self):
        self.assertEqual(self.view.model, Engagement)
        self.assertEqual(self.view.context_object_name, 'engagements')
        
    def test_engagement_list_GET(self):
        client = Client()

        response = client.get(reverse('engagements'))

        self.assertEquals(response.status_code, 302)
        

class TestTaskListView(TestCase):
    def setUp(self):
        self.view = TaskList

    def test_task_list_attrs(self):
        self.assertEqual(self.view.model, Task)
        self.assertEqual(self.view.context_object_name, 'tasks')

    def test_task_list_GET(self):
        client = Client()

        response = client.get(reverse('tasks'))

        self.assertEquals(response.status_code, 302)
    

class TestTaskDetailView(TestCase):
    def setUp(self):
        self.view = TaskDetail

    def test_task_list_attrs(self):
        self.assertEqual(self.view.model, Task)
        self.assertEqual(self.view.context_object_name, 'task')
        self.assertEqual(self.view.template_name, 'base/task.html')

    def test_task_detail_GET(self):
        client = Client()

        response = client.get(reverse('task', args=['1']))

        self.assertEquals(response.status_code, 302)
    

class TestTaskCreateView(TestCase):
    def setUp(self):
        self.view = TaskCreate
        self.user = User.objects.create_user(username='john', password='123')

    def test_task_create_attrs(self):
        self.assertEqual(self.view.model, Task)
        self.assertEqual(self.view.fields, ['title', 'description', 'complete'])
        
    def test_task_create_GET(self):
        client = Client()

        response = client.get(reverse('task', args=['1']))

        self.assertEquals(response.status_code, 302)


class TestTaskUpdateView(TestCase):
    def setUp(self):
        self.view = TaskUpdate

    def test_task_update_attrs(self):
        self.assertEqual(self.view.model, Task)
        self.assertEqual(self.view.fields, ['title', 'description', 'complete'])
        
    def test_task_update_GET(self):
        client = Client()

        response = client.get(reverse('task', args=['1']))

        self.assertEquals(response.status_code, 302)


class TestDeleteView(TestCase):
    def setUp(self):
        self.view = DeleteView

    def test_task_delete_attrs(self):
        self.assertEqual(self.view.model, Task)
        self.assertEqual(self.view.context_object_name, 'task')
        
    def test_task_delete_GET(self):
        client = Client()

        response = client.get(reverse('task', args=['1']))

        self.assertEquals(response.status_code, 302)


class TestCustomLoginView(TestCase):
    def setUp(self):
        self.view = CustomLoginView

    def test_login_view_attrs(self):
        self.assertEqual(self.view.template_name, 'base/login.html')
        self.assertEqual(self.view.fields, '__all__')
        
    def test_login_view_GET(self):
        client = Client()

        response = client.get(reverse('login'))

        self.assertEquals(response.status_code, 200)


class TestRegisterPageView(TestCase):
    def setUp(self):
        self.view = RegisterPage

    def test_register_view_attrs(self):
        self.assertEqual(self.view.template_name, 'base/register.html')
        self.assertEqual(self.view.form_class, UserCreationForm)
        
    def test_register_view_GET(self):
        client = Client()

        response = client.get(reverse('register'))

        self.assertEquals(response.status_code, 200)
