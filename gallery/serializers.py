from rest_framework import serializers

from .models import Image



class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = (
            'user',
            'title',
            'slug',
            'action',
            'description',
            'image_path',
        )
        extra_kwargs = {
            'user': {'read_only': True},
            'slug': {'read_only': True},
            'title': {'required' : False},
            'description': {'required' : False},
        }

    def create(self, validated_data):
        user = self.context.get('request').user
        image = Image.objects.create(**validated_data, user=user) 
        return image
