from comex.models import NetworkConfig, Network
import json
import re
import collections


# TODO: handle external_interfaces and dnsmasq
def adjust_attribute(attribute):
    symbols = re.split("([A-Z][a-z]*_*[a-z]*)", attribute)
    for symbol in symbols:
        if not symbol:
            symbols.remove(symbol)

    attribute = symbols[0]
    if symbols[0] == "tunnel":
        attribute = attribute + ".NAME." + symbols[5].lower()
    else:
        for i in range(1, len(symbols)):
            attribute = attribute + "." + symbols[i].lower()

    return attribute


def create_network_json_file(network, network_config):
    net = {}
    n_config = {}
    for config, value in network_config.__dict__.items():
        if config != "_state" and config != "id":
            n_config[adjust_attribute(config)] = value

    # sort network config entries for a better layout in file
    n_config = collections.OrderedDict(sorted(n_config.items()))

    net['config'] = n_config

    for config, value in network.__dict__.items():
        if config != "_state" and config != "id":
            net[adjust_attribute(config)] = value

    # sort network entries for a better layout in file
    net = collections.OrderedDict(sorted(net.items()))
    # Write data to JSON Config File
    with open('network_configuration.json', 'w') as configuration:
        json.dump(net, configuration)

    return configuration