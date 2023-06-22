from rest_framework import serializers
from .models import UserProfile,ProfileFeedItem
class HelloSerializer(serializers.Serializer):
    """ Serializers a name field for testing our api view """
    name = serializers.CharField(max_length=10)
    desig = serializers.CharField(max_length = 10)

class ProfileFeedItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProfileFeedItem
        fields = ('id','user_profile','status_text','created_on')
        extra_kwargs = {'user_profile': { 'read_only' : True }}

class UserProfileSerializer(serializers.ModelSerializer):
    """ creating Model serializer for the user profiles for object """
    class Meta:
        model = UserProfile
        fields = ('id','email','name','password')
        extra_kwargs = {
            'password':{
                'write_only':True,
                'style':{
                    'input_type':'password'
                }
            },
        }
    def create(self, validated_data):
        """Create and return a new user """
        user = UserProfile.objects.create_user(
            email = validated_data['email'],
            name=validated_data['name'],
            password = validated_data['password']
        )
        return user
    


