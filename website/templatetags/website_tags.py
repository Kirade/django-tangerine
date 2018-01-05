from django import template

register = template.Library()


@register.filter
def get_dictionary_value(dictionary, key):
    return dictionary.get(key)


@register.filter
def comma_separator(price):
    price = str(price)
    str_price = str()
    for i in range(1, len(price) + 1):
        if i % 3 == 0:
            str_price = price[:-i] + ',' + price[-i:]
    return str_price
