from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

def first(request):
    return HttpResponse('<h2>Hai there..!</h2>')

class HelloApiView(APIView):
    """ Test API view 'hello world' """
    def get(self,request,format=None):
        """ returns alist of APIView Features """
        an_apiview = [
            'uses HTTP methods as functions (get, post,patch, put, delete)',
            'Is similar to a traditional Django view',
            'Gives you the most control over your application logic',
            'is mapped manually to urls ',
        ]

        return Response({'message':'Hello !','an_apiview':an_apiview})