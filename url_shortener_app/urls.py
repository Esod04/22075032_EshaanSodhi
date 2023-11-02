# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path("", views.shorten_url, name='shorten_url'),
    path('shorten/', views.shorten_url, name='shorten_url'),
    path('list/', views.display_short_urls, name='short_url_list'),
    path('<str:code>/', views.redirect_original_url, name='redirect_original_url'),
]
