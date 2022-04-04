from django.test import TestCase
from base.models import Engagement, Task
from .engagement_tracker_factories import EngagementFactory, TaskFactory


class TestEngagementModel(TestCase):
    """
    Test class for engagement model
    """

    def test_create_engagement(self):
        """
        Test creating engagement model object
        """
        engagement = EngagementFactory.create()
        model_engagement = Engagement.objects.get(id=engagement.id)

        self.assertEqual(engagement.user, model_engagement.user)
        self.assertEqual(engagement.name, model_engagement.name)

    def test_engagement_string_representation(self):
        """
        Test string representation of Engagement object
        """
        engagement = EngagementFactory.create()
        self.assertEqual(str(engagement), engagement.name)


class TestTaskModel(TestCase):
    """
    Test class for task model
    """

    def test_create_task(self):
        """
        Test creating task model object
        """
        task = TaskFactory.create()
        model_task = Task.objects.get(id=task.id)

        self.assertEqual(task.user, model_task.user)
        self.assertEqual(task.engagement, model_task.engagement)
        self.assertEqual(task.title, model_task.title)
        self.assertEqual(task.description, model_task.description)
        self.assertEqual(task.complete, model_task.complete)
        self.assertEqual(task.created, model_task.created)

    def test_task_string_representation(self):
        """
        Test string representation of Task object
        """
        task = TaskFactory.create()
        self.assertEqual(str(task), task.title)
