from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.product_list, name='product_list'),
    url(r'^(?P<category_slug>[-\w]+)/$', views.product_list, name='product_list_by_category'),
    url(r'^(?P<pid>\d+)/(?P<slug>[-\w]+)/$', views.product_detail, name='product_details'),
    url(r'^result$', views.SearchList, name='search_list'),
    url(r'^advresult$', views.AdvSearchList, name='avcsearch_list'),
    url(r'^(?P<action>[-\w]+)/(?P<Cat_slug>[-\w]+)/(?P<comm>[-\w]+)/$', views.list_vide, name='list_by_category'),
    url(r'^vendre$', views.vendreUnBien, name='vendrebien'),
    url(r'^prestation$', views.nosprestation, name='prestation'),
    url(r'^contact$', views.contacteznous, name='contact'),
    url(r'^search$', views.search, name='search'),
    url(r'^vendeur$', views.vendorform, name='vendeur'),
    url(r'^creation/vendeur/', views.VendorCreate.as_view(), name='creation_vendeur'),
    url(r'^vendeur/(?P<pk>\d+)$', views.VendorDetailView.as_view(), name='vendor-detail'),
]