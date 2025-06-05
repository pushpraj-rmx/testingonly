from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Employee
from rest_framework.response import Response
# Create your views here.

@api_view(['GET', 'POST'])
def get_post(request):
    if request.method == 'GET':
        employees = Employee.objects.all().values()
        employees_list = list(employees)    
        return Response({"status":"OK","message":"Fetch data succesfully","data": employees_list})

    elif request.method == 'POST':
        data = request.data
        result = Employee(
            name=data.get('name'),
            email=data.get('email'),
            department=data.get('department'),
            salary=data.get('salary')
        ).save()

        return Response({"status":"OK","message": "Employee created", "data": data})


@api_view(['DELETE', 'PUT'])
def delete_put(request, emp_id):
    if request.method == 'DELETE':    
        result = Employee.objects.filter(id=emp_id).delete()
        return Response({"status":"OK","message": "Employee Deleted successfully", "emp_id": emp_id})
    elif request.method == 'PUT':
        data = request.data
        result = Employee.objects.filter(id=emp_id).update(
            name=data.get('name'),
            email=data.get('email'),
            department=data.get('department'),
            salary=data.get('salary')
        )
        return Response({"status":"OK","message": "Employee Edited successfully", "data": data})



def index(request):
    return render(request,'index.html')



