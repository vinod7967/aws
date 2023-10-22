from django.shortcuts import render
# from django.rest_framework import Response
from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework.response import Response
from .models import *
from .serializers import BlogSerializer
import json
class CrudOperations(APIView):
    serializer_class = BlogSerializer
    def get(self,request,pk=None):
        obj_all = Blog.objects.all()
        serializer = BlogSerializer(obj_all,many=True)
        return Response(serializer.data)
    def post(self,request,pk=None):
        print(request.data)
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
        else:
            print(serializer.errors)
            return Response({"errors":serializer.errors})
        return Response({"msg":"record inserted successfully"})
class UpdateRecord(APIView):
    serializer_class = BlogSerializer
    def put(self,request,pk=None):
        record = Blog.objects.get(id=pk)
        serializer = self.serializer_class(record,data=request.data)
        if serializer.is_valid():
            serializer.save()
        else:
            return Response({'errors ':serializer.errors})
        return Response({"msg":"record updated successfully"})
        


# Create your views here.
