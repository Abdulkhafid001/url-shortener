from django.urls import path
from .views import *
urlpatterns = [

    path('v1/urls/', urls_list),

    path('v1/urls/createurl/', create_url, name='create url'),

    path('v1/urls/<str:shortcode>/', get_url, name='get url'),

    path('v1/urls/visit/<str:shortcode>/', visit_url, name='visit url'),

    path('v1/urls/edit/<str:shortcode>/', edit_url, name='edit url'),

    path('v1/urls/delete/<str:shortcode>/', delete_url, name='delete url'),

    path('v1/urls/<str:shortcode>/stats/', url_stats, name='url stats')
]
