from django.urls import path, register_converter
from . import views
from . import converters

register_converter(converters.FloatUrlConverter, 'float')

urlpatterns = [
    path('', views.index, name='index'),
    path('imperial/<lbs>/<inch>', views.imperial, name='imperial'),
    path('metric/<float:kg>/<float:meters>', views.metric, name='metric'),
    path('<metric_system>/<float:weight>/<float:height>',
         views.metric_all, name='metric_all'),

]
