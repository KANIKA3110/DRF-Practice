from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from app2.models import Course
from app2.serializers import CourseSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

@api_view(['GET','POST'])
def courseListView(request):
    if request.method=='GET':
        courses=Course.objects.all()
        serializer=CourseSerializer(courses, many=True)
        return Response(serializer.data)
    
    elif request.method=='POST':
        serializer=CourseSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        else:
            return Response(serializer.erorrs)
        
@api_view(['GET', 'PUT', 'DELETE'])
def courseDetailView(request,pk):
    try:
        course=Course.objects.get(pk=pk)
        
    except Course.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method=='DELETE':
        course.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    elif request.method=='GET':
        serializer=CourseSerializer(course)
        return Response(serializer.data)
    
    elif request.method=='PUT':
        serializer=CourseSerializer(course, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
            
        else: 
            return Response(serializer.errors)
    
   
        
    
