from django.db import models
from django.contrib.auth.models import User

class Card(models.Model):
    name = models.CharField(max_length=100)
    elixir_cost = models.IntegerField()
    description = models.TextField()
    hitpoints = models.IntegerField()
    damage = models.IntegerField()
    image = models.ImageField(upload_to='card_images/', blank=True, null=True)  # 画像フィールドを追加

    def __str__(self):
        return self.name

class Comment(models.Model):
    card = models.ForeignKey(Card, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text