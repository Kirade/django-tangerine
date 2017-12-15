from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from .forms import RegisterForm, MyPageForm
from .models import Board, Product, Profile


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
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['range'] = range(1,10)
        return context


class BoardDetailView(DetailView):
    template_name = 'website/board/detail.html'
    model = Board
    context_object_name = 'board_obj'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs['pk']
        current_board_hit = Board.objects.get(id=pk)
        Board.objects.filter(id=pk).update(hit=current_board_hit.hit + 1)
        return context


class BoardCreateView(CreateView):
    template_name = 'website/board/new.html'
    model = Board
    fields = ['title', 'writer', 'text', ]
    success_url = reverse_lazy('board-list')

    @method_decorator(login_required())
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class BoardUpdateView(UpdateView):
    template_name = 'website/board/edit.html'
    model = Board
    fields = ['title', 'writer', 'text', ]
    success_url = '/board/'


class OrderView(TemplateView):
    template_name = 'website/order/index.html'


class FaqView(TemplateView):
    template_name = 'website/faq/index.html'


class RegisterView(CreateView):
    template_name='website/registration/register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('login')


class UserChangeView(UpdateView):
    template_name='website/registration/mypage.html'
    model = User
    form_class = MyPageForm
    success_url = reverse_lazy('change_success')

    def get_initial(self):
        obj = self.get_object()
        profile = Profile.objects.get(user_id=obj.id)
        initial = {'full_name': profile.full_name, 'address': profile.address, 'phone_number': profile.phone_number}
        return initial


class ChangeSuccessView(TemplateView):
    template_name = 'website/registration/change_success.html'