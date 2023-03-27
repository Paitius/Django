from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('shorten', views.shorten, name='shorten'),
    path('<hash>', views.redirect_go_to, name='redirect_go_to'),
]
