from django.conf.urls import patterns, include, url
from django.contrib import admin
from stock.api import ProductResource

product_resource = ProductResource()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'demo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^api/', include(product_resource.urls)),
    url(r'^admin/', include(admin.site.urls)),
)
