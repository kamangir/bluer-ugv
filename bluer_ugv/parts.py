from typing import Dict, List

db_of_parts = {
    "4-channel transmitter and receiver": "4-channel transmitter and receiver, [digikala](https://www.digikala.com/product/dkp-11037586/%DA%AF%DB%8C%D8%B1%D9%86%D8%AF%D9%87-%D9%88-%D9%81%D8%B1%D8%B3%D8%AA%D9%86%D8%AF%D9%87-%D9%85%D8%A7%D8%B4%DB%8C%D9%86-%DA%A9%D9%86%D8%AA%D8%B1%D9%84%DB%8C-%D9%85%D8%AF%D9%84-4ch-led/)",
    "rpi3b+": "Raspberry Pi 3B+",
    "dc motor, 12 VDC, 45 W, 9000 RPM": "DC motors: 12 VDC, 20-45 W, 9000 RPM",
    "SLA Battery": "Battery: Rechargeable sealed lead acid, 12 V, 7 Ah",
    "XL4015": "DC 12 VDC -> 5 VDC, 4A, [XL4015](https://www.handsontec.com/dataspecs/module/XL4015-5A-PS.pdf)",
    "BTS7960": "43 A H-Bridge Motor Driver, [BTS7960](https://www.handsontec.com/dataspecs/module/BTS7960%20Motor%20Driver.pdf)",
    "470 μF": "Capacitor, 470 μF to 1000 μF, 16 V or 25 V, Electrolytic, 105 °C rated if possible.",
    "Polyfuse": "Polyfuse, 1.1 A hold, 2.2 A trip, 16 V, resettable, through-hole, e.g., MF-R110",
    "TVS diode": "TVS diode, unidirectional, 600 W, 6.8 V clamp, e.g. P6KE6.8A, DO-15 package",
    "330 Ω": "Resistor, 330-470 Ω, 1/4 watt, 5% tolerance",
    "LED": "LED, ~2 V forward voltage, 10-20 mA",
}


def list_of_parts(dict_of_parts: Dict[str, str]) -> List[str]:
    return [
        (
            "- {}: {}".format(description, db_of_parts[part_name])
            if description
            else "- {}".format(db_of_parts[part_name])
        )
        for part_name, description in dict_of_parts.items()
    ]
