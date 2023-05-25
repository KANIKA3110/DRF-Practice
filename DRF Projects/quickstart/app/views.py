from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from . models import Employee
from . serializers import EmployeeSerializer, UserSerializer
#from django.contrib.auth.models import User
from app.models import User
from django.views.decorators.csrf import csrf_exempt
#from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

#@csrf_exempt
# Create your views here.
@api_view(['GET', 'POST'])
def employeeListView(request):
    if request.method=='GET':
        employees=Employee.objects.all()
        serializer=EmployeeSerializer(employees, many=True)
        #return JsonResponse({"message":"success"})
        #return JsonResponse(serializer.data, safe=False)
        return Response(serializer.data)
    
    elif request.method=='POST':
        #jsonData= JSONParser().parse(request)        
        #serializer=EmployeeSerializer(data=jsonData)
        serializer=EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            #return JsonResponse(serializer.data, safe=False)
            return Response(serializer.data)
        else:
            #return JsonResponse(serializer.errors, safe=False)
            return Response(serializer.errors)

@api_view(['GET', 'POST'])
def userListView(request):
    
    if request.method=='GET':
        users=User.objects.all()
        serializer=UserSerializer(users, many=True)
        #return JsonResponse(serializer.data, safe=False)
        return Response(serializer.data)
    
    elif request.method=='POST':

        #jsonData=JSONParser().parse(request)
        #serializer=UserSerializer(data=jsonData)
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            #return JsonResponse(serializer.data,safe=False)
            return Response(serializer.data)
        else:
            #return JsonResponse(serializer.errors, safe=False)        
            return Response(serializer.errors)        
        
        # both above were non pk based function based view

@api_view(['DELETE', 'PUT', 'GET'])
def employeeDetailView(request, pk):
    
    try:
        employee=Employee.objects.get(pk=pk)
        
    except Employee.DoesNotExist:
        #return HttpResponse(status=404)
        return Response(status=404)
    if request.method=='DELETE':
        employee.delete()
        #return HttpResponse(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    elif request.method=='GET':
        serializer=EmployeeSerializer(employee)
        #return JsonResponse(serializer.data, safe=False)
        return Response(serializer.data)
    
    elif request.method=='PUT':
        #jsonData=JSONParser().parse(request)
        #serializer=EmployeeSerializer(employee, data=jsonData)
        serializer=EmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            #return JsonResponse(serializer.data, safe=False)
            return Response(serializer.data)
        else:
            #return JsonResponse(serializer.errors, safe=False)
            return Response(serializer.errors)
