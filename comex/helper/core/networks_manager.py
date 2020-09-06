import json
from pylxd import Client
from comex.helper.parsers.config_file_parser import parse_configuration_file, network_info_parser


def create_network_lxd(client, config_file):
    """
    Wrapper of create network API - lxd
    :param client:
    :param config_file:
    :return:
    """
    name = network_info_parser(config_file)[0]
    description = network_info_parser(config_file)[1]
    configuration = parse_configuration_file(config_file)

    if not description and len(configuration) == 0:
        client.networks.create(name)

    elif description and len(configuration) == 0:
        client.networks.create(name, description=description)

    else:
        client.networks.create(name, description=description, config=configuration)


def all_networks_lxd(client):
    """
    List all networks
    :param client:
    :return:
    """
    return client.networks.all()


def all_network(client):
    networks = []
    for n in all_networks_lxd(client):
        if n.type == 'bridge':
            networks.append(n.name)

    return networks


#print(all_network(Client()))