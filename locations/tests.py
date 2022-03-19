# from django.test import TestCase
# from django.contrib.auth import get_user_model

# from .models import Location

# class LocationTests(TestCase):

#     @classmethod
#     def setUpTestData(cls):
#         testuser1 = get_user_model().objects.create_user(username='testuser', password='pass')
#         testuser1.save()

#         test_location = Location.objects.create(name='rake', owner=testuser1,description='Better for collecting leaves than a shovel.')
#         test_location.save()

#     def test_locations_model(self):
#         location = Location.objects.get(id=1)
#         actual_owner = str(location.owner)
#         actual_name = str(location.name)
#         actual_description = str(location.description)
#         self.assertEqual(actual_owner,'testuser')
#         self.assertEqual(actual_name, 'rake')
#         self.assertEqual(actual_description,'Better for collecting leaves than a shovel.')
