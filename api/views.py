from django.http import HttpResponse
from main.models import Watch, Brand, Price, Store
import json
from rest_framework.decorators import api_view, permission_classes
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from utils.strings import super_clean_str
# from django.views import View
from django.utils.decorators import method_decorator
from rest_framework.views import APIView
from utils.strings import super_clean_str, super_clean_price

@method_decorator(csrf_exempt, name='dispatch')
class AddWatchView(APIView):
    # @method_decorator(api_view(["POST"]))
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    @staticmethod
    def get_extra(data):
        extra_data = {}
        extra_data['sale_url'] = data['sale_url']
        extra_data['store'] = super_clean_str(data['store'])
        extra_data['price'] = super_clean_price(data['price'])
        extra_data['currency'] = data['currency']
        del data['sale_url']
        del data['store']
        del data['price']
        del data['currency']

        return extra_data

    @staticmethod
    def get_or_create_watch(data, image):
        # TODO: Clear the danger
        try:
            watch = Watch.objects.get(cleaned_reference=super_clean_str(data['reference']))
        except Watch.DoesNotExist:
            watch = Watch(**data)  # !DANGER: Data must contain the same fields as the watch
            watch.image = image
            watch.save()

        return watch

    @staticmethod
    def save_price(request, watch, extra):
        try:
            store = Store.objects.get(cleaned_name=extra['store'])
        except Store.DoesNotExist:
            return None

        price = Price(store=store, watch=watch, price=extra['price'], price_currency=extra['currency'], url=extra['sale_url'])
        price.save()

    def post(self, request):
        # TODO: clean the code and use class based views.
        """View used by the crawler to upload watches.
        Testing using the crawler is easier.
        """
        # check user permissions
        if not request.user.has_perm('main.add_watch'):
            return HttpResponse(status=403)

        data = json.loads(request.data['json'])
        data['brand'] = super_clean_str(data['brand'])
        extra = AddWatchView.get_extra(data)

        # Upload the watch only if there is a brand for it in the database
        try:
            data['brand'] = Brand.objects.get(cleaned_name=data['brand'])
        except Brand.DoesNotExist:
            return HttpResponse(status=409)

        watch = AddWatchView.get_or_create_watch(data, request.FILES["image"])

        if extra['price']:
            AddWatchView.save_price(request, watch, extra)

        return HttpResponse(status=200)
