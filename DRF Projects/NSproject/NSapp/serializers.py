from NSapp.models import Course, Instructor
from rest_framework import serializers

#NESTED SERIALIZER
#1ST WAY
'''
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model=Course
        fields='__all__'
        

class InstructorSerializer(serializers.ModelSerializer):
    courses=CourseSerializer(many=True, read_only=True)
    class Meta:
        model=Instructor
        fields='__all__'
'''

# 2ND WAY        
'''
class InstructorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Instructor
        fields='__all__'
        
class CourseSerializer(serializers.ModelSerializer):
    instructor=InstructorSerializer(read_only=True)
    class Meta:
        model=Course
        fields='__all__'
        
'''

class CourseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Course
        fields='__all__'
        

class InstructorSerializer(serializers.HyperlinkedModelSerializer):
    courses=serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='course-detail')
    class Meta:
        model=Instructor
        fields='__all__'