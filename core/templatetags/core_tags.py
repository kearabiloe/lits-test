from django import template
from decimal import Decimal
from django.db.models import Sum
from core.models import *
register = template.Library()


@register.simple_tag
def calculate_vat(amount, vat=0.15, exclusive=False):
    amount = float(amount)
    vat = amount*vat
    results = Decimal(vat)
    if exclusive:
        results = Decimal(amount-vat)
    return Decimal("{:.2f}". format(results))

@register.simple_tag
def sum_orders(orders, single=False, items=False):
    amount = 0
    if single:
        # Got a single order instance
        orders = Order.objects.filter(id=orders.id)
    if items:
        #Calculate aggregate items__quantity
        count = orders.aggregate(Sum('items__quantity'))
        return count.get('items__quantity__sum')
    for order in orders:
        amount += order.total
    return Decimal("{:.2f}". format(amount))
