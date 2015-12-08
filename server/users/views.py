from django.shortcuts import render
from django.http import StreamingHttpResponse
from users.models import User
from users.serializers import UserSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
from rest_framework.response import Response
import json


# Create your views here.

class JSONResponse(StreamingHttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


class User_list(APIView):
    def get(self, request, format=None):
        users = User.objects.all()
        ser = UserSerializer(users, many=True)
        return Response(ser.data)

    def post(self, request, format=None):
        ser = UserSerializer(request.DATA)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        return Response(ser.errors)
