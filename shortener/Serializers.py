from rest_framework import serializers
from .models import URL


class URLSerializer(serializers.ModelSerializer):
    class Meta:
        model = URL
        fields = ('id', 'full_url')


class URLListSerializer(serializers.ModelSerializer):
    class Meta:
        model = URL
        fields = ('id', 'full_url', 'url_hash', 'clicks', 'created_at')


# class HistorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = URL
#         fields = ('id', 'clicks', 'created_at')
