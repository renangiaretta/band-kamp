from rest_framework import serializers

from .models import Album


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ['id', 'name', 'year', 'user_id']
        extra_kwargs = {
            'id': {'read_only': True},
            'user_id': {'read_only': True}
        }

    def create(self, validated_data: dict) -> Album:
        return Album.objects.create(**validated_data)
