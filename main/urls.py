from django.conf.urls import url
from . import views

app_name = 'main'

urlpatterns = [
    url(r'^home/', views.index, name='index'),    # Home page
    url(r'e-market/$', views.emarket, name = 'emarket'),     # rain water 
    url(r'e-market/add-eShop/$', views.AddShop.as_view(), name = 'add-shop'),   # Add an E shop
    url(r'incubators/(?P<incubator_id>[0-9]+)/', views.details, name = 'details'),
    url(r'location/', views.location, name = 'location'),           #  map
    url(r'added/', views.added, name = 'added'),      #your incubator will be added soon page
    url(r'results', views.result, name = 'result'),         # For search function
    url(r'water-footprint/$', views.footprint, name = 'footprint'),
    url(r'underground-water-data/$', views.data, name = 'data'),    # ground water data from ISRO
    url(r'join-movement/$', views.join, name = 'join'),           #for the societies.
    url(r'add-movement/', views.Add.as_view(), name = 'add'),
    url(r'discover/$', views.discover, name = 'discover'),
    url(r'discover/(?P<discover_id>[0-9]+)', views.disc_details, name = 'disc-details'),    # 
    url(r'add-discover/$', views.AddDiscover.as_view(), name = 'add-discover'),
    url(r'contact/$', views.ContactForm.as_view(), name = 'contact-form'),

]

    