from django.contrib import admin
from django.urls import path
from nintendo_drf.dataset3.views import Dataset3ViewSet

# /dataset3/ - GET: Returns all of the entries in the database
#            - POST: Allows user to submit entry into database
#
# /dataset3/[id] - GET: Returns data about 1 database entry
#                - PUT: Edit data about 1 database entry
#                - DELETE: Deletes 1 database entry
#
# /dataset3/populate - GET: Clears database and populates from csv file
urlpatterns = [
    path('', Dataset3ViewSet.game_list),
    path('<int:id>', Dataset3ViewSet.game_detail),
    path('populate', Dataset3ViewSet.populate_database)
]