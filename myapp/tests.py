from django.test import TestCase
from .models import Animal

class AnimalTestCase(TestCase):

    def setUp(self):
        Animal.objects.create(name="lion", sound="roar")
        Animal.objects.create(name="cat", sound="meow")

    def test_animals_can_speak(self):
        lion = Animal.objects.get(name="lion")
        cat = Animal.objects.get(name="cat")
        self.assertEqual(lion.speak(), 'The lion says "roar"')
        self.assertEqual(cat.speak(), 'The cat says "meow"')

    def test_animal_count(self):
        ct = Animal.objects.count()
        self.assertEqual(2, ct)

    def test_animal_count_after_deletion(self):
        Animal.objects.get(name="lion").delete()
        Animal.objects.get(name="cat").delete()
        ct = Animal.objects.count()
        self.assertEqual(0, ct)
