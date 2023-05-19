from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Point
from .serializers import PointSerializer
from math import dist

class ClosestPointsAPIView(APIView):
    def post(self, request):
        input_points = request.data.get('points', '')
        input_points_list = input_points.split(';')
        points = []

        for point in input_points_list:
            coordinates = point.split(',')
            if len(coordinates) == 2:
                points.append((int(coordinates[0]), int(coordinates[1])))

        closest_points = self.find_closest_points(points)
        closest_points_coordinates = [
            f"{point[0]},{point[1]}" for point in closest_points
        ]

        # Save the received set of points and the closest points in the database
        point_serializer = PointSerializer(data={'coordinates': input_points_list})
        closest_points_serializer = PointSerializer(data={'coordinates': closest_points_coordinates})
        
        if point_serializer.is_valid() and closest_points_serializer.is_valid():
            point_serializer.save()
            closest_points_serializer.save()
            return Response(closest_points_coordinates, status=status.HTTP_201_CREATED)

        errors = {}
        if not point_serializer.is_valid():
           errors['input_points'] = point_serializer.errors
        if not closest_points_serializer.is_valid():
           errors['closest_points'] = closest_points_serializer.errors

        return Response({'errors': errors}, status=status.HTTP_400_BAD_REQUEST)
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
