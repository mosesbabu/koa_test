from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status

class ClosestPointsAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_closest_points_api(self):
        input_points = '2,2;-1,30;20,11;4,5'
        expected_response = ['2,2', '4,5']

        response = self.client.post('/api/closest-points/', {'points': input_points}, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data, expected_response)
