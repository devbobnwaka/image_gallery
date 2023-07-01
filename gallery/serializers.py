import io
from rest_framework import serializers

from .models import Image
from utils.utils import get_filtered_image

class ListImageSerializer(serializers.ModelSerializer):
    detail_url = serializers.HyperlinkedIdentityField(view_name='image-retrieve-update', lookup_field='slug')
    class Meta:
        model = Image
        fields = (
            'pk',
            'detail_url',
            'slug',
        )


class ImageSerializer(serializers.ModelSerializer):
    encoded_filter_image = serializers.SerializerMethodField()
    class Meta:
        model = Image
        fields = (
            'user',
            'title',
            'slug',
            'action',
            'description',
            'image_path',
            'encoded_filter_image'
        )
        extra_kwargs = {
            'user': {'read_only': True},
            'slug': {'read_only': True},
            'title': {'required' : False},
            'description': {'required' : False},
        }

    def get_encoded_filter_image(self, obj):
        encoded_image = get_filtered_image(obj.image_path, obj.action)
        return encoded_image

    def create(self, validated_data):
        user = self.context.get('request').user
        image = Image.objects.create(**validated_data, user=user) 
        return image

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.action = validated_data.get('action', instance.action)
        instance.image_path = validated_data.get('image_path', instance.image_path)
        instance.description = validated_data.get('description', instance.description)
        return instance

