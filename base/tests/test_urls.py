from django.test import SimpleTestCase
from django.urls import reverse, resolve
from base.views import CustomLoginView, EngagementList, RegisterPage, TaskList, TaskDetail, TaskCreate, TaskUpdate, DeleteView


class TestUrls(SimpleTestCase):
    """
    Test class for url patterns
    """

    def test_engagements_url_resolves(self):
        url = reverse('engagements')
        self.assertEquals(resolve(url).func.view_class, EngagementList)
    
    def test_tasks_url_resolves(self):
        url = reverse('tasks')
        self.assertEquals(resolve(url).func.view_class, TaskList)

    def test_task_url_resolves(self):
        url = reverse('task', args=['1'])
        self.assertEquals(resolve(url).func.view_class, TaskDetail)

    def test_taskcreate_url_resolves(self):
        url = reverse('task-create')
        self.assertEquals(resolve(url).func.view_class, TaskCreate)

    def test_taskupdate_url_resolves(self):
        url = reverse('task-update', args=['1'])
        self.assertEquals(resolve(url).func.view_class, TaskUpdate)

    def test_taskdelete_url_resolves(self):
        url = reverse('task-delete', args=['1'])
        self.assertEquals(resolve(url).func.view_class, DeleteView)
    
    def test_login_url_resolves(self):
        url = reverse('login')
        self.assertEquals(resolve(url).func.view_class, CustomLoginView)

    def test_register_url_resolves(self):
        url = reverse('register')
        self.assertEquals(resolve(url).func.view_class, RegisterPage)

        