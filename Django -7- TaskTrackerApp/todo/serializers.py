from rest_framework import serializers
from .models import Todo

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        # fields = '__all__'
        exclude = [
            'create_date',
            'update_date',
        ]