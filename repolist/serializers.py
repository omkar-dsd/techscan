from rest_framework import serializers
from repolist.models import Repo

class RepoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Repo
        fields = ('repo_id','url','full_name','description','language','stargazers_count','open_issues_count','forks_count')
