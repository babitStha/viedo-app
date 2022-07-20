from rest_framework import serializers
from .models import Video
class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = "__all__"
    def create(self, validated_data):
        validated_data.save()
        return validated_data
class ChargeSerializer(serializers.Serializer):
    video_size_in_MB = serializers.IntegerField()
    length_in_sec = serializers.IntegerField()
    type = serializers.CharField()