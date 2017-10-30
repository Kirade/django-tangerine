from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from .models import Board

from .forms import BoardForm


def index_view(request):
    board_obj = Board.objects.all()
    return render(request, 'website/index.html', {'board_obj': board_obj})


def board_detail(request, pk):
    board_obj = get_object_or_404(Board, pk=pk)
    return render(request, 'website/board_detail.html', {'board_obj': board_obj})


def board_new(request):

    if request.method == 'POST':
        form = BoardForm(request.POST)

        if form.is_valid():
            board = form.save(commit=False)
            board.created_date = timezone.now()
            board.save()

            return redirect('board_detail', pk=board.pk)

    else:
        form = BoardForm

    return render(request, 'website/board_edit.html', {'form': form})


def board_edit(request, pk):

    board = get_object_or_404(Board, pk=pk)
    if request.method == 'POST':
        form = BoardForm(request.POST, instance=board)
        if form.is_valid():
            board = form.save(commit=False)
            board.created_date = timezone.now()
            board.save()
            return redirect('board_detail', pk=board.pk)
    else:
        form = BoardForm(instance=board)

    return render(request, 'website/board_edit.html', {'form': form})



