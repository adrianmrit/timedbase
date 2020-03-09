from django.shortcuts import render, get_object_or_404
from .models import Brand, Watch, Price, Store
from django.db.models.functions import Substr
from django.db.models import Count
import string
from django.views import View
from django.db.models import OuterRef, Subquery, Exists
from django.forms.models import model_to_dict

# Create your views here.

class IndexView(View):
    def get(self, request):
        # TODO: Better home page
        return render(request, 'main/index.html')


class BrandsView(View):
    def get (self, request, letter=None):
        count_letters_queryset = []
        if not letter:
            brands = Brand.objects.order_by('?')[0:10]
        else:
            brands = Brand.objects.filter(cleaned_name__startswith=letter)

        available_alphabet = Brand.objects.all().annotate(first_letter=Substr('cleaned_name', 1, 1)).values_list("first_letter", flat=True).distinct()
        # available_brands = count_letters_queryset[0].union(*count_letters_queryset[1:])

        return render(request, 'main/brands.html', {'brands': brands, 'available_alphabet': available_alphabet, 'alphabet': string.ascii_lowercase, 'active_letter': letter})


class BrandView(View):
    def get(self, request, id):
        brand = get_object_or_404(Brand, pk=id)

        return render(request, 'main/brand.html', {'brand': brand})


class WatchView(View):
    def get(self, request, id):
        watch = get_object_or_404(Watch, pk=id)

        watch_details = model_to_dict(watch)
        del watch_details['name']
        del watch_details['url']
        del watch_details['image']
        del watch_details['description']
        del watch_details['id']
        del watch_details['cleaned_reference']
        del watch_details['brand']

        prices = Price.objects.filter(watch=watch).order_by('store', '-timestamp').distinct('store')

        return render(request, 'main/watch.html', {'watch': watch, 'prices': prices, 'watch_details': watch_details})