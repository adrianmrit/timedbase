from django.db import models
from django_countries.fields import CountryField

# Create your models here.
class Brand(models.Model):
    name = models.CharField(max_length=60, unique=True)
    cleaned_name = models.CharField(max_length=60, unique=True)
    country = CountryField(blank=True, null=True)
    website = models.URLField()
    description = models.CharField(max_length=2000, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.cleaned_name = ''.join(x for x in self.name if x.isalnum()).lower()

        super(Brand, self).save(*args, **kwargs)

    def __str__(self):
        return self.name



class Watch(models.Model):
    url = models.URLField(unique=True)
    image = models.URLField(blank=True, null=True)
    name = models.CharField(max_length=60)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    # cleaned_brand = models.CharField(max_length=60)
    reference = models.CharField(max_length=30)
    cleaned_reference = models.CharField(max_length=30)
    description = models.TextField(max_length=2000, blank=True)

    origin = models.CharField(max_length=30, null=True, blank=True)
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
        self.cleaned_reference = ''.join(x for x in self.reference if x.isalnum()).lower()

        super(Watch, self).save(*args, **kwargs)

    class Meta:
        unique_together = [['brand', 'cleaned_reference'], ['brand', 'reference']]
        verbose_name_plural = "watches"
