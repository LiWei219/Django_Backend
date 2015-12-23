from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse
import json
import httplib
# Create your views here.
class LogManagement(APIView):
    def post(self, request, format=None):
        #
        #include method here
        #
	c = {}
	storm_h_z=request.POST.get('type');
	master_slave=request.POST.get('type2');
	master_num=request.POST.get('type3');
	slave_num=request.POST.get('type4');	
	if storm_h_z == '1' :#and master_slave == '0': #storm log master
		with open('/home/qll/data/storm_master') as f:
			c = f.read()
	elif storm_h_z == '2' :#and master_slave == '1': #storm log slave
		with open('/home/qll/data/storm_slave') as f:
			c = f.read()
	elif storm_h_z == '3' :#and master_slave == '0': #hadoop master
 		with open('/home/qll/data/hadoop_master') as f:
			c = f.read()
	elif storm_h_z == '4' :#and master_slave == '1': #hadoop slave
		with open('/home/qll/data/hadoop_slave') as f:
			c = f.read()
	elif storm_h_z == '5' :#and master_slave == '0': # zoo master 
		with open('/home/qll/data/zoo_master') as f:
			c = f.read()
	elif storm_h_z == '6':# and master_slave == '1': #zoo slave
		with open('/home/qll/data/zoo_slave') as f:
			c = f.read()
	return HttpResponse(json.dumps(c), content_type="application/json")
	return Response(c)
