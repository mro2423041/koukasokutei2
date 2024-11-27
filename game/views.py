
from django.shortcuts import render, get_object_or_404, redirect
from .models import Card
from .forms import CommentForm

def card_list(request):
    cards = Card.objects.all()
    return render(request, 'game/card_list.html', {'cards': cards})

def card_detail(request, pk):
    card = get_object_or_404(Card, pk=pk)
    return render(request, 'game/card_detail.html', {'card': card})

def add_comment_to_card(request, pk):
    card = get_object_or_404(Card, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.card = card
            comment.author = request.user
            comment.save()
            return redirect('card_detail', pk=card.pk)
    else:
        form = CommentForm()
    return render(request, 'game/add_comment_to_card.html', {'form': form})