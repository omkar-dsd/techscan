from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.db.models import Count
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from userlist.models import Actor
from userlist.serializers import ActorSerializer


@csrf_exempt
def index(request, login):
    """
    List all categorised repos.
    """
    actor = Actor.objects.get(login=login)
    resp = request.GET.get('json')
    print(actor)
    if resp:
        serializer = ActorSerializer(actor, many=True)
        return JsonResponse(serializer.data, safe=False)
    else:
        return render(request, 'userlist/main.html', {'data': actor})
