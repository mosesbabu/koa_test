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
