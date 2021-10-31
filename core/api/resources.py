from tastypie.resources import ModelResource,  ALL_WITH_RELATIONS
from tastypie import fields
from core.models import Order, Material, Vendor, OrderItem


class VendorResource(ModelResource):
    class Meta:
        queryset = Vendor.objects.all()
        allowed_methods = ['get']

class MaterialResource(ModelResource):
    vendor = fields.ForeignKey(VendorResource, 'vendor', full=True)
    class Meta:
        queryset = Material.objects.all()
        allowed_methods = ['get']
        filtering = {'vendor':ALL_WITH_RELATIONS}

class OrderItemResource(ModelResource):
    material = fields.ForeignKey(MaterialResource, 'material', full=True)
    total = fields.CharField(attribute='total', readonly=True)

    class Meta:
        queryset = OrderItem.objects.all()
        allowed_methods = ['get']


class OrderResource(ModelResource):
    items = fields.ToManyField(OrderItemResource, 'items', full=True)
    total = fields.CharField(attribute='total', readonly=True)

    class Meta:
        queryset = Order.objects.all()
        allowed_methods = ['get','post']
