from rest_framework import serializers
from CBVapp.models import Course

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model=Course
        fields='__all__'