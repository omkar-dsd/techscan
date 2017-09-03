from rest_framework import serializers
from userlist.models import Actor

class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ('actor_id','url','avatar_url','name','login','user_type','location','followers', 'following','repo_id')
