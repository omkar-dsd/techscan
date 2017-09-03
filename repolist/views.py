from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.db.models import Count
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.postgres.search import SearchVector
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from repolist.models import Repo
from repolist.serializers import RepoSerializer

def search(request):
    q = request.GET.get('q')
    print (q)
    return HttpResponse(q)

@csrf_exempt
def index(request, language):
    """
    List all categorised repos.
    """
    repos_list = Repo.objects.filter(language__iexact=language)
    paginator = Paginator(repos_list, 9)
    page = request.GET.get('page')
    resp = request.GET.get('json')
    try:
        repos = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        repos = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        repos = paginator.page(paginator.num_pages)
    if resp:
        serializer = LanguageSerializer(repos, many=True)
        return JsonResponse(serializer.data, safe=False)
    else:
        return render(request, 'repolist/main.html', {'data': repos, 'paginate' : range(paginator.num_pages), 'lang': language})
