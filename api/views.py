from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Video
from .serializers import VideoSerializer
from rest_framework import status

# Create your views here.

@api_view(['GET','POST'])
def get_videos(request):
    if request.method == "GET":
        video = Video.objects.all()
        serializer = VideoSerializer(video, many=True)
        return Response(serializer.data)
    if request.method == "POST":
        serializer = VideoSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response("File Uploaded", status=status.HTTP_201_CREATED)
    return Response("Failed to upload", status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def add_video(request):
    if request.method == "POST":
        serializer = VideoSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response("File Uploaded", status=status.HTTP_201_CREATED)
    return Response("Failed to upload", status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def get_charge(request):
    if request.data:
        max_len = 6 * 60 + 18
        video_size = float(request.data.get('video_size_in_MB'))
        length_in_sec = float(request.data.get('length_in_sec'))
        type = request.data.get('type')
        charges= 0.0
        charges += (5 if (video_size < 500) else 12.5)
        charges += (12.5 if (length_in_sec < max_len) else 20)
        return Response({'charges':charges})
    return Response("Request body shouldnot be empty", status=status.HTTP_400_BAD_REQUEST)
