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
        tmp.save()
        return 1
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
        tmp.save()
        return 1
    except Exception as e:
        print (e)
        return -1

def index(request):
    passed = [0,0]
    failed = [0,0]
    total = 0
    with open('data.json') as f:
        for line in f:
            entry = json.loads(line)
            if populate_repo(entry) == 1:
                passed[0] += 1
            else:
                failed[0] += 1

            if populate_actor(entry) == 1:
                passed[1] += 1
            else:
                failed[1] += 1
            total += 1
            print("Status :  Total  --->  " + str(total))
            print("Repo -> passed : "+ str(passed[0])+ " failed : "+ str(failed[0]))
            print("Actor -> passed : "+ str(passed[1])+ " failed : "+ str(failed[1]))

    return HttpResponse("Hello, its done!")
