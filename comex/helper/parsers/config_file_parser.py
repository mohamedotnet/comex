import json


def __is_default_configuration(configuration):
    if configuration['bridge.driver'] != "native" or configuration['bridge.external_interfaces'] != "" \
            or configuration['bridge.hwaddr'] != "" or configuration['bridge.mode'] != "standard" \
            or configuration['bridge.mtu'] != 1500 or configuration['dns.domain'] != "lxd" \
            or configuration['dns.mode'] != "managed" or configuration['fan.overlay_subnet'] != "240.0.0.0/8" \
            or configuration['fan.type'] != "vxlan" or configuration['fan.underlay_subnet'] != "" \
            or configuration['ipv4.address'] != "" or not configuration['ipv4.dhcp'] \
            or configuration['ipv4.dhcp.expiry'] != "1h" or configuration['ipv4.dhcp.gateway'] != "" \
            or configuration['ipv4.dhcp.ranges'] != "" or not configuration['ipv4.firewall'] \
            or configuration['ipv4.nat'] or configuration['ipv4.nat.order'] != "before" \
            or configuration['ipv4.nat.address'] != "" or configuration['ipv4.routes'] != "" \
            or not configuration['ipv4.routing'] \
            or configuration['ipv6.address'] != "" or not configuration['ipv6.dhcp'] \
            or configuration['ipv6.dhcp.expiry'] != "1h" or configuration['ipv6.dhcp.ranges'] != "" \
            or configuration['ipv6.dhcp.stateful'] or not configuration['ipv6.firewall'] \
            or configuration['ipv6.nat'] or configuration['ipv6.nat.order'] != "before" \
            or configuration['ipv6.nat.address'] != "" or configuration['ipv6.routes'] != "" \
            or not configuration['ipv6.routing'] \
            or configuration['raw.dnsmasq'] != "" or configuration['tunnel.NAME.group'] != "239.0.0.1" \
            or configuration['tunnel.NAME.id'] != 0 or configuration['tunnel.NAME.interface'] != "" \
            or configuration['tunnel.NAME.local'] != "" or configuration['tunnel.NAME.port'] != 0 \
            or configuration['tunnel.NAME.protocol'] != "" or configuration['tunnel.NAME.remote'] != "" \
            or configuration['tunnel.NAME.ttl'] != 1:
        print("default")
        return False

    return True


def __default_bridge(bridge_config):
    br_conf = {}

    if bridge_config['bridge.driver'] != "native":
        br_conf['bridge.driver'] = bridge_config['bridge.driver']

    if bridge_config['bridge.external_interfaces'] != "":
        br_conf['bridge.external_interfaces'] = bridge_config['bridge.external_interfaces']

    if bridge_config['bridge.hwaddr'] != "":
        br_conf['bridge.hwaddr'] = bridge_config['bridge.hwaddr']

    if bridge_config['bridge.mode'] != "standard":
        br_conf['bridge.mode'] = bridge_config['bridge.mode']

    if bridge_config['bridge.mtu'] != 1500:
        br_conf['bridge.mtu'] = bridge_config['bridge.mtu']

    return br_conf


def __default_dns(dns_config):
    dns_conf = {}

    if dns_config['dns.domain'] != "lxd":
        dns_conf['dns.domain'] = dns_config['dns.domain']

    if dns_config['dns.mode'] != "":
        dns_conf['dns.mode'] = dns_config['dns.mode']

    return dns_conf


def __default_fan(fan_config):
    fan_conf = {}

    if fan_config['fan.overlay_subnet'] != "240.0.0.0/8":
        fan_conf['fan.overlay_subnet'] = fan_config['fan.overlay_subnet']

    if fan_config['fan.type'] != "vxlan":
        fan_conf['fan.type'] = fan_config['fan.type']

    if fan_config['fan.underlay_subnet'] != "":
        fan_conf['fan.underlay_subnet'] = fan_config['fan.underlay_subnet']

    return fan_conf


def __default_ipv4(ipv4_config):
    ipv4_conf = {}

    if ipv4_config['ipv4.address'] != "":
        ipv4_conf['ipv4.address'] = ipv4_config['ipv4.address']

    if not ipv4_config['ipv4.dhcp']:
        ipv4_conf['ipv4.dhcp'] = ipv4_config['ipv4.dhcp']

    if ipv4_config['ipv4.dhcp.expiry'] != "1h":
        ipv4_conf['ipv4.dhcp.expiry'] = ipv4_config['ipv4.dhcp.expiry']

    if ipv4_config['ipv4.dhcp.gateway'] != "":
        ipv4_conf['ipv4.dhcp.gateway'] = ipv4_config['ipv4.dhcp.gateway']

    if ipv4_config['ipv4.dhcp.ranges'] != "":
        ipv4_conf['ipv4.dhcp.ranges'] = ipv4_config['ipv4.dhcp.ranges']

    if not ipv4_config['ipv4.firewall']:
        ipv4_conf['ipv4.firewall'] = ipv4_config['ipv4.firewall']

    if ipv4_config['ipv4.nat']:
        ipv4_conf['ipv4.nat'] = ipv4_config['ipv4.nat']

    if ipv4_config['ipv4.nat.order'] != "before":
        ipv4_conf['ipv4.nat.order'] = ipv4_config['ipv4.nat.order']

    if ipv4_config['ipv4.nat.address'] != "":
        ipv4_conf['ipv4.nat.address'] = ipv4_config['ipv4.nat.address']

    if ipv4_config['ipv4.routes'] != "":
        ipv4_conf['ipv4.routes'] = ipv4_config['ipv4.routes']

    if not ipv4_config['ipv4.routing']:
        ipv4_conf['ipv4.routing'] = ipv4_config['ipv4.routing']

    return ipv4_conf


