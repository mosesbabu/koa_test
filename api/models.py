from django.db import models

class Point(models.Model):
    points = models.CharField(max_length=255)

    def __str__(self):
        return self.points
class Meta:
        app_label = 'api'