from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import UserProfile
from . import serializers
from rest_framework.authentication import TokenAuthentication
from . import permissions
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
    
class HelloViewset(viewsets.ViewSet):
    serializer_class = serializers.HelloSerializer
    """ Test API Viewsets """
    def list(self,request):
        """ return a hello message: this is like get method """
        a_viewset = ['usees actions (list,create,retrieve,update,patial_update and delte)',
                     'Automatically maps to urls using routers',
                     'Provides more functionality with less code']  
        return Response({'message':'Hello..!','a_viewset':a_viewset})

    def create(self,request):
        """ Create a heloo message using VIEWSETS """
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            desig = serializer.validated_data.get('desig')
            message = f"Hello {name}..!, and i am a {desig}"
            return Response({'message':message})  
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def retrieve(self, request, pk=None):
        """ retreving a particular object by ID """
        return Response({'http_method':'GET'})
    
    def update(self, request,pk = None):
        """ Hnadle update the value using PUT """
        return Response({'http_method':'PUT'})
    
    def partial_update(self, request,pk = None):
        """ Hnadle partial update the value using PATCH """
        return Response({'http_method':'PATCH'})
    
    def destroy(self, request,pk = None):
        """ delete the value using DELETE """
        return Response({'http_method':'DELETE'})
    

class UserProfilesViewset(viewsets.ModelViewSet):
    """ Handle creating and updating profiles """
    serializer_class = serializers.UserProfileSerializer
    queryset = UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.updateOwnProfile, )

    
    