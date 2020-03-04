from django.http import HttpResponse
from main.models import Watch, Brand
import json
from rest_framework.decorators import api_view, permission_classes
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import IsAuthenticated
from utils.strings import super_clean_str


@csrf_exempt
@api_view(["POST"])
@permission_classes([IsAuthenticated])
def add_watch_view(request):
    # TODO: clean the code and use class based views.
    """View used by the crawler to upload watches.
    Testing using the crawler is easier.
    """
    if request.method == 'POST':
        # check user permissions
        if not request.user.has_perm('main.add_watch'):
            return HttpResponse(status=403)

        data = json.loads(request.data['json'])
        data['brand'] = super_clean_str(data['brand'])

        # Upload the watch only if there is a brand for it in the database
        try:
            data['brand'] = Brand.objects.get(cleaned_name=data['brand'])
        except Brand.DoesNotExist:
            return HttpResponse(status=409)

        # TODO: Clear the danger
        watch = Watch(**data)  # !DANGER: Data must contain the same fields as the watch
        watch.image = request.FILES["image"]
        watch.save()

        return HttpResponse(status=200)
    else:
        return HttpResponse(status=405)
