from bluer_ugv.README.ugvs.comparison.features.control import UGV_Control
from bluer_ugv.README.ugvs.comparison.features.cost import UGV_Cost
from bluer_ugv.README.ugvs.comparison.features.size import UGV_Size
from bluer_ugv.README.ugvs.comparison.ugvs.classes import List_of_UGVs
from bluer_ugv.README.ugvs.comparison.features.range import unlimited_range

list_of_ugvs = List_of_UGVs()

list_of_ugvs.add(
    nickname="arzhang",
    name="محصول ما",
    features={
        "concealment": True,
        "control": UGV_Control.AI,
        "cost": UGV_Cost.LOW,
        "payload": 40,
        "range": unlimited_range,
        "ps": True,
        "sanction_proof": True,
        "size": UGV_Size.SMALL,
        "speed": 4,
        "swarm": True,
        "uv_delivery": True,
    },
)

list_of_ugvs.add(
    nickname="nazir",
    name="ربات موشک‌انداز نذیر",
    features={
        "control": UGV_Control.RC,
        "cost": UGV_Cost.MEDIUM,
        "payload": 700,
        "range": 4,
        "size": UGV_Size.MEDIUM,
    },
)

list_of_ugvs.add(
    nickname="heidar",
    name="ربات حیدر",
    features={
        "concealment": True,
        "control": UGV_Control.AI,
        "cost": UGV_Cost.LOW,
        "payload": 40,
        "range": 10,
        "size": UGV_Size.SMALL,
        "speed": 60,
        "swarm": True,
    },
    deficiencies=[
        "انتقال قدرت: زنجیر",
    ],
)


list_of_ugvs.add(
    nickname="karakal",
    name="ربات جنگجوی هوشمند کاراکال",
    features={
        "control": UGV_Control.AI,
        "cost": UGV_Cost.MEDIUM,
        "size": UGV_Size.MEDIUM,
        "speed": 30,
        "range": 0.5,
    },
)

list_of_ugvs.add(
    nickname="qasem",
    name="ربات قاسم",
    features={
        "cost": UGV_Cost.MEDIUM,
        "size": UGV_Size.MEDIUM,
        "uv_delivery": True,
    },
    deficiencies=[],
)

list_of_ugvs.add(
    nickname="arya",
    name="ربات آریا",
    features={
        "control": UGV_Control.AI,
        "cost": UGV_Cost.MEDIUM,
        "size": UGV_Size.MEDIUM,
        "speed": 50,
        "uv_delivery": True,
    },
    deficiencies=[],
)

list_of_ugvs.add(
    nickname="sepah",
    name="ربات جنگ میدانی سپاه",
    features={},
    deficiencies=[],
)


list_of_ugvs.add(
    nickname="raad1",
    name="متلاشی‌کننده بمب و تله انفجاری رعد ۱",
    features={
        "control": UGV_Control.RC,
        "cost": UGV_Cost.MEDIUM,
        "size": UGV_Size.SMALL,
    },
    deficiencies=[],
)

list_of_ugvs.add(
    nickname="uran_9",
    name="Uran-9",
    features={
        "DYI": ...,
        "control": UGV_Control.AI,
        "cost": UGV_Cost.HIGH,
        "range": 1,
        "size": UGV_Size.LARGE,
        "speed": 133,
    },
    deficiencies=[],
)

list_of_ugvs.add(
    nickname="themis_9",
    name="THeMIS-9",
    features={
        "control": UGV_Control.AI,
        "cost": UGV_Cost.HIGH,
        "payload": 1630,
        "range": 1.5,
        "size": UGV_Size.LARGE,
        "speed": 20,
    },
    deficiencies=[],
)

list_of_ugvs.add(
    nickname="type_x",
    name="Type-X",
    features={
        "control": UGV_Control.AI,
        "cost": UGV_Cost.HIGH,
        "payload": 4100,
        "size": UGV_Size.LARGE,
        "speed": 80,
    },
    deficiencies=[],
)


list_of_ugvs.add(
    nickname="centaur",
    name="Centaur",
    features={
        "control": UGV_Control.RC,
        "cost": UGV_Cost.HIGH,
        "payload": 14.5,
        "range": 0.8,
        "size": UGV_Size.MEDIUM,
        "speed": 4,
    },
    deficiencies=[],
)


list_of_ugvs.add(
    nickname="xm1219",
    name="XM1219",
    features={
        "control": UGV_Control.RC,
        "cost": UGV_Cost.HIGH,
        "size": UGV_Size.LARGE,
    },
    deficiencies=[],
)

list_of_ugvs.add(
    nickname="talon",
    name="Foster-Miller TALON",
    features={
        "control": UGV_Control.RC,
        "cost": UGV_Cost.HIGH,
        "range": 1.2,
        "size": UGV_Size.MEDIUM,
    },
    deficiencies=[],
)

list_of_ugvs.add(
    nickname="gladiator",
    name="Gladiator TUGV",
    features={
        "control": UGV_Control.RC,
        "cost": UGV_Cost.HIGH,
        "size": UGV_Size.LARGE,
    },
    deficiencies=[],
)

list_of_ugvs.add(
    nickname="ukap",
    name="UKAP",
    features={
        "control": UGV_Control.RC,
        "cost": UGV_Cost.HIGH,
        "size": UGV_Size.LARGE,
    },
    deficiencies=[],
)

list_of_ugvs.add(
    nickname="ripsaw",
    name="Ripsaw",
    features={
        "control": UGV_Control.AI,
        "cost": UGV_Cost.HIGH,
        "payload": 910,
        "size": UGV_Size.LARGE,
        "speed": 105,
    },
    deficiencies=[],
)

list_of_ugvs.add(
    nickname="teodor",
    name="tEODor",
    features={
        "control": UGV_Control.RC,
        "cost": UGV_Cost.HIGH,
        "payload": 100,
        "size": UGV_Size.MEDIUM,
    },
    deficiencies=[],
)


list_of_ugvs.add(
    nickname="black_knight",
    name="Black Knight",
    features={
        "control": UGV_Control.AI,
        "cost": UGV_Cost.HIGH,
        "size": UGV_Size.LARGE,
        "speed": 77,
    },
    deficiencies=[],
)

list_of_ugvs.add(
    nickname="guardium",
    name="Guardium",
    features={
        "control": UGV_Control.AI,
        "cost": UGV_Cost.HIGH,
        "size": UGV_Size.LARGE,
    },
    deficiencies=[],
)

list_of_ugvs.add(
    nickname="milica",
    name="Milos & Milica",
    features={
        "control": UGV_Control.RC,
        "cost": UGV_Cost.MEDIUM,
        "payload": 100,
        "range": 3,
        "size": UGV_Size.LARGE,
        "speed": 12.5,
    },
    deficiencies=[],
)

list_of_ugvs.add(
    nickname="taifun_m",
    name="Taifun-M",
    features={
        "control": UGV_Control.RC,
        "cost": UGV_Cost.HIGH,
        "size": UGV_Size.LARGE,
        "uv_delivery": True,
    },
    deficiencies=[],
)

list_of_ugvs.add(
    nickname="template",
    name="template",
    features={
        "DYI": ...,
        "control": ...,
        "cost": ...,
        "payload": ...,
        "ps": ...,
        "range": ...,
        "size": ...,
        "speed": ...,
        "swarm": ...,
        "uv_delivery": ...,
    },
    deficiencies=[],
)
