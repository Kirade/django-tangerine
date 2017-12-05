from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Board, Product
from .forms import BoardForm


class IndexView(TemplateView):
    template_name = 'website/index.html'

    # 넘기려고 하는 데이터를 context안에 dictionary로 넣을 수 있다.
    # as_view(extra_context={~})형태로 url 처리과정에서도 정보를 넘겨 받을 수 있다.
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['dummy'] = 'dummy'
        return context


class IntroView(TemplateView):
    template_name = 'website/intro.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['dummy'] = 'dummy'
        return context


class ProductListView(ListView):
    template_name = 'website/product/list.html'
    model = Product
    context_object_name = 'product_obj_list'


class BoardListView(ListView):
    template_name = 'website/board/list.html'
    model = Board
    context_object_name = 'board_obj_list'


class BoardDetailView(DetailView):
    template_name = 'website/board/detail.html'
    model = Board
    context_object_name = 'board_obj'
    

def board_detail(request, pk):
    board_obj = get_object_or_404(Board, pk=pk)
    return render(request, 'website/board/detail.html', {'board_obj': board_obj})


def board_new(request):
    if request.method == 'POST':
        form = BoardForm(request.POST)

        if form.is_valid():
            board = form.save(commit=False)
            board.created_date = timezone.now()
            board.save()

            return redirect('board-detail', pk=board.pk)

    else:
        form = BoardForm

    return render(request, 'website/board/edit.html', {'form': form})


def board_edit(request, pk):
    board = get_object_or_404(Board, pk=pk)
    if request.method == 'POST':
        form = BoardForm(request.POST, instance=board)
        if form.is_valid():
            board = form.save(commit=False)
            board.created_date = timezone.now()
            board.save()
            return redirect('board-detail', pk=board.pk)
    else:
        form = BoardForm(instance=board)

    return render(request, 'website/board/edit.html', {'form': form})


def order(request):
    model_obj = None
    return render(request, 'website/order/index.html', {'obj': model_obj})


def faq(request):
    model_obj = None
    return render(request, 'website/faq/index.html', {'obj': model_obj})
