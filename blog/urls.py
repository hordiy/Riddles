from django.urls import path
from .views import *

urlpatterns = [
    path('', posts_list, name='posts_list_url'),
    path('загадки/create/', PostCreate.as_view(), name='post_create_url'),
    path('загадки/<str:slug>/', PostDetail.as_view(), name='post_detail_url'),
    path('загадки/<str:slug>/update/', PostUpdate.as_view(), name='post_update_url'),
    path('загадки/<str:slug>/delete/', PostDelete.as_view(), name='post_delete_url'),
    path('категории/', categories_list, name='categories_list_url'),
    path('категории/create/', CategoryCreate.as_view(), name='category_create_url'),
    path('категории/<str:slug>/', CategoryDetail.as_view(), name='category_detail_url'),
    path('категории/<str:slug>/update/', CategoryUpdate.as_view(), name='category_update_url'),
    path('категории/<str:slug>/delete/', CategoryDelete.as_view(), name='category_delete_url')
]
