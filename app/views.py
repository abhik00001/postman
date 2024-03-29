from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view

from app.models import todo

from app.serializer import todoserializer

# Create your views here.

@api_view(['GET'])
def home(request):
    val = todo.objects.all()
    serialize_val = todoserializer(val , many = True)

    return Response({
        "message" : "data fetch Successfully",
        "data" : serialize_val.data
    })

@api_view(["GET"])
def singleget(request , id):
    val = todo.objects.get(id = id)
    serializedata = todoserializer(val)

    return Response({
        "message":f"{serializedata} get successfully",
        "data" : serializedata.data
    })

@api_view(['POST'])
def savethistodo(request):
    serlizedata = todoserializer(data = request.data)
    if serlizedata.is_valid():
        serlizedata.save()

    return Response({
        "message" : "Data saved Sucessfully",
        "data" : serlizedata.data
    })