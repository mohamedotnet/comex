from django.db import models
# from djangotoolbox.fields import ListField


# Config Models
class NetworkConfig(models.Model):
    # Bridge Config
    bridgeDriver = models.CharField(max_length=30, default='native')
    bridgeExternal_interfaces = models.CharField(max_length=30, default='')
    bridgeHwaddr = models.CharField(max_length=30, default='')
    bridgeMode = models.CharField(max_length=30, default='standard')
    bridgeMtu = models.IntegerField(default=1500)
    # DNS Config
    dnsDomain = models.CharField(max_length=30, default='lxd')
    dnsMode = models.CharField(max_length=30, default='managed')
    # Fan Config
    fanOverlay_subnet = models.CharField(max_length=30, default='240.0.0.0/8')
    fanType = models.CharField(max_length=30, default='vxlan')
    fanUnderlay_subnet = models.CharField(max_length=30, default='')
    # ipv4 Config
    ipv4Address = models.CharField(max_length=30, default='')
    ipv4Dhcp = models.BooleanField(default=True)
    ipv4DhcpExpiry = models.CharField(max_length=30, default='1h')
    ipv4DhcpGateway = models.CharField(max_length=30, default='')
    ipv4DhcpRanges = models.CharField(max_length=30, default='')
    ipv4Firewall = models.BooleanField(default=True)
    ipv4Nat = models.BooleanField(default=False)
    ipv4NatOrder = models.CharField(max_length=30, default='before')
    ipv4NatAddress = models.CharField(max_length=30, default='')
    ipv4Routes = models.CharField(max_length=30, default='')
    ipv4Routing = models.BooleanField(default=True)
    # ipv6 Config
    ipv6Address = models.CharField(max_length=30, default='')
    ipv6Dhcp = models.BooleanField(default=True)
    ipv6DhcpExpiry = models.CharField(max_length=30, default='1h')
    ipv6DhcpRanges = models.CharField(max_length=30, default='')
    ipv6DhcpStateful = models.BooleanField(default=False)
    ipv6Firewall = models.BooleanField(default=True)
    ipv6Nat = models.BooleanField(default=False)
    ipv6NatOrder = models.CharField(max_length=30, default='before')
    ipv6NatAddress = models.CharField(max_length=30, default='')
    ipv6Routes = models.CharField(max_length=30, default='')
    ipv6Routing = models.BooleanField(default=True)
    # Raw Config
    rawDnsmasq = models.CharField(max_length=30, default='')
    # Tunnel Config
    tunnelNAMEGroup = models.CharField(max_length=30, default='239.0.0.1')
    tunnelNAMEId = models.IntegerField(default=0)
    tunnelNAMEInterface = models.CharField(max_length=30, default='')
    tunnelNAMELocal = models.CharField(max_length=30, default='')
    tunnelNAMEPort = models.IntegerField(default=0)
    tunnelNAMEProtocol = models.CharField(max_length=30, default='')
    tunnelNAMERemote = models.CharField(max_length=30, default='')
    tunnelNAMETtl = models.IntegerField(default=1)


class ContainerConfig(models.Model):
    # Boot Config
    bootAutostart = models.BooleanField()
    bootAutoStartDelay = models.IntegerField()
    bootAutostartPriority = models.IntegerField()
    bootHostShutDownTimeOut = models.IntegerField()
    bootStopPrority = models.IntegerField()
    # Environment Config
    env = models.CharField(max_length=30)
    # Limits Config
    limitsCpu = models.CharField(max_length=30)
    limitsCpuAllowance = models.CharField(max_length=30)
    limitsCpuPriority = models.CharField(max_length=30)
    limitsDiskPriority = models.IntegerField()
    limitsHugePages64K = models.CharField(max_length=30)
    limitsCpuHugePages1M = models.CharField(max_length=30)
    limitsCpuHugePages2M = models.CharField(max_length=30)
    limitsCpuHugePages1G = models.CharField(max_length=30)
    limitsKernel = models.CharField(max_length=30)
    limitsMemory = models.CharField(max_length=30)
    limitsMemoryEnforce = models.CharField(max_length=30)
    limitsMemoryHugePages = models.BooleanField()
    limitsMemorySwap = models.BooleanField()
    limitsMemorySwapPriority = models.IntegerField()
    limitsNetworkPriority = models.IntegerField()
    limitsProcesses = models.IntegerField()
    # LinuxKernel Config
    linuxKernelModules = models.CharField(max_length=30)
    # MigrationIncremental Config
    migrationIncrementalMemory = models.BooleanField()
    migrationIncrementalMemoryGoal = models.IntegerField()
    migrationIncrementalMemoryIterations = models.IntegerField()
    # Nvidia Config
    nvidiaDriverCapabilities = models.CharField(max_length=30)
    nvidiaRuntime = models.BooleanField()
    nvidiaRequireCuda = models.CharField(max_length=30)
    nvidiaRequireDriver = models.CharField(max_length=30)
    # TODO: raw data
    # Security Config
    securityDevLxd = models.BooleanField()
    securityIdMapBase = models.IntegerField()
    securityIdMapIsolated = models.BooleanField()
    securityIdMapSize = models.IntegerField()
    securityNesting = models.BooleanField()
    securityPrivileged = models.BooleanField()
    securityProtectionDelete = models.BooleanField()
    securityProtectionShift = models.BooleanField()
    securitySecureBoot = models.BooleanField()
    securitySyscallsBlackList = models.CharField(max_length=30)
    securitySyscallsBlackListCompat = models.BooleanField()
    securitySyscallsBlackListDefault = models.BooleanField()
    securitySyscallsInterceptMknod = models.BooleanField()
    securitySyscallsInterceptMount = models.BooleanField()
    securitySyscallsInterceptMountAllowed = models.CharField(max_length=30)
    securitySyscallsInterceptMountFuse = models.CharField(max_length=30)
    securitySyscallsInterceptMountShift = models.BooleanField()
    securitySyscallsInterceptSetxattr = models.BooleanField()
    securitySyscallsWhiteList = models.CharField(max_length=30)
    # Snapshots Config
    snapshotsSchedule = models.CharField(max_length=30)
    snapshotsScheduleStopped = models.BooleanField()
    snapshotsPattern = models.CharField(max_length=30)
    snapshotsExpiry = models.CharField(max_length=30)
    # User Config
    user = models.CharField(max_length=30)


