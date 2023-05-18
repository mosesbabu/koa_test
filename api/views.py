from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Point
from .serializers import PointSerializer

class ClosestPointsAPIView(APIView):
    def post(self, request):
        input_points = request.data.get('points_array', '')
        input_points_list = input_points.split(';')
        points_array = []

        for point in input_points_list:
            points = point.split(',')
            if len(points) == 2:
                points_array.append((int(points[0]), int(points[1])))

        closest_points = self.find_closest_points(points_array)
        closest_points_coordinates = [
            f"{point[0]},{point[1]}" for point in closest_points
        ]

        serializer = PointSerializer(data={'points_array': closest_points_coordinates}, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def find_closest_points(self, points):
        min_distance = float('inf')
        closest_points = []

        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                distance = self.calculate_distance(points[i], points[j])
                if distance < min_distance:
                    min_distance = distance
                    closest_points = [points[i], points[j]]

        return closest_points

    def calculate_distance(self, point1, point2):
        x1, y1 = point1
        x2, y2 = point2
        return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5