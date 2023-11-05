from rest_framework import serializers
from .models import Student


# class StudentSerializer(serializers.Serializer):
#     first_name = serializers.CharField()
#     last_name = serializers.CharField()
#     number = serializers.IntegerField()

#     def create(self, validated_data):
#         return Student(**validated_data)

#     def update(self, instance, validated_data):
#         instance.first_name = validated_data.get('email', instance.email)
#         instance.last_name = validated_data.get('content', instance.content)
#         instance.number = validated_data.get('created', instance.created)
#         instance.save()
#         return instance

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        # fields = ['number', 'last_name', 'first_name']
        # fields = '__all__'
        exclude = ['id']
