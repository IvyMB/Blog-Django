import factory
from faker import Faker

from django.contrib.auth.models import User
from django.utils.timezone import now

from models.post import Post
from models.events import Events

faker = Faker()


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    email = factory.Faker('safe-email')
    username = factory.LazyAttribute(lambda x: faker.name())

    @classmethod
    def _prepare(cls, create, **kwargs):
        password = kwargs.pop("password", None)
        user = super(UserFactory, cls)._prepare(create, **kwargs)
        if password:
            user.set_password(password)
        if create:
            user.save()
        return user


class PostFactory(factory.django.DjangoModelFactory):
    title = factory.LazyAttribute(lambda x: faker.sentence())
    created_on = factory.LazyAttribute(lambda x: now())
    author = factory.SubFactory(UserFactory)
    status = 0

    class Meta:
        model = Post


class EventsFactory(factory.django.DjangoModelFactory):
    title = factory.LazyAttribute(lambda x: faker.sentence())
    date = factory.LazyAttribute(lambda x: faker.date_between(start_date='12-02-2023', end_date='12-02-2024'))
    created_on = factory.LazyAttribute(lambda x: now())
    description = factory.LazyAttribute(lambda x: faker.sentence())

    class Meta:
        model = Events
