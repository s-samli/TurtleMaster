from django.shortcuts import render
from datetime import date
import random
import math
import json
from rest_framework import viewsets
from rest_framework import permissions
from TurtleMasterApp.serializers import InfectionDataUsSerializer
from TurtleMasterApp.serializers import InfectionDataUsStatisticsSerializer
from TurtleMasterApp.serializers import InfectionDataWorldSerializer
from TurtleMasterApp.serializers import InfectionDataWorldStatisticsSerializer
from TurtleMasterApp.serializers import TimeSeriesDataUsSerializer
from TurtleMasterApp.serializers import TimeSeriesDataWorldSerializer
from TurtleMasterApp.serializers import ViewStatisticsDataSerializer
from TurtleMasterApp.models import InfectionDataUs
from TurtleMasterApp.models import InfectionDataUsStatistics
from TurtleMasterApp.models import InfectionDataWorld
from TurtleMasterApp.models import InfectionDataWorldStatistics
from TurtleMasterApp.models import TimeSeriesDataUs
from TurtleMasterApp.models import TimeSeriesDataWorld
from TurtleMasterApp.models import ViewStatisticsData
from django.http import JsonResponse

def index(request):

    queryset_topline = ViewStatisticsData.objects.all().order_by('timestamp')
    serializer_topeline = ViewStatisticsDataSerializer(queryset_topline, many=True)

    queryset_us_statistics = InfectionDataUsStatistics.objects.all().order_by('timestamp')
    serializer_us_statistics = InfectionDataUsStatisticsSerializer(queryset_us_statistics, many=True)

    queryset_world_statistics = InfectionDataWorldStatistics.objects.all().order_by('timestamp')
    serializer_world_statistics = InfectionDataWorldStatisticsSerializer(queryset_world_statistics, many=True)

    context = {
        'json_topline': json.dumps(serializer_topeline.data),
        'json_us_statistics': json.dumps(serializer_us_statistics.data),
        'json_world_statistics': json.dumps(serializer_world_statistics.data),
    }


    return render(request, 'TurtleMasterApp/index.html', context)

class InfectionDataUsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = InfectionDataUs.objects.all().order_by('timestamp')
    serializer_class = InfectionDataUsSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `province_state` query parameter in the URL.
        """
        queryset = InfectionDataUs.objects.all().order_by('timestamp')

        province_state = self.request.query_params.get('province_state', None)
        if province_state is not None:
            queryset = queryset.filter(province_state=province_state)
        return queryset
# Create your views here.

class InfectionDataUsStatisticsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = InfectionDataUsStatistics.objects.all().order_by('timestamp')
    serializer_class = InfectionDataUsStatisticsSerializer
    permission_classes = [permissions.AllowAny]

class InfectionDataWorldViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = InfectionDataWorld.objects.all().order_by('timestamp')
    serializer_class = InfectionDataWorldSerializer
    permission_classes = [permissions.AllowAny]

class InfectionDataWorldStatisticsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = InfectionDataWorldStatistics.objects.all().order_by('timestamp')
    serializer_class = InfectionDataWorldStatisticsSerializer
    permission_classes = [permissions.AllowAny]

class TimeSeriesDataUsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = TimeSeriesDataUs.objects.all().order_by('timestamp')
    serializer_class = TimeSeriesDataUsSerializer
    permission_classes = [permissions.AllowAny]

class TimeSeriesDataWorldViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = TimeSeriesDataWorld.objects.all().order_by('timestamp')
    serializer_class = TimeSeriesDataWorldSerializer
    permission_classes = [permissions.AllowAny]

class ViewStatisticsDataViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = ViewStatisticsData.objects.all().order_by('timestamp')
    serializer_class = ViewStatisticsDataSerializer
    permission_classes = [permissions.AllowAny]
