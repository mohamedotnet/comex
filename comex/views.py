from django.shortcuts import render, redirect
from comex.helper import wrappers
from comex.helper.generators import JSONGenerator


def index(request):
    # Reminder: Every variable here is accessed in the corresponding template through context subscription
    return render(request, 'comex/index.html')


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
        config_file = JSONGenerator.create_network_json_file(net, net_config)
        # parse the configuration file + validation
        # config_file_parser.parse_network_config_file(config_file)
        # create the network

        # call the creation function with 'configFile'
        return redirect(index)

    return render(request, 'comex/createNetwork.html')


def modify_network(request, network_id):
    pass


def list_networks(request):
    pass


def assign_container(request):
    pass


def post_network(request):
    return render(request, 'comex/index.html')
