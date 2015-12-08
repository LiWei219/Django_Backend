from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class JobManagement(APIView):
    def get(self, request, format=None):
        #
        #include method here
        #
        return Response({'Response':'JobManagement'})