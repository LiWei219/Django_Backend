from rest_framework.views import APIView
from rest_framework.response import Response
import redis
# Create your views here.

class RealtimeApplicationThroughput(APIView):
	def get(self, request, format=None):
		
		data = []
		r = redis.Redis(host='2001:da8:a0:500::1:7', port=6379, db=0)
		line1 = r.get('throuput')
		line2 = r.get('countPacket')
		#line1 = '1/2/3/4/5/6/7/8/9/0'
		#line2 = '0/9/8/7/6/5/4/3/2/1'
		array1 = line1.split('/')
		array2 = line2.split('/')

		for i in range(1,len(array1)):
			body = {}
			body['throuput'] = array1[i]
			body['countPacket'] = array2[i]
			data.append(body)
			#print data
		return Response(data)

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
