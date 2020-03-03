from django.shortcuts import render
from .models import Brand
from django.db.models.functions import Substr
from django.db.models import Count
import string

# Create your views here.

def index(request):
    return render(request, 'main/index.html')

def brands(request, letter=None):
    count_letters_queryset = []
    if not letter:
        brands = Brand.objects.order_by('?')[0:10]
    else:
        brands = Brand.objects.filter(cleaned_name__startswith=letter)

    available_alphabet = Brand.objects.all().annotate(first_letter=Substr('cleaned_name', 1, 1)).values_list("first_letter", flat=True).distinct()
    # available_brands = count_letters_queryset[0].union(*count_letters_queryset[1:])

    return render(request, 'main/brands.html', {'brands': brands, 'available_alphabet': available_alphabet, 'alphabet': string.ascii_lowercase, 'active_letter': letter})