class Network(models.Model):
    # networkConfig = models.OneToOneField(NetworkConfig, on_delete=models.CASCADE)
    description = models.CharField(max_length=30, default='')
    name = models.CharField(max_length=30, default='')
    networkType = models.CharField(max_length=30, default='bridged')
    managed = models.BooleanField(default=True)
    status = models.CharField(max_length=30, default='Created')
    # locations = ListField()


class Profile(models.Model):
    description = models.CharField(max_length=30, default="default")
    name = models.CharField(max_length=30)


class Container(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    network = models.ManyToManyField(Network)
    containerConfig = models.OneToOneField(ContainerConfig, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    remote = models.CharField(max_length=30)
    architecture = models.CharField(max_length=30)
    creation = models.DateField()
    status = models.CharField(max_length=30)
    containerType = models.CharField(max_length=30)
    pid = models.IntegerField()
    # config = EmbeddedModelField('ContainerConfig')


class Device(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    container = models.ForeignKey(Container, on_delete=models.CASCADE)


class Nic(Device, models.Model):
    parent = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    mtu = models.IntegerField()
    hwaddr = models.CharField(max_length=30)


class Bridge(Nic):
    hostName = models.CharField(max_length=30)
    limitsIngress = models.CharField(max_length=30)
    limitsEgress = models.CharField(max_length=30)
    limitsMax = models.CharField(max_length=30)
    ipv4address = models.CharField(max_length=30)
    ipv6address = models.CharField(max_length=30)
    ipv4routes = models.CharField(max_length=30)
    ipv6routes = models.CharField(max_length=30)
    securityMacFiltering = models.BooleanField()
    securityIpv4Filtering = models.BooleanField()
    securityIpv6Filtering = models.BooleanField()
    maasSubnetIpv4 = models.CharField(max_length=30)
    maasSubnetIpv6 = models.CharField(max_length=30)
    bootPriority = models.IntegerField()


class MacVlan(Nic):
    vlan = models.IntegerField()
    maasSubnetIpv4 = models.CharField(max_length=30)
    maasSubnetIpv6 = models.CharField(max_length=30)
    bootPriority = models.IntegerField()


class Physical(Nic):
    vlan = models.IntegerField()
    maasSubnetIpv4 = models.CharField(max_length=30)
    maasSubnetIpv6 = models.CharField(max_length=30)
    bootPriority = models.IntegerField()


class Ipvlan(Nic):
    vlan = models.IntegerField()
    ipv4address = models.CharField(max_length=30)
    ipv6address = models.CharField(max_length=30)


class P2P(Nic):
    hostName = models.CharField(max_length=30)
    limitsIngress = models.CharField(max_length=30)
    limitsEgress = models.CharField(max_length=30)
    limitsMax = models.CharField(max_length=30)
    ipv4routes = models.CharField(max_length=30)
    ipv6routes = models.CharField(max_length=30)
    bootPriority = models.IntegerField()


class Routed(Nic):
    vlan = models.IntegerField()
    ipv4address = models.CharField(max_length=30)
    ipv6address = models.CharField(max_length=30)


class SRIOV(Nic):
    securityMacFiltering = models.BooleanField()
    vlan = models.IntegerField()
    maasSubnetIpv4 = models.CharField(max_length=30)
    maasSubnetIpv6 = models.CharField(max_length=30)
    bootPriority = models.IntegerField()
