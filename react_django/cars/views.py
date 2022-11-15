from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Car
from .serializers import *


@api_view(['GET', 'POST'])
def cars_list(request):
    """
    List  cars.
    """
    if request.method == 'GET':
        data = []
        sortby = request.GET.get('sortby', 'pk')
        cars = Car.objects.all().order_by(sortby)
        filtersString = request.GET.get('filters', '')
        filtersEntries = filtersString.split('*')
        filtersPairs = list(map(lambda f: f.split('='), filtersEntries))
        filtersDict = {}
        if len(filtersString) > 0:
            for key, value in filtersPairs:
                filtersDict[key] = value
            for filter in filtersDict:
                if filter == 'model':
                    cars = cars.filter(model__contains=filtersDict[filter])
                if filter == 'number':
                    cars = cars.filter(number__contains=filtersDict[filter])
                if filter == 'manufacturedate':
                    cars = cars.filter(manufacturedate__contains=filtersDict[filter])
        page = request.GET.get('page', 1)
        per = request.GET.get('per', 10)
        paginator = Paginator(cars, per)
        try:
            data = paginator.page(page)
        except PageNotAnInteger:
            data = paginator.page(1)
        except EmptyPage:
            data = paginator.page(paginator.num_pages)
            page=paginator.num_pages

        serializer = CarSerializer(data,context={'request': request} ,many=True)

        return Response(
            {'data': serializer.data,
            'count': paginator.count,
            'numpages' : paginator.num_pages,
            'per': int(per),
            'page': int(page),
            }
            )
