from typing import Dict, List, Tuple

from blueness import NAME

from bluer_ugv import NAME
from bluer_ugv.logger import logger

db_of_parts: Dict[str, List[str]] = {
    "330-ohm": [
        "Resistor, 330-470 Ω, 1/4 watt, 5% tolerance",
    ],
    "4-ch-transceiver": [
        "4-channel transmitter and receiver",
        "source: [digikala](https://www.digikala.com/product/dkp-11037586/%DA%AF%DB%8C%D8%B1%D9%86%D8%AF%D9%87-%D9%88-%D9%81%D8%B1%D8%B3%D8%AA%D9%86%D8%AF%D9%87-%D9%85%D8%A7%D8%B4%DB%8C%D9%86-%DA%A9%D9%86%D8%AA%D8%B1%D9%84%DB%8C-%D9%85%D8%AF%D9%84-4ch-led/)",
    ],
    "470-mF": [
        "capacitor, 470 μF to 1000 μF, 16 V or 25 V, Electrolytic, 105 °C rated if possible."
    ],
    "BTS7960": [
        "43 A, H-Bridge Motor Driver",
        "specs: [BTS7960](https://www.handsontec.com/dataspecs/module/BTS7960%20Motor%20Driver.pdf)",
    ],
    "dc-motor-12-VDC-45W": [
        "12 VDC motor, 20-45 W, 9000 RPM",
    ],
    "LED": [
        "LED, ~2 V forward voltage, 10-20 mA",
    ],
    "Polyfuse": [
        "Polyfuse, 1.1 A hold, 2.2 A trip, 16 V, resettable, through-hole, e.g., MF-R110",
    ],
    "rpi3bp": [
        "Raspberry Pi 3B+",
    ],
    "SLA-Battery": [
        "Rechargeable sealed lead acid battery, 12 V, 7 Ah",
    ],
    "TVS-diode": [
        "TVS diode, unidirectional, 600 W, 6.8 V clamp, e.g. P6KE6.8A, DO-15 package",
    ],
    "XL4015": [
        "12 VDC -> 5 VDC, 4A",
        "specs: [XL4015](https://www.handsontec.com/dataspecs/module/XL4015-5A-PS.pdf)",
    ],
}


def get_list_of_parts(
    dict_of_parts: Dict[str, str],
    reference: str = "../parts",
) -> Tuple[bool, List[str]]:
    logger.info(
        "{}.get_list_of_parts: {}".format(
            NAME,
            ", ".join(dict_of_parts.keys()),
        )
    )

    for part_name in dict_of_parts:
        if part_name not in db_of_parts:
            logger.error(f"{part_name}: part not found.")
            return False, []

    return True, sorted(
        [
            (
                "1. [{}{}]().".format(
                    db_of_parts[part_name][0],
                    ": {}".format(description) if description else "",
                    f"{reference}/{part_name}.md",
                )
            )
            for part_name, description in dict_of_parts.items()
        ]
    )
