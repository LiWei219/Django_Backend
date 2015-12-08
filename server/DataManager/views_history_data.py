from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class OfflineApplicationLayerResults(APIView):
    def get(self, request, format=None):
        #
        #include method here
        #
        return Response({'Response':'OfflineApplicationLayerResults'})

class OfflineTransportLayerResults(APIView):
    def get(self, request, format=None):
        #
        #include method here
        #
        return Response({'Response':'OfflineTransportLayerResults'})

class OfflineNetworkLayerResults(APIView):
    def get(self, request, format=None):
        #
        #include method here
        #
        return Response({'Response':'OfflineNetworkLayerResults'})