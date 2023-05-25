from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from CBVapp.models import Course
from CBVapp.serializers import CourseSerializer
from rest_framework import status
from django.http import Http404

from rest_framework import mixins, generics
from rest_framework.viewsets import ViewSet, ModelViewSet

from rest_framework_tracking.mixins import LoggingMixin

# Create your views here.


#WITHOUT MIXINS
''' 
#non pk based - list view - all list
class CourseListView(APIView):
    
     def get(self, request):
        courses=Course.objects.all()
        serializer=CourseSerializer(courses, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer=CourseSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        else:
            return Response(serializer.erorrs)
    
    
#pk based - detail view - single entry
class CourseDetailView(APIView):
    
    def get_course(self, pk):
        try:
            return Course.objects.get(pk=pk)
            
        except Course.DoesNotExist:
            raise Http404()
    
    def get(self, request, pk):
        course=self.get_course(pk)
        serializer=CourseSerializer(course)
        return Response(serializer.data)
    
    def delete(self, request, pk):
        # course=self.get_course(pk)
        # course.delete()
        self.get_course(pk).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def put(self, request, pk):
        course=self.get_course(pk)
        serializer=CourseSerializer(course, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
            
        else: 
            return Response(serializer.errors)
'''

#WITH MIXINS

'''
#non pk operations - list view - get and post
class CourseListView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    
    queryset=Course.objects.all()
    serializer_class=CourseSerializer
    
    def get(self, request):
        return self.list(request)
    
    def post(self, request):
        return self.create(request)

#pk based operations - detail view - get put d  elete    
class CourseDetailView(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin,generics.GenericAPIView):
    
    queryset=Course.objects.all()
    serializer_class=CourseSerializer
    
    def get(self, request, pk):
       return self.retrieve(request, pk)
    
    def put(self, request, pk):
       return self.update(request, pk)
   
    def delete(self, request, pk):
       return self.destroy(request, pk)
'''

#WITH GENERICS

'''
class CourseListView(generics.ListAPIView, generics.CreateAPIView):
    queryset=Course.objects.all()
    serializer_class=CourseSerializer
    
class CourseDetailView(generics.RetrieveAPIView, generics.UpdateAPIView, generics.DestroyAPIView):
    queryset=Course.objects.all()
    serializer_class=CourseSerializer
'''    

#WITH MULTIPLE GENERICS
'''
class CourseListView(generics.ListCreateAPIView):
    queryset=Course.objects.all()
    serializer_class=CourseSerializer 
    
class CourseDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Course.objects.all()
    serializer_class=CourseSerializer

'''

#WITH VIEWSET
'''
class CourseViewSet(ViewSet):
    
    def list(set, request):
        courses=Course.objects.all()
        serializer=CourseSerializer(courses, many=True)
        return Response(serializer.data)
    
    def create(set, request):
        serializer=CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    def retrieve(self, request, pk):
        try:
            course=Course.objects.get(pk=pk)
            
        except Course.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer=CourseSerializer(course)
        return Response(serializer.data)
    
    def get_course(self, pk):
        try:
            return Course.objects.get(pk=pk)
            
        except Course.DoesNotExist:
            raise Http404()
        
    def destroy(self, request, pk):
        self.get_course(pk).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def update(self, request, pk):
        course=self.get_course(pk)
        serializer=CourseSerializer(course, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
            
        else: 
            return Response(serializer.errors)
'''

#WITH MODEL VIEWSET
class CourseViewSet(ModelViewSet):
    queryset=Course.objects.all()
    serializer_class=CourseSerializer