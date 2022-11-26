from django.contrib import admin
from django.urls import path
from nintendo_drf.dataset5.views import Dataset5ViewSet

# /dataset5/ - GET: Returns all of the entries in the database
#            - POST: Allows user to submit entry into database
#
# /dataset5/[id] - GET: Returns data about 1 database entry
#                - PUT: Edit data about 1 database entry
#                - DELETE: Deletes 1 database entry
#
# /dataset5/populate - GET: Clears database and populates from csv file
urlpatterns = [
    path('', Dataset5ViewSet.game_list),
    path('<int:id>', Dataset5ViewSet.game_detail),
    path('populate', Dataset5ViewSet.populate_database)
]