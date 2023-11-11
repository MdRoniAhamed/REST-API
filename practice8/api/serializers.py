from .models import Singer, Song
from rest_framework import serializers


class SingerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Singer
        fields = ['id','name','gender','song']

class SongSerializer(serializers.ModelSerializer):
    singer = SingerSerializer(many=True)
    class Meta:
        model = Song
        fields = ['id','title','singer']
        