from django.views.generic.base import TemplateView
from django.shortcuts import render
from django.core.exceptions import ValidationError
from .forms import OrderForm




class IndexView(TemplateView):
    template_name = 'website/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = OrderForm()
        return context

def order_new(request):

    if request.method == 'POST':
        form = OrderForm(request.POST)

        if form.is_valid():
            form.save()
            return render(request, 'website/order_success.html')
        else:
            raise ValidationError('Invalid Form')

    else:
        form = OrderForm()

    return render(request, 'website/order_success.html', {
        'form': form
    })