from django.shortcuts import render
from django.http import HttpResponse
from main.models import Watch
import json
from django.contrib.auth.decorators import permission_required
from rest_framework.decorators import api_view, permission_classes
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import IsAuthenticated

@csrf_exempt
@api_view(["POST"])
@permission_classes([IsAuthenticated])
def add_watch_view(request):
    if request.method == 'POST':
        if not request.user.has_perm('main.add_watch'):
            return HttpResponse(status=403)
        data = json.loads(request.body)
        obj, created = Watch.objects.get_or_create(**data)
        return HttpResponse(status=200)
    else:
        return HttpResponse(status=405)
