from .models import Song
from .serializers import SongSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class SongList(APIView):

    def get(self, request):
        # query for all Song records in the database
        # convert QuerySet of song objects into a list of dictionaries
        # pass serializer.data into Response(), which converts the list of dictionaries into a JSON string literal
        # then returns the response to the requestor (client who hit endpoint)
        songs = Song.objects.all()
        serializer = SongSerializer(songs, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SongSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
