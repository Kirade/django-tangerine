from django import forms
from django.core.validators import EmailValidator
from .models import Order


class OrderForm(forms.ModelForm):
    PRODUCT_CHOICES = (
        ('', '상품 선택'),
        ('상품5', '상품 5kg'),
        ('상품10', '상품 10kg'),
        ('비상품5', '비상품 5kg'),
        ('비상품10', '비상품 10kg'),
    )

    product = forms.CharField(widget=forms.Select(choices=PRODUCT_CHOICES, attrs={'class': 'form-control'}))
    count = forms.IntegerField(min_value=1, widget=forms.NumberInput(attrs={'class': 'form-control',
                                                                            'placeholder': '단위 : 박스'}))
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                         'placeholder': '주문하시는 분 성함'}))
    tel = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                        'placeholder': '연락가능한 번호'}))
    address = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                            'placeholder': '배송받으실 주소'}))
    email = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control',
                                                          'placeholder': '이메일 주소',
                                                          }))

    product.label = "상품"
    product.help_text = "<small class='form-text text-muted'>상품은 한 종류씩 주문이 가능합니다.<br> 여러 종류일 경우 나누어 주문해주세요.</small>"
    count.label = "갯수"
    name.label =  "성함"
    tel.label = "전화번호"
    address.label = "주소"
    email.label = "이메일"

    class Meta:
        model = Order
        exclude = ('created_at',)