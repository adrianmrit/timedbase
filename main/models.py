from django.db import models
from django_countries.fields import CountryField
from utils.strings import super_clean_str
from djmoney.models.fields import MoneyField
from easy_thumbnails.signals import saved_file
from easy_thumbnails.signal_handlers import generate_aliases_global


# generate thumbnails on upload
saved_file.connect(generate_aliases_global)


# Create your models here.
class Brand(models.Model):
    name = models.CharField(max_length=60, unique=True)
    cleaned_name = models.CharField(max_length=60, unique=True)
    country = CountryField(blank=True, null=True)
    url = models.URLField()
    description = models.CharField(max_length=2000, blank=True, null=True)
    logo=models.ImageField(upload_to='brand_logo/', blank=True, null=True)

    def save(self, *args, **kwargs):
        self.cleaned_name = super_clean_str(self.name)
        super(Brand, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


# TODO: fix fields
class Watch(models.Model):
    url = models.URLField(unique=True, blank=True, null=True)
    name = models.CharField(max_length=60)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name="watches", related_query_name="watch")
    reference = models.CharField(max_length=30)
    cleaned_reference = models.CharField(max_length=30)
    description = models.TextField(max_length=2000, blank=True, null=True)

    image = models.ImageField(upload_to='watch_image/', blank=True, null=True)

    origin = models.CharField(max_length=30, null=True, blank=True)
    gender = models.CharField(max_length=30, null=True, blank=True)
    collection = models.CharField(max_length=80, null=True, blank=True)
    water_resistance = models.CharField(max_length=80, null=True, blank=True)
    case_shape = models.CharField(max_length=80, null=True, blank=True)
    case_diameter = models.CharField(max_length=80, null=True, blank=True)
    case_width = models.CharField(max_length=80, null=True, blank=True)
    case_length = models.CharField(max_length=80, null=True, blank=True)
    case_thickness = models.CharField(max_length=80, null=True, blank=True)
    case_back = models.CharField(max_length=80, null=True, blank=True)
    crystal = models.CharField(max_length=80, null=True, blank=True)
    case_material = models.CharField(max_length=80, null=True, blank=True)
    bezel_material = models.CharField(max_length=80, null=True, blank=True)
    weight = models.CharField(max_length=80, null=True, blank=True)
    lugs_width = models.CharField(max_length=80, null=True, blank=True)
    movement_type = models.CharField(max_length=80, null=True, blank=True)
    caliber_diameter = models.CharField(max_length=80, null=True, blank=True)
    movement_model = models.CharField(max_length=80, null=True, blank=True)
    jewels = models.CharField(max_length=80, null=True, blank=True)
    time = models.CharField(max_length=80, null=True, blank=True)
    caliber = models.CharField(max_length=80, null=True, blank=True)
    battery = models.CharField(max_length=80, null=True, blank=True)
    functions = models.CharField(max_length=80, null=True, blank=True)
    dial_color = models.CharField(max_length=80, null=True, blank=True)
    indexes = models.CharField(max_length=80, null=True, blank=True)
    strap_material = models.CharField(max_length=80, null=True, blank=True)
    buckle = models.CharField(max_length=80, null=True, blank=True)
    strap_color = models.CharField(max_length=80, null=True, blank=True)
    features = models.CharField(max_length=80, null=True, blank=True)

    def __str__(self):
        return "{} {}".format(self.name, self.reference)

    def save(self, *args, **kwargs):
        self.cleaned_reference = super_clean_str(self.reference)

        super(Watch, self).save(*args, **kwargs)

    class Meta:
        unique_together = [['brand', 'cleaned_reference'], ['brand', 'reference']]
        verbose_name_plural = "watches"


class Price(models.Model):
    price = MoneyField(max_digits=14, decimal_places=2, default_currency='USD')
    url = models.URLField()
    store = models.ForeignKey("main.Store", on_delete=models.CASCADE)
    watch = models.ForeignKey("main.Watch", on_delete=models.CASCADE, related_name="prices", related_query_name="price")
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return "{} timestamp:{}".format(self.watch.cleaned_reference, self.timestamp)


class Store(models.Model):
    name = models.CharField(max_length=60, unique=True)
    url = models.URLField(unique=True)
    cleaned_name = models.CharField(max_length=60, unique=True)

    def save(self, *args, **kwargs):
        self.cleaned_name = super_clean_str(self.name)

        super(Store, self).save(*args, **kwargs)

    def __str__(self):
        return self.name