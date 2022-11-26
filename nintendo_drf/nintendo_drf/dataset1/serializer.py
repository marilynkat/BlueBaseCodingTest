from rest_framework import serializers
from .models import Game

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ['id', 'title', 'developer', 'publisher1', 'publisher2', 'release_date1', 'release_date2']