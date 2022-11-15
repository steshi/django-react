import django_filters

class CarsFilter(django_filters.FilterSet):
    class Meta:
        model = Car
        # Declare all your model fields by which you will filter
        # your queryset here:
        fields = ['model', 'manufacturedDate']
