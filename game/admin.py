from django.contrib import admin
from .models import Card, Comment

class CardAdmin(admin.ModelAdmin):
    list_display = ('name', 'elixir_cost', 'hitpoints', 'damage', 'image')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('card', 'author', 'text', 'created_date')

admin.site.register(Card, CardAdmin)
admin.site.register(Comment, CommentAdmin)