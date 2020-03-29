from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('home', views.index, name="index"),
    path('create.network', views.create_network, name="create_network"),
    path('modify.network/<int:network_id/>', views.modify_network, name="modify_network"),
    path('list.networks', views.list_networks, name="list_networks"),
    path('assign.container', views.assign_container, name="assign_container"),
    # path('post_network', views.post_network, name="post_network")
]
