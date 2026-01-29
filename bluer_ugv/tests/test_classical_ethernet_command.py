from bluer_ugv.swallow.session.classical.ethernet.command import EthernetCommand


def test_classical_ethernet_command():
    command = EthernetCommand()

    as_str = command.as_str()
    assert isinstance(as_str, str)
    assert as_str
