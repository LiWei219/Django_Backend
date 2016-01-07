"""server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url, patterns
from django.contrib import admin
admin.autodiscover()
#user_views

from users.views import *
from django.conf.urls import patterns, url
from users import views
#TrafficMonitor_views
from TrafficMonitor.views_dushboard_resources import *
from TrafficMonitor.views_resource_list import *
from TrafficMonitor.views_traffic_applications import *
from TrafficMonitor.views_traffic_report import *
#DataManager_views
from DataManager.views_history_data import *
from DataManager.views_apply_for_collection import *
from DataManager.views_dataset_query import *
from DataManager.views_management_applications import *
#ClusterManager
from ClusterManager.views_log_management import *
from ClusterManager.views_report_management import *
from ClusterManager.views_cluster_overview import *
from ClusterManager.views_job_management import *

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
]

#Useroperation
urlpatterns += [

    url(r'^login/$', login.as_view()),
    url(r'^regist/$', regist.as_view()),

]

#TrafficMonitor
urlpatterns += [
    #dushboard_resources
    url(r'^RealtimeApplicationThroughput/$', RealtimeApplicationThroughput.as_view()),
    url(r'^RealtimeApplicationDataPacket/$', RealtimeApplicationDataPacket.as_view()),
    url(r'^RealtimeApplicationStream/$', RealtimeApplicationStream.as_view()),
    url(r'^RealtimeSourceCountryThroughput/$', RealtimeSourceCountryThroughput.as_view()),
    url(r'^RealtimeDestinationCountryThroughput/$', RealtimeDestinationCountryThroughput.as_view()),
    url(r'^RealtimeApplicationStatisticsForm/$', RealtimeApplicationStatisticsForm.as_view()),
    url(r'^RealtimeApplicationChart/$', RealtimeApplicationChart.as_view()),
    url(r'^RealtimeSourceCountryChart/$', RealtimeSourceCountryChart.as_view()),
    url(r'^RealtimeDestinationCountryChart/$', RealtimeDestinationCountryChart.as_view()),

    #resource_list
    url(r'^ResourceList/$', ResourceList.as_view()),

    #traffic_applications
    url(r'^AnomlyDetections/$', AnomlyDetections.as_view()),
    url(r'^AnomlyDetectionsid/$', AnomlyDetectionsid.as_view()),

    #traffic_report
    url(r'^ReportForm/$', ReportForm.as_view()),

]

#DataManager
urlpatterns += [
    #history_data
    url(r'^OfflineApplicationLayerResults/$', OfflineApplicationLayerResults.as_view()),
    url(r'^OfflineTransportLayerResults/$', OfflineTransportLayerResults.as_view()),
    url(r'^OfflineNetworkLayerResults/$', OfflineNetworkLayerResults.as_view()),

    #dataset_query
    url(r'^StandardDatasetList/$', StandardDatasetList.as_view()),
    url(r'^StandardDatasetsDetail/$', StandardDatasetsDetail.as_view()),
    url(r'^StandardDatasetQuery/$', StandardDatasetQuery.as_view()),

    #apply_for_collection
    url(r'^GetAvailableDatasets/$', GetAvailableDatasets.as_view()),
    url(r'^ApplyNewDataset/$', ApplyNewDataset.as_view()),

    #management_application
    url(r'^GetAvailableJar/$', GetAvailableJar.as_view()),
    url(r'^UploadJar/$', UploadJar.as_view()),
    url(r'^RunJar/$', RunJar.as_view()),

]

#ClusterManager
urlpatterns += [
    #cluster_overview
    url(r'^ClusterOverview/$', ClusterOverview.as_view()),

    #job_management
    url(r'^JobManagement/$', JobManagement.as_view()),

    #log_management
    url(r'^LogManagement/$', LogManagement.as_view()),

    #report_management
    url(r'^ReportManagement/$', ReportManagement.as_view()),
]
