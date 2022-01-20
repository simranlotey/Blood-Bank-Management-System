from django.urls import path
from .views import home, about, donor_registration, search, search_info, contact


urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('donor_registration/', donor_registration,
         name='donor_registration'),
    path('donor_registration/donor_list/',
         donor_registration, name='donor_list'),
    path('search/', search, name='search'),
    path('search_list/', search, name='search_list'),
    path('search/search_list/search_info/<email>/',
         search_info, name='search_info'),
    path('contact/', contact, name='contact'),
]
