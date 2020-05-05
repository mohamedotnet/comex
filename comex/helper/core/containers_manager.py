def get_container(client, container_name):
    return client.containers.get(container_name)


def all_containers_lxd(client):
    return client.containers.all()


def connect_to_network_lxd(client, container_name, device):
    container = client.containers.get(container_name)
    # TODO: test if it is already connected to this network
    container.devices.update(device)


def get_container_networks(client, container_name):
    networks = {}
    container = get_container(client, container_name)
    for key, value in container.devices.items():
        if value['type'] == 'nic':
            networks[key] = container.devices.get(key)

    return networks