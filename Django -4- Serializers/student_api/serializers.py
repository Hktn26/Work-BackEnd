from rest_framework import serializers

class StudentSerializer(serializers.Serializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    number = serializers.IntegerField()

    