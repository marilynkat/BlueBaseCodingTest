from django.contrib import admin
from .models import Game

#allow admin page to display information
#about dataset model
admin.site.register(Game)