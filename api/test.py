from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Point

class ClosestPointsAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse('closest_points')

    def test_closest_points_api(self):
        data = {
            'points': '2,2;-1,30;20,11;4,5'
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(len(response.data['coordinates']), 2)

        # Check if the points are stored in the database
        stored_points = Point.objects.all()
        self.assertEqual(stored_points.count(), 2)
        self.assertEqual(stored_points[0].coordinates, '2,2')
        self.assertEqual(stored_points[1].coordinates, '4,5')
