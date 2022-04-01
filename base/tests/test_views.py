from django.test import TestCase, Client
from django.urls import reverse
from base.models import Engagement, Task, User


from base.views import EngagementList, TaskList

class TestViews(TestCase):

#using a setup pattern
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
        #self.assertTemplateUsed(response, 'base/engagement_list.html')

class TestTaskListView(TestCase):
    def setUp(self):
        self.view = TaskList

    def test_task_list_attrs(self):
        self.assertEqual(self.view.model, Task)
        self.assertEqual(self.view.context_object_name, 'tasks')
