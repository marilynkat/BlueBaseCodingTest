from django.contrib import admin
from django.urls import path
from nintendo_drf.dataset1.views import Dataset1ViewSet

# /dataset1/ - GET: Returns all of the entries in the database
#            - POST: Allows user to submit entry into database
#
# /dataset1/[id] - GET: Returns data about 1 database entry
#                - PUT: Edit data about 1 database entry
#                - DELETE: Deletes 1 database entry
#
# /dataset1/populate - GET: Clears database and populates from csv file
urlpatterns = [
    path('', Dataset1ViewSet.game_list),
    path('<int:id>', Dataset1ViewSet.game_detail),
    path('populate', Dataset1ViewSet.populate_database)
]