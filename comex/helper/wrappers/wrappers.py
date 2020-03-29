from comex.models import *


# private function to set attribute value of a network configuration object
def __set_attributes(net_config, attribute_name, attribute_value):
    """
    :param net_config:
    :param attribute_name:
    :param attribute_value:
    :return:
    """
    if attribute_value:
        setattr(net_config, attribute_name, attribute_value)


def network_wrapper(name, description):
    network = Network()
    __set_attributes(network, "name", name)
    __set_attributes(network, "description", description)

    return network


def network_config_wrapper(bridgeDriver, e_interfaces, hwaddr, mode, mtu, dns_domain, dns_mode,
                           overlay_subnet, fan_type, underlay, v4addr, v4dhcp, v4dhcp_expiry,
                           v4dhcp_gateway, v4dhcp_ranges, v4firewall, v4nat, v4nat_order, v4nat_address,
                           v4routes, v4routing, v6addr, v6dhcp, v6dhcp_expiry, v6dhcp_ranges,
                           v6dhcp_stateful, v6firewall, v6nat, v6nat_order, v6nat_address, v6routes,
                           v6routing, raw_dnsmasq, group, id, interface, local, port, protocol,
                           remote, ttl):
    network_config = NetworkConfig()

    __set_attributes(network_config, "bridgeDriver", bridgeDriver)
    __set_attributes(network_config, "bridgeExternal_interfaces", e_interfaces)
    __set_attributes(network_config, "bridgeHwaddr", hwaddr)
    __set_attributes(network_config, "bridgeMode", mode)
    __set_attributes(network_config, "bridgeMtu", mtu)
    __set_attributes(network_config, "dnsDomain", dns_domain)
    __set_attributes(network_config, "dnsMode", dns_mode)
    __set_attributes(network_config, "fanOverlay_subnet", overlay_subnet)
    __set_attributes(network_config, "fanType", fan_type)
    __set_attributes(network_config, "fanUnderlay_subnet", underlay)
    __set_attributes(network_config, "ipv4Address", v4addr)
    __set_attributes(network_config, "ipv4Dhcp", v4dhcp)
    __set_attributes(network_config, "ipv4DhcpExpiry", v4dhcp_expiry)
    __set_attributes(network_config, "ipv4DhcpGateway", v4dhcp_gateway)
    __set_attributes(network_config, "ipv4DhcpRanges", v4dhcp_ranges)
    __set_attributes(network_config, "ipv4Firewall", v4firewall)
    __set_attributes(network_config, "ipv4Nat", v4nat)
    __set_attributes(network_config, "ipv4NatOrder", v4nat_order)
    __set_attributes(network_config, "ipv4NatAddress", v4nat_address)
    __set_attributes(network_config, "ipv4Routes", v4routes)
    __set_attributes(network_config, "ipv4Routing", v4routing)
    __set_attributes(network_config, "ipv6Address", v6addr)
    __set_attributes(network_config, "ipv6Dhcp", v6dhcp)
    __set_attributes(network_config, "ipv6DhcpExpiry", v6dhcp_expiry)
    #__set_attributes(network_config, "ipv6DhcpStateful", v6dhcp_ranges)
    __set_attributes(network_config, "ipv6DhcpStateful", v6dhcp_stateful)
    __set_attributes(network_config, "ipv6Firewall", v6firewall)
    __set_attributes(network_config, "ipv6Nat", v6nat)
    __set_attributes(network_config, "ipv6NatOrder", v6nat_order)
    __set_attributes(network_config, "ipv6NatAddress", v6nat_address)
    __set_attributes(network_config, "ipv6Routes", v6routes)
    __set_attributes(network_config, "ipv6Routing", v6routing)
    __set_attributes(network_config, "rawDnsMasq", raw_dnsmasq)
    __set_attributes(network_config, "tunnelNAMEGroup", group)
    __set_attributes(network_config, "tunnelNAMEId", id)
    __set_attributes(network_config, "tunnelNAMEInterface", interface)
    __set_attributes(network_config, "tunnelNAMELocal", local)
    __set_attributes(network_config, "tunnelNAMEPort", port)
    __set_attributes(network_config, "tunnelNAMEProtocol", protocol)
    __set_attributes(network_config, "tunnelNAMERemote", remote)
    __set_attributes(network_config, "tunnelNAMETtl", ttl)

    return network_config
