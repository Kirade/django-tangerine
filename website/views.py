from django.views.generic.base import TemplateView
from .models import Order
from django.shortcuts import render


class IndexView(TemplateView):
    template_name = 'website/index.html'

    # 넘기려고 하는 데이터를 context안에 dictionary로 넣을 수 있다.
    # as_view(extra_context={~})형태로 url 처리과정에서도 정보를 넘겨 받을 수 있다.
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['dummy'] = 'dummy'
        return context

def order_new(request):

    if request.method == 'GET':
        order = Order.objects.create(
            product=request.GET['product'],
            count=request.GET['product-count'],
            name=request.GET['recipient-name'],
            tel=request.GET['recipient-tel'],
            address=request.GET['recipient-addr'],
            email=request.GET['recipient-email']
        )

        order.save()

    else:
        order = None

    return render(request,'website/test.html', {
        'order': order
    })