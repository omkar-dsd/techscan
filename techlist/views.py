from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.db.models import Count
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from repolist.models import Repo
from techlist.serializers import LanguageSerializer
from django.shortcuts import render, HttpResponse
from repolist.models import Repo
from userlist.models import Actor
import json, requests

ath = "?access_token=1c8d531213e4625d5adb1dcaaba055841ae8a6e7"

def populate_repo(entry):
    repo_id = entry['repo']['id']
    repo_url = entry['repo']['url']
    r = requests.get(repo_url + ath)
    data = json.loads(r.text)
    try:
        tmp = Repo(repo_id=repo_id,
                   url=repo_url,
                   full_name=data['full_name'],
                   description=data['description'],
                   language=data['language'],
                   stargazers_count=data['stargazers_count'],
                   open_issues_count=data['open_issues_count'],
                   forks_count=data['forks_count']
                   )
        return tmp
    except Exception as e:
        print(e)
        return -1

def populate_actor(entry):
    actor_id = entry['actor']['id']
    actor_url = entry['actor']['url']
    r = requests.get(actor_url + ath)
    data = json.loads(r.text)
    try:
        tmp = Actor(actor_id=actor_id,
                    url=actor_url,
                    avatar_url=data['avatar_url'],
                    name=data['name'],
                    login=data['login'],
                    user_type=data['type'],
                    location=data['location'],
                    followers=data['followers'],
                    following=data['following'],
                    repo_id=entry['repo']['id']
                    )
        return tmp
    except Exception as e:
        print (e)
        return -1

def popu(request):
    i = 0
    with open('data.json') as f:
        for line in f:
            entry = json.loads(line)
            a = populate_repo(entry)
            b = populate_actor(entry)
            if not a == -1 and not b == -1:
                a.save()
                b.save()
                i = i + 1
                print("Processed " + str(i))
    return HttpResponse("Done")


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
