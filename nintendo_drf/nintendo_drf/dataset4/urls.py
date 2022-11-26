from django.contrib import admin
from django.urls import path
from nintendo_drf.dataset4.views import Dataset4ViewSet

# /dataset4/ - GET: Returns all of the entries in the database
#            - POST: Allows user to submit entry into database
#
# /dataset4/[id] - GET: Returns data about 1 database entry
#                - PUT: Edit data about 1 database entry
#                - DELETE: Deletes 1 database entry
#
# /dataset4/populate - GET: Clears database and populates from csv file
urlpatterns = [
    path('', Dataset4ViewSet.game_list),
    path('<int:id>', Dataset4ViewSet.game_detail),
    path('populate', Dataset4ViewSet.populate_database)
]