from django.db import models

# Create your models here.
class Actor(models.Model):
    actor_id = models.BigIntegerField(primary_key=True)
    url = models.URLField(max_length=256)
    avatar_url = models.URLField(max_length=512, null=True)
    name = models.CharField(max_length=128, null=True)
    login = models.CharField(max_length=64)
    user_type = models.CharField(max_length=16, null=True)
    location = models.CharField(max_length=64, null=True)
    followers = models.PositiveIntegerField()
    following = models.PositiveIntegerField()
    repo = models.ForeignKey('repolist.Repo', on_delete=models.CASCADE)

#           Table "public.userlist_actor"
#    Column   |          Type          | Modifiers
# ------------+------------------------+-----------
#  actor_id   | bigint                 | not null
#  url        | character varying(256) | not null
#  avatar_url | character varying(512) | not null
#  name       | character varying(128) | not null
#  login      | character varying(64)  | not null
#  user_type  | character varying(16)  | not null
#  location   | character varying(64)  | not null
#  followers  | integer                | not null
#  following  | integer                | not null
#  repo_id    | bigint                 | not null
