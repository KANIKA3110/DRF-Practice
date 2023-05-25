from django.contrib import admin
from django.urls import path
from NSapp.views import InstructorListView, CourseListView, CourseDetailView, InstructorDetailView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('instructors/', InstructorListView.as_view()),
    path('courses/', CourseListView.as_view()),
    path('courses/<int:pk>/', CourseDetailView.as_view(), name='course-detail'),
    path('instructors/<int:pk>/', InstructorDetailView.as_view(), name='instructor-detail'),
    path('auth/login/', obtain_auth_token, name='create-token'),
    
]