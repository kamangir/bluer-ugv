from bluer_ugv.README import (
    aliases,
    beast,
    releases,
    root,
    swallow,
)
from bluer_ugv.README.arzhang import docs as arzhang
from bluer_ugv.README.computer import docs as computer
from bluer_ugv.README.eagle import docs as eagle
from bluer_ugv.README.fire import docs as fire
from bluer_ugv.README.rangin import docs as rangin
from bluer_ugv.README.ravin import docs as ravin
from bluer_ugv.README.ROS import docs as ROS
from bluer_ugv.README.ugvs import docs as ugvs
from bluer_ugv.README.validations import docs as validations

docs = (
    root.docs
    + aliases.docs
    + arzhang.docs
    + beast.docs
    + eagle.docs
    + fire.docs
    + rangin.docs
    + ravin.docs
    + releases.docs
    + ROS.docs
    + computer.docs
    + ugvs.docs
    + swallow.docs
    + validations.docs
)
