from rest_framework import serializers

from .models import Reviews,Project,Userr




class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Userr
        #exclude = ['image']
        fields = ['name', 'email', 'password', 'profession','image']


class ProjectSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Project
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Reviews
        fields = '__all__'
        