def __default_ipv6(ipv6_config):
    ipv6_conf = {}

    if ipv6_config['ipv6.address'] != "":
        ipv6_conf['ipv6.address'] = ipv6_config['ipv6.address']

    if not ipv6_config['ipv6.dhcp']:
        ipv6_conf['ipv6.dhcp'] = ipv6_config['ipv6.dhcp']

    if ipv6_config['ipv6.dhcp.expiry'] != "1h":
        ipv6_conf['ipv6.dhcp.expiry'] = ipv6_config['ipv6.dhcp.expiry']

    if ipv6_config['ipv6.dhcp.ranges'] != "":
        ipv6_conf['ipv6.dhcp.ranges'] = ipv6_config['ipv6.dhcp.ranges']

    if ipv6_config['ipv6.dhcp.stateful']:
        ipv6_conf['ipv6.stateful'] = ipv6_config['ipv6.stateful']

    if not ipv6_config['ipv6.firewall']:
        ipv6_conf['ipv6.firewall'] = ipv6_config['ipv6.firewall']

    if ipv6_config['ipv6.nat']:
        ipv6_conf['ipv6.nat'] = ipv6_config['ipv6.nat']

    if ipv6_config['ipv6.nat.order'] != "before":
        ipv6_conf['ipv6.nat.order'] = ipv6_config['ipv6.nat.order']

    if ipv6_config['ipv6.nat.address'] != "":
        ipv6_conf['ipv6.nat.address'] = ipv6_config['ipv6.nat.address']

    if ipv6_config['ipv4.routes'] != "":
        ipv6_conf['ipv4.routes'] = ipv6_config['ipv6.routes']

    if not ipv6_config['ipv6.routing']:
        ipv6_conf['ipv6.routing'] = ipv6_config['ipv6.routing']

    return ipv6_conf


def __default_tunnel(tunnel_config):
    tunnel_conf = {}

    if tunnel_config['tunnel.NAME.group'] != "239.0.0.1":
        tunnel_conf['tunnel.NAME.group'] = tunnel_config['tunnel.NAME.group']

    if tunnel_config['tunnel.NAME.id'] != 0:
        tunnel_conf['tunnel.NAME.id'] = tunnel_config['tunnel.NAME.id']

    if tunnel_config['tunnel.NAME.interface'] != "":
        tunnel_conf['tunnel.NAME.interface'] = tunnel_config['tunnel.NAME.interface']

    if tunnel_config['tunnel.NAME.local'] != "":
        tunnel_conf['tunnel.NAME.local'] = tunnel_config['tunnel.NAME.local']

    if tunnel_config['tunnel.NAME.port'] != 0:
        tunnel_conf['tunnel.NAME.port'] = tunnel_config['tunnel.NAME.port']

    if tunnel_config['tunnel.NAME.protocol'] != "":
        tunnel_conf['tunnel.NAME.protocol'] = tunnel_config['tunnel.NAME.protocol']

    if tunnel_config['tunnel.NAME.remote'] != "":
        tunnel_conf['tunnel.NAME.remote'] = tunnel_config['tunnel.NAME.remote']

    if tunnel_config['tunnel.NAME.ttl'] != 1:
        tunnel_conf['tunnel.NAME.ttl'] = tunnel_config['tunnel.NAME.ttl']

    return tunnel_conf


def __default_raw(raw_config):
    raw_conf = {}

    if raw_config['raw.dnsmasq'] != "":
        raw_conf['raw.dnsmasq'] = raw_config['raw.dnsmasq']

    return raw_conf


def parse_configuration_file(config_map):
    network = config_map
    verbose_config = network['config']

    configuration = {}

    if not __is_default_configuration(verbose_config):
        if len(__default_bridge(verbose_config)) != 0:
            configuration.update(__default_bridge(verbose_config))

        if len(__default_dns(verbose_config)) != 0:
            configuration.update(__default_dns(verbose_config))

        if len(__default_fan(verbose_config)) != 0:
            configuration.update(__default_fan(verbose_config))

        if len(__default_ipv4(verbose_config)) != 0:
            configuration.update(__default_ipv4(verbose_config))

        if len(__default_ipv6(verbose_config)) != 0:
            configuration.update(__default_ipv4(verbose_config))

        if len(__default_raw(verbose_config)) != 0:
            configuration.update(__default_raw(verbose_config))

        if len(__default_tunnel(verbose_config)) != 0:
            configuration.update(__default_tunnel(verbose_config))

    return configuration


def network_info_parser(config_map):
    return config_map['name'], config_map['description']