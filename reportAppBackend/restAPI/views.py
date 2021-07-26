from django.db.models.fields.files import FieldFile
from rest_framework.views import APIView
from rest_framework import status
import pandas as pd
from .models import Service, Category, Status, TableObject, ExportedFile
from .seriallizer import ServiceSerializer, CategorySerializer, StatusSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.http import Http404
from pathlib import Path
import os



# category API
@api_view(['GET', 'POST'])
def categories_list(request):
    if request.method == "GET":
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response({"categories":serializer.data})

    elif request.method == "POST":
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'PUT', 'DELETE'])
def category_detail(request, pk):
    try:
        current_category = Category.objects.get(pk=pk)
    except Category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CategorySerializer(current_category)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CategorySerializer(current_category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        current_category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# services API 
@api_view(['GET', 'POST'])
def services_list(request):
    if request.method == "GET":
        services = Service.objects.all()
        serializer = ServiceSerializer(services, many=True)
        return Response({"services":serializer.data})

    elif request.method == "POST":
        serializer = ServiceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def service_detail(request, pk):
    try:
        current_service = Service.objects.get(pk=pk)
    except Service.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ServiceSerializer(current_service)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ServiceSerializer(current_service, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        current_service.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# status API
@api_view(['GET', 'POST'])
def status_list(request):
    if request.method == "GET":
        statuses = Status.objects.all()
        serializer = StatusSerializer(statuses, many=True)
        return Response({"status":serializer.data})

    elif request.method == "POST":
        serializer = StatusSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def status_detail(request, pk):
    try:
        current_status = Status.objects.get(pk=pk)
    except Status.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = StatusSerializer(current_status)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = StatusSerializer(current_status, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        current_status.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
 
@api_view(['GET'])
def generateFile(request):
    categories_list = Category.objects.all()
    file_list = ExportedFile.objects.all()
    rows = []
    for cat in categories_list:
        for serv in cat.service.all():
            rows.append(TableObject(cat.name, serv.name, serv.status_name, serv.remark))
    data = {"№": ["Category", "Service", "Status", "Remark"]}
    for row in range(len(rows)):
        data.update({row:[rows[row].category_name, rows[row].service_name, rows[row].status_name, rows[row].remark]})
    
    df = pd.DataFrame.from_dict(data, orient="index")
    filename = "table.xlsx"
    df.to_excel("media/"+filename, index=False, header=True)
    BASE_DIR = Path(__file__).resolve().parent.parent
    my_file = BASE_DIR.joinpath("media/"+filename)
    # STATIC_ROOT = os.path.join(os.path.dirname(my_file))
    file = ExportedFile(file=my_file)
    file.save()
    return Response({"":len(file_list)})