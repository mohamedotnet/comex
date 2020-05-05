from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('home', views.index, name="index"),
    path('create.network', views.create_network, name="create_network"),
    path('modify.network/<int:network_id/>', views.modify_network, name="modify_network"),
    path('networks', views.networks, name="networks"),
    path('connect.container', views.containers, name="containers"),
    path('containers', views.containers, name="containers"),
    path('containers/<slug:container_name>', views.connect_container, name="connect_container")
]
