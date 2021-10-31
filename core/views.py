from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *
from .tasks import *
# Create your views here.
class VendorView(LoginRequiredMixin,View):
    '''
    View for managing a vendor's orders
    '''
    template_name = "./vendor.html"

    def get(self, request, *args, **kwargs):
        context ={}
        orders = Order.objects.filter(vendor=request.user.vendor)
        vendors = Vendor.objects.all()
        context['orders'] = orders
        context['vendors'] = vendors
        return render(request, self.template_name, context)


class OrderView(LoginRequiredMixin,View):
    '''
    View for creating an order
    '''
    template_name = "./order.html"

    def get(self, request, *args, **kwargs):
        context ={}
        materials = Material.objects.filter(vendor=request.user.vendor)
        vendors = Vendor.objects.all()
        context['materials'] = materials
        context['vendors'] = vendors
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        context ={}
        materials = []
        for item in request.POST:
            #Build Order materials
            if item.startswith('material_'):
                materials.append( (item.split('_')[1],request.POST.get(item)))
        vendor = Vendor.objects.get(id=request.POST.get('vendor'))
        order = Order.objects.create(
            vendor=vendor,
            placed_by=request.user,
            delivery_date=request.POST.get('delivery_date'),
            comment=request.POST.get('comment')
        )
        for item in materials:
            material = Material.objects.get(id=item[0])
            order_item = OrderItem.objects.create(
                material=material,
                quantity=item[1],
                )
            order.items.add(order_item)
        order.save()
        send_order_confirmation_email(order)
        return redirect('vendor')
