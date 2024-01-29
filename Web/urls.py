from django.urls import path, re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    re_path(r'^(?P<country_code>in)/$', views.home, name='home'),

    path('group-tours/', views.group_tours, name='group-tours'),
    re_path(r'^(?P<country_code>in)/group-tours/$', views.group_tours, name='group-tours'),

    path('view-group-tour/<str:group_tour_id>/', views.view_group_tour_default, name='view-group-tour-default'),
    re_path(r'^(?P<country_code>in)/view-group-tour/(?P<group_tour_id>\w+)/$', views.view_group_tour_region, name='view-group-tour-region'),

    path('get-price/<str:country_code>', views.get_price, name='get-price'),
    path('booking-payment/<str:booking_id>/', views.booking_payment, name='booking-payment'),

    path('iwa-group-of-companies/', views.iwa_group_of_companies, name='iwa-group-of-companies'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

