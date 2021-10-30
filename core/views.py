from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *

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
