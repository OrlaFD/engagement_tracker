import factory
from django.contrib.auth import get_user_model

from base.models import Engagement, Task


User = get_user_model()

class UserFactory(factory.django.DjangoModelFactory):
    """
    Factory for user
    """
    class Meta:
        model = User

    username = factory.Faker('user_name')
    email = factory.Faker('email')
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    password = factory.Faker('password')

class EngagementFactory(factory.django.DjangoModelFactory):
    """
    Factory For Engagement
    """
    class Meta:
        model = Engagement

    user = factory.SubFactory(UserFactory)
    name = factory.Faker('name')

class TaskFactory(factory.django.DjangoModelFactory):
    """
    Factory For Task
    """
    class Meta:
        model = Task

    user = factory.SubFactory(UserFactory)
    engagement = factory.SubFactory(EngagementFactory)
    title = factory.Faker('title')
    description = factory.Faker('description')
    complete = factory.Faker('complete')
    created = factory.Faker('created')
  