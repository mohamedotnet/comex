from django import forms


class NetworkForm(forms.Form):
    netname = forms.CharField(label="netname", max_length=40)
    netdesc = forms.CharField(label="netdesc", max_length=40)
    netype = forms.CharField(label="netype", max_length=40)
    netdomain = forms.CharField(label="netdomain", max_length=40)
    netmode = forms.ChoiceField(widget=forms.Select, choices=(
        ("mode_1", "None"),
        ("mode_2", "Managed"),
        ("mode_3", "Dynamic"),
    ))
    raw_dnsmasq = forms.CharField(label="raw_dnsmasq", max_length=40)
    bridge_driver = forms.ChoiceField(widget=forms.Select, choices=(
        ("bridge_driver_1", "Native"),
        ("bridge_driver_2", "Open vSwitch"),
    ))
    e_interfaces = forms.CharField(label="e_interfaces", max_length=40)
    hwaddr = forms.CharField(label="hwaddr", max_length=40)
    driver_mode = forms.ChoiceField(widget=forms.Select, choices=(
        ("driver_mode_1", "Standard"),
        ("driver_mode_2", "Fan"),
    ))
    mtu = forms.IntegerField(label="mtu", max_length=40)
    overlay = forms.CharField(label="overlay", max_length=40)
    fantype = forms.ChoiceField(widget=forms.Select, choices=(
        ("fan_type_1", "vxlan"),
        ("fan_type_2", "ipip"),
    ))
    underlay = forms.CharField(label="underlay", max_length=40)
    v4addr = forms.CharField(label="v4addr", max_length=40)
    netname = forms.CharField(label="netname", max_length=40)
    forms.CheckboxInput()
