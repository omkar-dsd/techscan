from rest_framework import serializers
from repolist.models import Repo

class LanguageSerializer(serializers.ModelSerializer):
    the_count = serializers.SerializerMethodField()
    class Meta:
        model = Repo
        fields = ('language','the_count')
    def get_the_count(self, obj):
        return obj['the_count']
