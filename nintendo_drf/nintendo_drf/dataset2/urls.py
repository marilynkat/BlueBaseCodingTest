from django.contrib import admin
from django.urls import path
from nintendo_drf.dataset2.views import Dataset2ViewSet

# /dataset2/ - GET: Returns all of the entries in the database
#            - POST: Allows user to submit entry into database
#
# /dataset2/[id] - GET: Returns data about 1 database entry
#                - PUT: Edit data about 1 database entry
#                - DELETE: Deletes 1 database entry
#
# /dataset2/populate - GET: Clears database and populates from csv file
urlpatterns = [
    path('', Dataset2ViewSet.game_list),
    path('<int:id>', Dataset2ViewSet.game_detail),
    path('populate', Dataset2ViewSet.populate_database)
]