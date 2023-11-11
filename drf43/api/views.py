from .serializers import Singer, Song, SingerSerializer, SongSerializer
from rest_framework.viewsets import ModelViewSet

class SongViewSet(ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

class SingerViewSet(ModelViewSet):
    queryset = Singer.objects.all()
    serializer_class = SingerSerializer
