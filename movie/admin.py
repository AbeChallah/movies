from django.contrib import admin
from .models import Movie, Review

class MovieAdmin(admin.ModelAdmin):
  model = Movie
  search_fields = ['title', 'description']

admin.site.register(Movie, MovieAdmin)

class ReviewAdmin(admin.ModelAdmin):
  model = Review
  list_display = ('user', 'movie', 'text', 'watchAgain')
  search_fields = ['text']

admin.site.register(Review, ReviewAdmin)