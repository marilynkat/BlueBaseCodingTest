from django.http import JsonResponse
from .models import Game
from .serializer import GameSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import requests
import csv
import json
import io

class Dataset4ViewSet():
    @api_view(['GET'])
    def populate_database(request):
        #clear table
        Game.objects.all().delete()

        #get csv file
        response = requests.get('https://bluebase.blob.core.windows.net/internship/df_5.csv')

        #rename headers to match models
        full = "id,title,publisher,year\n" + response.text
        
        #turn csv into json object and populate databasae
        reader = csv.DictReader(io.StringIO(full))
        json_data = json.dumps(list(reader))
        json_dic = json.loads(json_data)
        for x in json_dic:
            serializer = GameSerializer(data=x)
            if serializer.is_valid():
                serializer.save()
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
            
        # Remove first entry in db since it's headers only    
        Game.objects.first().delete()
        return Response(status=status.HTTP_201_CREATED)
    
    @api_view(['GET', 'POST'])
    def game_list(request):
        #return information for all games
        if request.method == 'GET':
            games = Game.objects.all()
            serializer = GameSerializer(games, many=True)
            return Response(serializer.data)
        
        #add new game entry
        if request.method == 'POST':
            serializer = GameSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            
    @api_view(['GET', 'PUT', 'DELETE'])
    def game_detail(request, id):
        #select game by id
        try:
            game = Game.objects.get(pk=id)
        except Game.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        #return game information
        if request.method == 'GET':
            serializer = GameSerializer(game)
            return Response(serializer.data)
        
        #update game information
        elif request.method == 'PUT':
            serializer = GameSerializer(game, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        #delete game 
        elif request.method == 'DELETE':
            game.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)