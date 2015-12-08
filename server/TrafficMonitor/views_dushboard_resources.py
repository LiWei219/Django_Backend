from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class RealtimeApplicationThroughput(APIView):
	def get(self, request, format=None):
		#
		#include method here
		#
		return Response({'Response':'RealtimeApplicationThroughput'})

class RealtimeApplicationDataPacket(APIView):
	def get(self, request, format=None):
		#
		#include method here
		#
		return Response({'Response':'RealtimeApplicationDataPacket'})

class RealtimeApplicationStream(APIView):
	def get(self, request, format=None):
		#
		#include method here
		#
		return Response({'Response':'RealtimeApplicationStream'})

class RealtimeSourceCountryThroughput(APIView):
	def get(self, request, format=None):
		#
		#include method here
		#
		return Response({'Response':'RealtimeSourceCountryThroughput'})

class RealtimeDestinationCountryThroughput(APIView):
	def get(self, request, format=None):
		#
		#include method here
		#
		return Response({'Response':'RealtimeDestinationCountryThroughput'})

class RealtimeApplicationStatisticsForm(APIView):
	def get(self, request, format=None):
		#
		#include method here
		#
		return Response({'Response':'RealtimeApplicationStatisticsForm'})

class RealtimeApplicationChart(APIView):
	def get(self, request, format=None):
		#
		#include method here
		#
		return Response({'Response':'RealtimeApplicationChart'})

class RealtimeSourceCountryChart(APIView):
	def get(self, request, format=None):
		#
		#include method here
		#
		return Response({'Response':'RealtimeSourceCountryChart'})

class RealtimeDestinationCountryChart(APIView):
	def get(self, request, format=None):
		#
		#include method here
		#
		return Response({'Response':'RealtimeDestinationCountryChart'})