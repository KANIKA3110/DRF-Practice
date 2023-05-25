#from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import generics
from NSapp.serializers import InstructorSerializer, CourseSerializer
from NSapp.models import Instructor, Course
from rest_framework.permissions import IsAuthenticated, IsAdminUser, BasePermission
from rest_framework.authentication import BasicAuthentication, TokenAuthentication
from rest_framework.authtoken.models import Token
# Create your views here.

#TO CREATE TOKEN IMMEDIATELY FOR EXISTING USER
'''
users=User.objects.all()
for user in users:
    token=Token.objects.get_or_create(user=user)
    print(token)
'''

class WriteByAdminOnlyPermission(BasePermission):
    def has_permission(self, request, view):
        print('inside hash permission: ', request.user)
        user=request.user
        
        if request.method=='GET':
            return True 
        
        if request.method=='POST' or request.method=='PUT' or request.method=='DELETE':
            if user.is_superuser:
                return True
            
            return False
    

class InstructorListView(generics.ListCreateAPIView):
    permission_classes=[IsAuthenticated]
    serializer_class=InstructorSerializer
    queryset=Instructor.objects.all()
    
class InstructorDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class=InstructorSerializer
    queryset=Instructor.objects.all()
    
#WITHOUT TOKEN AUTHENTICATION
'''    
class CourseListView(generics.ListCreateAPIView):
    #permission_classes=[IsAuthenticated] - for session authentication
    #or for basic authentication-
    authentication_classes=[BasicAuthentication]
    #permission_classes=[IsAuthenticated]
    #permission_classes=[WriteByAdminOnlyPermission]
    permission_classes=[IsAuthenticated,WriteByAdminOnlyPermission]
    serializer_class=CourseSerializer
    queryset=Course.objects.all()
'''    

# WITH TOKEN AUTHENTICATION    
class CourseListView(generics.ListCreateAPIView):
    #permission_classes=[IsAuthenticated] - for session authentication
    #or for basic authentication-
    authentication_classes=[TokenAuthentication]
    #permission_classes=[IsAuthenticated]
    #permission_classes=[WriteByAdminOnlyPermission]
    permission_classes=[IsAuthenticated,WriteByAdminOnlyPermission]
    serializer_class=CourseSerializer
    queryset=Course.objects.all()
    
class CourseDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class=CourseSerializer
    queryset=Course.objects.all()    
    
