from rest_framework import serializers
from .models import User

class UserPublicSerializer(serializers.Serializer):
    email = serializers.CharField(read_only=True)
    first_name = serializers.CharField(read_only=True)
    last_name = serializers.CharField(read_only=True)


class UserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password', 'password2']
        extra_kwargs = {
            'first_name ': {'required': False},
            'last_name ': {'required': False},
            'password' : {'write_only': True},
        }

    def validate(self, data):
        """
        Check that the password match.
        """
        if data.get('password') != data.get('password2'):
            raise serializers.ValidationError("Password does not match")
        return data

    def create(self, validated_data):
        validated_data.pop('password2')  # Remove password2 from validated_data
        user = User.objects.create_user(**validated_data)
        return user