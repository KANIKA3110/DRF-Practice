from rest_framework import serializers
from app2.models import Course

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model=Course
        fields='__all__'
