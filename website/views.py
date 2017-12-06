from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView

from .models import Board, Product


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


class BoardCreateView(CreateView):
    template_name = 'website/board/edit.html'
    model = Board
    fields = ['title', 'text', ]
    success_url = '/board/'


class BoardUpdateView(UpdateView):
    template_name = 'website/board/edit.html'
    model = Board
    fields = ['title', 'text', ]
    success_url = '/board/'


class OrderView(TemplateView):
    template_name = 'website/order/index.html'


class FaqView(TemplateView):
    template_name = 'website/faq/index.html'
