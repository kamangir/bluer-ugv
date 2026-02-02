from typing import Tuple, Union, Type, Dict

from bluer_ugv.swallow.session.classical.scenario.state.machines.generic import (
    GenericStateMachine,
)
from bluer_ugv.swallow.session.classical.scenario.state.machines.rangin import (
    RanginStateMachine,
)
from bluer_ugv.swallow.session.classical.scenario.state.machines.swallow import (
    SwallowStateMachine,
)

dict_of_state_machines: Dict[str, Type[GenericStateMachine]] = {
    cls.name: cls
    for cls in [
        GenericStateMachine,
        RanginStateMachine,
        SwallowStateMachine,
    ]
}
