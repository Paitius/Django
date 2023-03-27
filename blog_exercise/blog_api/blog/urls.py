from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('user', views.UserList.as_view(), name='user_list'),
    path('user/<int:pk>', views.UserData.as_view(), name='user_data'),
    path('post', views.PostList.as_view(), name='post_list'),
    path('post/<int:pk>', views.PostData.as_view(), name='post_data'),
]
