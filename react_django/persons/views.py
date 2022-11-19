from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Person
from .serializers import *

@api_view(['GET', 'POST'])
def persons_list(request):
    """
    List  persons.
    """
    if request.method == 'GET':
        data = []
        sortby = request.GET.get('sortby', 'pk')
        persons = Person.objects.all().order_by(sortby)
        filtersString = request.GET.get('filters', '')
        filtersEntries = filtersString.split('*')
        filtersPairs = list(map(lambda f: f.split('='), filtersEntries))
        filtersDict = {}

        if len(filtersString) > 0:
            for key, value in filtersPairs:
                filtersDict[key] = value
            for filter in filtersDict:
                if filter == 'name':
                    persons = persons.filter(name__contains=filtersDict[filter])
                if filter == 'surname':
                    persons = persons.filter(surname__contains=filtersDict[filter])
                if filter == 'birthdate':
                    persons = persons.filter(birthdate__contains=filtersDict[filter])
                if filter == 'driverlicensenum':
                    persons = persons.filter(driverlicensenum__contains=filtersDict[filter])
        page = request.GET.get('page', 1)
        per = request.GET.get('per', 10)
        paginator = Paginator(persons, per)

        try:
            data = paginator.page(page)
        except PageNotAnInteger:
            data = paginator.page(1)
        except EmptyPage:
            data = paginator.page(paginator.num_pages)
            page=paginator.num_pages

        serializer = PersonSerializer(data, context={'request': request}, many=True)

        return Response(
            {'data': serializer.data,
            'count': paginator.count,
            'numpages' : paginator.num_pages,
            'per': int(per),
            'page': int(page),
            }
            )

@api_view(['GET', 'POST'])
def rels(request):
    if request.method == 'GET':
        data = []
        sortby = request.GET.get('sortby', 'pk')
        persons = Person.objects.prefetch_related('cars').order_by(sortby)
        filtersString = request.GET.get('filters', '')
        filtersEntries = filtersString.split('*')
        filtersPairs = list(map(lambda f: f.split('='), filtersEntries))
        filtersDict = {}
        if len(filtersString) > 0:
            for key, value in filtersPairs:
                filtersDict[key] = value
            for filter in filtersDict:
                if filter == 'name':
                    persons = persons.filter(name__contains=filtersDict[filter])
                if filter == 'surname':
                    persons = persons.filter(surname__contains=filtersDict[filter])
                if filter == 'driverlicensenum':
                    persons = persons.filter(driverlicensenum__contains=filtersDict[filter])
                if filter == 'model':
                    persons = persons.filter(cars__model__contains=filtersDict[filter])
                if filter == 'number':
                    persons = persons.filter(cars__number__contains=filtersDict[filter])

        page = request.GET.get('page', 1)
        per = request.GET.get('per', 10)
        paginator = Paginator(persons, per)
        try:
            data = paginator.page(page)
        except PageNotAnInteger:
            data = paginator.page(1)
        except EmptyPage:
            data = paginator.page(paginator.num_pages)
            page=paginator.num_pages
        serializer = RelSerializer(data, context={'request': request}, many=True)
        result = []
        for person in serializer.data:
            for car in person['cars']:
                result.append({
                    'pk': person['pk'],
                    'name': person['name'],
                    'surname': person['surname'],
                    'driverlicensenum': person['driverlicensenum'],
                    'model': car['model'],
                    'number': car['number'],
                })

        return Response(
            {   
                'data': result,
                'count': paginator.count,
                'numpages' : paginator.num_pages,
                'per': int(per),
                'page': int(page),
            }
            )

