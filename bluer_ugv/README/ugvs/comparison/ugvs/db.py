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
        "DYI": ...,
        "control": UGV_Control.RC,
        "cost": ...,
        "payload": ...,
        "ps": ...,
        "range": ...,
        "size": UGV_Size.MEDIUM,
        "speed": 30,
        "swarm": ...,
        "uv_delivery": ...,
    },
)

list_of_ugvs.add(
    nickname="qasem",
    name="ربات قاسم",
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

list_of_ugvs.add(
    nickname="arya",
    name="ربات آریا",
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

list_of_ugvs.add(
    nickname="sepah",
    name="ربات جنگ میدانی سپاه",
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


list_of_ugvs.add(
    nickname="raad1",
    name="متلاشی‌کننده بمب و تله انفجاری رعد ۱",
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

list_of_ugvs.add(
    nickname="themis_9",
    name="THeMIS-9",
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

list_of_ugvs.add(
    nickname="centaur",
    name="Centaur",
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
