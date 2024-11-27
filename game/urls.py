from django.urls import path
from . import views

urlpatterns = [
    path('', views.card_list, name='card_list'),
    path('card/<int:pk>/', views.card_detail, name='card_detail'),
    path('card/<int:pk>/comment/', views.add_comment_to_card, name='add_comment_to_card'),
]

