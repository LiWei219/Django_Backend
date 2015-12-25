from rest_framework.views import APIView
from rest_framework.response import Response
import redis
import json
from rest_framework.parsers import JSONParser
# Create your views here.
from django.http import HttpResponse
class RealtimeApplicationThroughput(APIView):
	parser_classes = (JSONParser,)
	def get(self, request, format=None):
		callback = request.GET.get('callback','logIt')	
		#print callback
		data = []
		#r = redis.Redis(host='166.111.143.200', port=6379, db=0)
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
		D = '%s(%s)'%(callback, json.dumps(data))
		#D = '%s(%s)'%(callback, '{"username":"jack","age":21,"gender":"male"}')
		#print D
		#return Response(data)
		#return HttpResponse(D, content_type="application/json;charset=utf-8")
		return HttpResponse(D, content_type="application/json")

class RealtimeApplicationThroughput_Throuput_Second(APIView):
        parser_classes = (JSONParser,)
        def get(self, request, format=None):
                callback = request.GET.get('callback','logIt')
                data = []
                r = redis.Redis(host='2001:da8:a0:500::1:7', port=6379, db=0)
                line = r.get('throuput_second')
                array = line.split('/')

                for i in range(1,len(array)):
                        body = {}
                        body['throuput'] = array[i]
                        data.append(body)
                        #print data
                D = '%s(%s)'%(callback, json.dumps(data))
                return HttpResponse(D, content_type="application/json")

class RealtimeApplicationThroughput_Throuput_Minute(APIView):
        parser_classes = (JSONParser,)
        def get(self, request, format=None):
                callback = request.GET.get('callback','logIt')
                data = []
                r = redis.Redis(host='2001:da8:a0:500::1:7', port=6379, db=0)
                line = r.get('throuput_minute')
                array = line.split('/')

                for i in range(1,len(array)):
                        body = {}
                        body['throuput'] = array[i]
                        data.append(body)
                        #print data
                D = '%s(%s)'%(callback, json.dumps(data))
                return HttpResponse(D, content_type="application/json")

class RealtimeApplicationThroughput_CountPacket_Second(APIView):
        parser_classes = (JSONParser,)
        def get(self, request, format=None):
                callback = request.GET.get('callback','logIt')
                data = []
                r = redis.Redis(host='2001:da8:a0:500::1:7', port=6379, db=0)
                line = r.get('countPacket_second')
                array = line.split('/')

                for i in range(1,len(array)):
                        body = {}
                        body['countPacket'] = array[i]
                        data.append(body)
                        #print data
                D = '%s(%s)'%(callback, json.dumps(data))
                return HttpResponse(D, content_type="application/json")

class RealtimeApplicationThroughput_CountPacket_Minute(APIView):
        parser_classes = (JSONParser,)
        def get(self, request, format=None):
                callback = request.GET.get('callback','logIt')
                data = []
                r = redis.Redis(host='2001:da8:a0:500::1:7', port=6379, db=0)
                line = r.get('countPacket_minute')
                array = line.split('/')

                for i in range(1,len(array)):
                        body = {}
                        body['countPacket'] = array[i]
                        data.append(body)
                        #print data
                D = '%s(%s)'%(callback, json.dumps(data))
                return HttpResponse(D, content_type="application/json")

class RealtimeApplicationThroughput_Minute(APIView):
        parser_classes = (JSONParser,)
        def get(self, request, format=None):
                callback = request.GET.get('callback','logIt')
                data = []
                r = redis.Redis(host='2001:da8:a0:500::1:7', port=6379, db=0)
                line1 = r.get('countPacket_minute')
                line2 = r.get('throuput_minute')
                array1 = line1.split('/')
                array2 = line2.split('/')
                for i in range(1,len(array1)):
                        body = {}
                        body['countPacket'] = array1[i]
                        body['throuput'] = array2[i]
                        data.append(body)
                        #print data
                D = '%s(%s)'%(callback, json.dumps(data))
                return HttpResponse(D, content_type="application/json")

class RealtimeApplicationThroughput_Second(APIView):
        parser_classes = (JSONParser,)
        def get(self, request, format=None):
                callback = request.GET.get('callback','logIt')
                data = []
                r = redis.Redis(host='2001:da8:a0:500::1:7', port=6379, db=0)
                line1 = r.get('countPacket_second')
                line2 = r.get('throuput_second')
                array1 = line1.split('/')
                array2 = line2.split('/')
                for i in range(1,len(array1)):
                        body = {}
                        body['countPacket'] = array1[i]
                        body['throuput'] = array2[i]
                        data.append(body)
                        #print data
                D = '%s(%s)'%(callback, json.dumps(data))
                return HttpResponse(D, content_type="application/json")

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
