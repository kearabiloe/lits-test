"""lits_demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from core.views import *
from tastypie.api import Api
from core.api.resources import OrderResource, MaterialResource, VendorResource
from django.contrib.auth.views import LoginView

v1_api = Api(api_name='v1')
v1_api.register(VendorResource())
v1_api.register(OrderResource())
v1_api.register(MaterialResource())

urlpatterns = [
    path('admin/', admin.site.urls),
    path('vendor/', VendorView.as_view(), name="vendor"),
    path('order/', OrderView.as_view(), name="order"),
    path('login/', LoginView.as_view(
        template_name='admin/login.html',
        extra_context={'site_header': 'LITS',}), name="login"
    ),
    path('api/', include(v1_api.urls)),
    path('', OrderView.as_view(), name="home"),
]
#Work around for serving media files localy
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
