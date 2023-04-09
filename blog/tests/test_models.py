from django.test import TestCase

from ..models.events import Events


class TestEvents(TestCase):
    def setUp(self):
        self.events = Events.objects.create(
            title='My first event',
            date='2023-03-23 12:00:00',
            description='Event my first event blog'
        )

    def test_model_creation(self):
        test_object = Events.objects.filter(title='My first event')
        self.assertEqual(test_object.date, '2023-03-23 12:00:00')
        self.assertNumQueries(test_object.description, 'Event my first event blog')

