from rest_framework import serializers
from .models import Video
class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = "__all__"
class ChargeSerializers(serializers.Serializer):
    video_size_in_MB = serializers.IntegerField()
    length_in_sec = serializers.IntegerField()
    type = serializers.CharField()