from pylxd import Client
from comex.helper.core import networks_manager


def get_container(client, container_name):
    return client.containers.get(container_name)


def all_containers_lxd(client):
    return client.containers.all()


def connect_to_network_lxd(container, device):
    # TODO: test if it is already connected to this network
    container.devices.update(device)
    container.save()


def get_container_networks(client, container_name):
    networks = {}
    container = get_container(client, container_name)
    for key, value in container.devices.items():
        if value['type'] == 'nic':
            networks[key] = container.devices.get(key)

    return networks


def get_container_networks_list(client, container_name):
    network = []
    for n in get_container_networks(client, container_name).keys():
        network.append(get_container_networks(client, container_name).get(n).get('parent'))

    return network


def connected_containers(client):
    all_networks = networks_manager.all_network(client)
    networks = {}
    for n in all_networks:
        networks[n] = []

    for container in all_containers_lxd(client):
        for network in get_container_networks_list(client, container.name):
            networks[network].append(container.name)

    return networks


print(connected_containers(Client()))
#print("results: ", get_container_networks_list(Client(), 'cmx'))



