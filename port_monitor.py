from pox.core import core
import pox.openflow.libopenflow_01 as of

log = core.getLogger()

mac_to_port = {}

def _handle_PortStatus(event):
    dpid = event.dpid
    port = event.ofp.desc.port_no
    state = event.ofp.desc.state

    status = "UP" if state == 0 else "DOWN"
    log.info(f"[ALERT] Switch {dpid} Port {port} is {status}")

def _handle_PacketIn(event):
    packet = event.parsed
    dpid = event.dpid
    in_port = event.port

    if dpid not in mac_to_port:
        mac_to_port[dpid] = {}

    mac_to_port[dpid][packet.src] = in_port

    if packet.dst in mac_to_port[dpid]:
        out_port = mac_to_port[dpid][packet.dst]
    else:
        out_port = of.OFPP_FLOOD

    msg = of.ofp_packet_out()
    msg.data = event.ofp
    msg.actions.append(of.ofp_action_output(port=out_port))
    event.connection.send(msg)

def _handle_ConnectionUp(event):
    log.info(f"Switch {event.dpid} connected")

def launch():
    core.openflow.addListenerByName("PortStatus", _handle_PortStatus)
    core.openflow.addListenerByName("PacketIn", _handle_PacketIn)
    core.openflow.addListenerByName("ConnectionUp", _handle_ConnectionUp)