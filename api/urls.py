from django.urls import path
from .views import ClosestPointsAPIView

urlpatterns = [
    path('closest-points/', ClosestPointsAPIView.as_view(), name='closest_points'),
]
