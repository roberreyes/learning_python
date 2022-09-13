routing_protocol = "ospf"
routing_protocol = routing_protocol.upper()
if routing_protocol == "OSPF" or routing_protocol == "ISIS":
    print("This router is running a link state protocol")
else:
    print("This router is not running a link state protocol")
