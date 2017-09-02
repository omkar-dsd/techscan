from django.db import models

# Create your models here.
class Repo(models.Model):
    repo_id = models.BigIntegerField(primary_key=True)
    url = models.URLField(max_length=256)
    full_name = models.CharField(max_length=128, null=True)
    description = models.TextField(max_length=1024, null=True)
    language = models.CharField(max_length=32, null=True)
    stargazers_count = models.PositiveIntegerField()
    open_issues_count = models.PositiveIntegerField()
    forks_count = models.PositiveIntegerField()

#               Table "public.repolist_repo"
#       Column       |          Type          | Modifiers
# -------------------+------------------------+-----------
#  repo_id           | bigint                 | not null
#  url               | character varying(256) | not null
#  full_name         | character varying(128) | not null
#  description       | text                   | not null
#  language          | character varying(32)  | not null
#  stargazers_count  | integer                | not null
#  open_issues_count | integer                | not null
#  forks_count       | integer                | not null
