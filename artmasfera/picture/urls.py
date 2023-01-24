from django.urls import path

from .views import *

urlpatterns = [
    path('', home_i, name='home'),                                                      #http://127.0.0.1:8000/
    path('gallery/vzrosly/', MasterClassAdults.as_view(), name='big_mk'),               #http://127.0.0.1:8000/gallery/vzrosly/
    path('gallery/detski/', MasterClassKids.as_view(), name='little_mk'),               #http://127.0.0.1:8000/gallery/detski/
    path('about/', about, name='about'),                                                #http://127.0.0.1:8000/about/
    path('sertificates/', sertificates, name='sertificates'),                           #http://127.0.0.1:8000/sertificates/
    path('corporate/', corporate, name='corporate'),                                    #http://127.0.0.1:8000/corporate/
    path('contacts/', contacts, name='contacts'),                                       #http://127.0.0.1:8000/contacts/
    path('partners/', partners, name='partners'),                                       #http://127.0.0.1:8000/contacts/
    path('legal/', legal, name='legal'),                                                #http://127.0.0.1:8000/contacts/
    path('form_writer/<int:ip_mk>/<int:ip_pict>/', form_writer, name='form_writer'),    #http://127.0.0.1:8000/form_write/
    path('gallery_picture/<int:ip_mk>/', gallery_picture, name='gallery_picture'),      #http://127.0.0.1:8000/gallery/
    path('price_list/', price_list, name='price_list'),                                 #http://127.0.0.1:8000/gallery/
    path('stories/', stories, name='stories'),
    path('redirect_s/', redirect_s, name='redirect_s')
]
