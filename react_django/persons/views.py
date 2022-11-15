from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Person
from .serializers import *
from faker import Faker
from faker_vehicle import VehicleProvider

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
        print('-->-->-->-->-->-->', data)

        serializer = PersonSerializer(data, context={'request': request} ,many=True)

        return Response(
            {'data': serializer.data,
            'count': paginator.count,
            'numpages' : paginator.num_pages,
            'per': int(per),
            'page': int(page),
            }
            )

# @api_view(['GET', 'POST'])
# def persons_fake(request):
#     if request.method == 'GET':
#         method = request.GET.get('method')
#         if method == 'generate': 
#             count = int(request.GET.get('count'))
#             faker = Faker()
#             faker.add_provider(VehicleProvider)
#             for _ in range(0, count):
#                 print(12)
#                 Person.objects.create(name=faker.first_name(), surname=faker.last_name(), driverlicensenum=faker.nic_handle('DL'), birthdate=faker.date_between(18))
#         return Response({})