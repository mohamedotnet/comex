from django.shortcuts import render, redirect
from comex.helper.wrappers import wrappers
from comex.helper.generators import JSONGenerator
from pylxd import Client
from comex.helper.core.networks_manager import create_network_lxd, all_networks_lxd
from comex.helper.core.containers_manager import *

import json

client = Client()


def index(request):
    all_networks = all_networks_lxd(client)
    #print(connected_containers(client))
    context = {"networks" : all_networks, "connected_containers" : json.dumps(connected_containers(client))}
    return render(request, 'comex/index.html', context=context)


def create_network(request):
    if request.method == "POST":
        net = wrappers.network_wrapper(request.POST.get("netname"), request.POST.get("netdesc"))
        net_config = wrappers.network_config_wrapper(request.POST.get("bridge_driver"),
                                                     request.POST.get("e_interfaces"),
                                                     request.POST.get("hwaddr"),
                                                     request.POST.get("driver_mode"),
                                                     request.POST.get("mtu"),
                                                     request.POST.get("dnsdomain"),
                                                     request.POST.get("dnsmode"),
                                                     request.POST.get("overlay"),
                                                     request.POST.get("fantype"),
                                                     request.POST.get("underlay"),
                                                     request.POST.get("v4addr"),
                                                     True if request.POST.get("v4dhcp") == "on" else False,
                                                     request.POST.get("v4dhcp_expiry"),
                                                     request.POST.get("v4dhcp_gateway"),
                                                     request.POST.get("v4dhcp_ranges"),
                                                     True if request.POST.get("v4firewall") == "on" else False,
                                                     True if request.POST.get("v4nat") == "on" else False,
                                                     request.POST.get("v4nat_order"),
                                                     request.POST.get("v4nataddr"),
                                                     request.POST.get("v4routes"),
                                                     True if request.POST.get("v4routing") == "on" else False,
                                                     request.POST.get("v6addr"),
                                                     True if request.POST.get("v6dhcp") == "on" else False,
                                                     request.POST.get("v6dhcp_expiry"),
                                                     request.POST.get("v6dhcp_ranges"),
                                                     True if request.POST.get("v6dhcp_stateful") == "on" else False,
                                                     True if request.POST.get("v6firewall") == "on" else False,
                                                     True if request.POST.get("v6nat") == "on" else False,
                                                     request.POST.get("v6nat_order"),
                                                     request.POST.get("v6nataddr"),
                                                     request.POST.get("v6routes"),
                                                     True if request.POST.get("v6routing") == "on" else False,
                                                     request.POST.get("raw_dnsmasq"),
                                                     request.POST.get("group"),
                                                     request.POST.get("id"),
                                                     request.POST.get("interface"),
                                                     request.POST.get("local"),
                                                     request.POST.get("port"),
                                                     request.POST.get("protocol"),
                                                     request.POST.get("remote"),
                                                     request.POST.get("ttl"))

        # generate configuration file
        config_map = JSONGenerator.generate_network_json_file(net, net_config)
        # TODO: validate the network json file and send feedback in case of anomaly
        # validation code goes here
        # Create the network if no anomaly
        create_network_lxd(client, config_map)
        # TODO: add success attribute to context
        return redirect(index)

    return render(request, 'comex/createNetwork.html')


def modify_network(request):
    pass


def networks(request):
    all_networks = all_networks_lxd(client)
    context = {'networks': all_networks}
    return render(request, 'comex/networks.html', context=context)


def containers(request):
    all_containers = all_containers_lxd(client)
    context = {'containers': all_containers}
    return render(request, 'comex/containers.html', context=context)


#<input type="hidden" name="container_name" value="{{ container.name }}">
def connect_container(request, container_name):
    container = get_container(client, container_name)
    if request.method == "GET":
        context = {'container': container,
                   'container_network': get_container_networks(client, container_name),
                   'networks': all_networks_lxd(client)}
        return render(request, 'comex/connectContainer.html', context=context)
    else:
        # TODO: Generate device dictionnary
        # {'net0': {'ipv4.address': '196.1.1.5', 'name': 'int0', 'nictype': 'bridged', 'parent': 'lokmach', 'type': 'nic'}}
        device = JSONGenerator.create_network_device(request.POST.get("name"),
                                                     request.POST.get("network"))

        connect_to_network_lxd(container, device)
        return redirect(connect_container, container_name=container_name)