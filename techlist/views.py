from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.db.models import Count
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from repolist.models import Repo
from techlist.serializers import LanguageSerializer


@csrf_exempt
def index(request):
    """
    List all categorised repos.
    """
    field = 'language'
    repos = Repo.objects.values(field).order_by(field).annotate(the_count=Count(field)).order_by('-the_count').filter(the_count__gte=30)
    resp = request.GET.get('json')
    if resp:
        serializer = LanguageSerializer(repos, many=True)
        return JsonResponse(serializer.data, safe=False)
    else:
        return render(request, 'techlist/main.html', {'data': repos})
