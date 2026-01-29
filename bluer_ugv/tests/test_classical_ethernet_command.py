from bluer_ugv.swallow.session.classical.ethernet.command import EthernetCommand


def test_classical_ethernet_command():
    command = EthernetCommand(
        action="some-action",
        data={"data": "some-data"},
    )

    as_str = command.as_str()
    assert isinstance(as_str, str)
    assert as_str

    to_dict = command.to_dict()
    assert isinstance(to_dict, dict)
    for thing in ["action", "data"]:
        assert thing in to_dict
