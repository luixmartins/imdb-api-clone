from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import GenreSerializer, MediaSerializer
from .models import Media, Genre

class MediaCreateList(APIView):
    def get(self, request):
        media = Media.objects.all()
        serializer = MediaSerializer(media, many=True)
        
        return Response(serializer.data) 
    
    def post(self, request):
        data = request.data 
        genre = data.get('genre')
        serializer = MediaSerializer(data=data, genre=genre)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        
        return Response(serializer.errors, status=400)
    
class MediaDetailUpdateDelete(APIView):
    def get(self, request, pk):
        media = Media.objects.get(pk=pk)
        
        serializer = MediaSerializer(media)
        
        if serializer.data: 
            return Response(serializer.data, status=200)
                
        return Response(serializer.errors, status=400)
    
    def put(self, request, pk):
        media = Media.objects.get(pk=pk)
        
        serializer = MediaSerializer(
            instance=media, 
            data=request.data, 
            genre=request.data.get('genre')
            )
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=400)
    
    def delete(self, request, pk):
        media = Media.objects.get(pk=pk)
        
        media.delete()