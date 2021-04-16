from rest_framework import serializers
from .models import Song


class SongSerializer(serializers.ModelSerializer):
    # defining fields allows ModelSerializer to match list of fields to model
    # note added id even though it isn't explcitely written in model. Database auto-generates the id
    class Meta:
        model = Song
        fields = ['id', 'title', 'artist', 'album', 'release_date', 'likes']
