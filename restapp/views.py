from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from . import serializers
# Create your views here.

def first(request):
    return HttpResponse('<h2>Hai there..!</h2>')

class HelloApiView(APIView):
    """ Test API view 'hello world' """
    serializer_class = serializers.HelloSerializer

    def get(self,request,format=None):
        """ returns alist of APIView Features """
        an_apiview = [
            'uses HTTP methods as functions (get, post,patch, put, delete)',
            'Is similar to a traditional Django view',
            'Gives you the most control over your application logic',
            'is mapped manually to urls ',
        ]

        return Response({'message':'Hello !','an_apiview':an_apiview})
    
    def post(self,request):
        """ Create a hello message with our name """
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            desig = serializer.validated_data.get('desig')
            message = f"Hello {name}..!, and i am a {desig}"
            return Response({'message':message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def put(self,request,pk=None):
        """ Handling updating an object """
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            desig = serializer.validated_data.get('desig')
            message = f"Hello {name}..!, and i am a {desig}"
            return Response({'message':message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self,request,pk=None):
        """ updating a particular object entity """
        return Response({'method':'PATCH'})

    def delete(self,request,pk=None):
        """Deleting an object """
        return Response({'method':'DELETE'})