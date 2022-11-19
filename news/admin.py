from django.contrib import admin
from .models import News

class NewsAdmin(admin.ModelAdmin):
  model = News
  list_display = ('headline', 'date')
  search_fields = ['headline', 'date']

admin.site.register(News, NewsAdmin)