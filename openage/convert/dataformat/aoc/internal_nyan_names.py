# Copyright 2019-2020 the openage authors. See copying.md for legal info.

"""
Age of Empires games do not necessarily come with an english
translation. Therefore, we use the strings in this file to
figure out the names for a nyan object.
"""

# key: head unit id; value: (nyan object name, filename prefix)
UNIT_LINE_LOOKUPS = {
    4: ("Archer", "archer"),
    5: ("HandCannoneer", "hand_cannoneer"),
    7: ("Skirmisher", "skirmisher"),
    8: ("Longbowman", "longbowman"),
    11: ("Mangudai", "mangudai"),
    13: ("FishingShip", "fishing_ship"),
    17: ("TradeCog", "trade_cog"),
    25: ("TeutonicKnight", "teutonic_knight"),
    35: ("Ram", "ram"),
    36: ("BombardCannon", "bombard_cannon"),
    38: ("Knight", "knight"),
    39: ("HorseArcher", "horse_archer"),
    40: ("Cataphract", "cataphract"),
    41: ("Huscarl", "huscarl"),
    46: ("Janissary", "janissary"),
    73: ("ChuKoNu", "chu_ko_nu"),
    74: ("Militia", "militia"),
    93: ("Spearman", "spearman"),
    118: ("Villager", "villager"),
    125: ("Monk", "monk"),
    128: ("TradeCart", "trade_cart"),
    232: ("WoadRaider", "woad_raider"),
    239: ("WarElephant", "war_elephant"),
    250: ("Longboat", "longboat"),
    279: ("Scorpion", "scorpion"),
    280: ("Mangonel", "mangonel"),
    281: ("ThrowingAxeman", "throwing_axeman"),
    282: ("Mameluke", "mameluke"),
    291: ("Samurai", "samurai"),
    329: ("CamelRider", "camel_rider"),
    331: ("Trebuchet", "trebuchet"),
    420: ("CannonGalleon", "cannon_galleon"),
    440: ("Petard", "petard"),
    448: ("LightCavalry", "light_cavalry"),
    527: ("DemolitionShip", "demo_ship"),
    529: ("FireTrireme", "fire_trireme"),
    539: ("Galley", "galley"),
    545: ("TransportShip", "transport_ship"),
    692: ("Berserk", "berserk"),
    725: ("JaguarWarrior", "jaguar_warrior"),
    751: ("EagleWarrior", "eagle_warrior"),
    755: ("Tarkan", "tarkan"),
    763: ("PlumedArcher", "plumed_archer"),
    771: ("Conquistador", "conquistador"),
    775: ("Missionary", "missionary"),
    827: ("WarWaggon", "war_waggon"),
    831: ("TurtleShip", "turtle_ship"),
}

# key: head unit id; value: (nyan object name, filename prefix)
BUILDING_LINE_LOOKUPS = {
    12: ("Barracks", "barracks"),
    45: ("Dock", "dock"),
    49: ("SiegeWorkshop", "siege_workshop"),
    50: ("Farm", "farm"),
    68: ("Mill", "mill"),
    70: ("House", "house"),
    72: ("PalisadeWall", "palisade"),
    79: ("Tower", "tower"),
    82: ("Castle", "castle"),
    84: ("Market", "market"),
    87: ("ArcheryRange", "archery_range"),
    101: ("Stable", "stable"),
    103: ("Blacksmith", "blacksmith"),
    104: ("Monastery", "monastery"),
    109: ("TownCenter", "town_center"),
    117: ("StoneWall", "stone_wall"),
    199: ("FishingTrap", "fishing_trap"),
    209: ("University", "university"),
    236: ("BombardTower", "bombard_tower"),
    276: ("Wonder", "wonder"),
    487: ("StoneGate", "stone_gate"),
    562: ("LumberCamp", "lumber_camp"),
    584: ("MiningCamp", "mining_camp"),
    598: ("Outpost", "outpost"),
}

# key: head unit id; value: (nyan object name, filename prefix)
TECH_GROUP_LOOKUPS = {
    2: ("EliteTarkan", "elite_tarkan"),
    3: ("Yeoman", "yeoman"),
    4: ("ElDorado", "el_dorado"),
    5: ("FurorCeltica", "furor_celtica"),
    6: ("SiegeDrill", "siege_drill"),
    7: ("Mahouts", "mahouts"),
    8: ("TownWatch", "town_watch"),
    9: ("Zealotry", "zealotry"),
    10: ("Artillery", "artillery"),
    11: ("Crenellations", "crenellations"),
    12: ("CropRotation", "crop_rotation"),
    13: ("HeavyPlow", "heavy_plow"),
    14: ("HorseCollar", "horse_collar"),
    15: ("Guilds", "guilds"),
    16: ("Anarchy", "anarchy"),
    17: ("Banking", "banking"),
    19: ("Cartography", "cartography"),
    21: ("Atheism", "atheism"),
    22: ("Loom", "loom"),
    23: ("Coinage", "coinage"),
    24: ("GarlandWars", "garland_wars"),
    27: ("WarElephant", "war_elephant"),
    34: ("WarGalley", "war_galley"),
    35: ("Galleon", "galleon"),
    37: ("CannonGalleon", "cannon_galleon"),
    39: ("Husbandry", "husbandry"),
    45: ("Faith", "faith"),
    47: ("Chemistry", "chemistry"),
    48: ("Caravan", "caravan"),
    49: ("Berserkergang", "berserkergang"),
    50: ("Masonry", "masonry"),
    51: ("Architecture", "architecture"),
    52: ("Rocketry", "rocketry"),
    54: ("TreadmillCrane", "treadmill_crane"),
    55: ("GoldMining", "gold_mining"),
    59: ("Kataparuto", "kataparuto"),
    60: ("EliteConquistador", "elite_conquistador"),
    61: ("Logistica", "logistica"),
    63: ("Keep", "keep"),
    64: ("BombardTower", "bombard_tower"),
    67: ("Forging", "forging"),
    68: ("IronCasting", "iron_casting"),
    74: ("ScaleMailArmor", "scale_mail_armor"),
    75: ("BlastFurnace", "blast_furnace"),
    76: ("ChainMailArmor", "chain_mail_armor"),
    77: ("PlateMailArmor", "plate_mail_armor"),
    80: ("PlateBardingArmor", "plate_barding_armor"),
    81: ("ScaleBardingArmor", "scale_barding_armor"),
    82: ("ChainBardingArmor", "chain_barding_armor"),
    83: ("BeardedAxe", "bearded_axe"),
    90: ("Tracking", "tracking"),
    93: ("Ballistics", "ballistics"),
    96: ("CappedRam", "capped_ram"),
    98: ("EliteSkirmisher", "elite_skirmisher"),
    100: ("Crossbowman", "crossbowman"),
    101: ("FeudalAge", "feudal_age"),
    102: ("CastleAge", "castle_age"),
    103: ("ImperialAge", "imperial_age"),
    140: ("GuardTower", "guard_tower"),
    182: ("GoldShaftMining", "gold_shaft_mining"),
    194: ("FortifiedWall", "fortified_wall"),
    197: ("Pikeman", "pikeman"),
    199: ("Fletching", "fletching"),
    200: ("BodkinArrow", "bodkin_arrow"),
    201: ("Bracer", "bracer"),
    202: ("BoubleBitAxe", "double_bit_axe"),
    203: ("BowSaw", "bow_saw"),
    207: ("Longswordsman", "longswordsman"),
    209: ("Chevalier", "chevalier"),
    211: ("PaddedArcherArmor", "padded_archer_armor"),
    212: ("LeatherArcherArmor", "leather_archer_armor"),
    213: ("WheelBarrow", "wheel_barrow"),
    215: ("Squires", "squires"),
    217: ("TwoHandedSwordsman", "two_handed_swordsman"),
    218: ("HeavyCavalryArcher", "heavy_cavalry_archer"),
    219: ("RingArcherArmor", "RingArcherArmor"),
    221: ("TwoManSaw", "two_man_saw"),
    222: ("Swordsman", "swordsman"),
    230: ("BlockPrinting", "block_printing"),
    231: ("Sanctity", "sanctity"),
    233: ("Illumination", "illumination"),
    236: ("HeavyCamelRider", "heavy_camel_rider"),
    237: ("Arbalest", "arbalest"),
    239: ("HeavyScorpion", "heavy_scorpion"),
    244: ("HeavyDemolitionShip", "heavy_demolition_ship"),
    246: ("FastFireShip", "fast_fire_ship"),
    249: ("HandCart", "hand_cart"),
    252: ("Fervor", "fervor"),
    254: ("LightCavalry", "light_cavalry"),
    255: ("SiegeRam", "siege_ram"),
    257: ("Onager", "Onager"),
    264: ("Champion", "champion"),
    265: ("Paladin", "paladin"),
    278: ("StoneMining", "stone_mining"),
    279: ("StoneShaftMining", "stone_shaft_mining"),
    280: ("TownPatrol", "town_patrol"),
    315: ("Conscription", "conscription"),
    316: ("Redemption", "redemption"),
    319: ("Atonement", "atonement"),
    320: ("SiegeOnager", "siege_onager"),
    321: ("Sappers", "sappers"),
    322: ("MurderHoles", "murder_holes"),
    360: ("EliteLongbowman", "elite_longbowman"),
    361: ("EliteCataphract", "elite_cataphract"),
    362: ("EliteChoKoNu", "elite_cho_ko_nu"),
    363: ("EliteThrowingAxeman", "elite_throwing_axeman"),
    364: ("EliteTeutonicKnight", "elite_teutonic_knight"),
    365: ("EliteHuscarl", "elite_huscarl"),
    366: ("EliteSamurai", "elite_samurai"),
    367: ("EliteWarElephant", "elite_war_elephant"),
    368: ("EliteMameluke", "elite_mameluke"),
    369: ("EliteJanissary", "elite_janissary"),
    370: ("EliteWoadRaider", "elite_woad_raider"),
    371: ("EliteMangudai", "elite_mangudai"),
    372: ("EliteLongboat", "elite_longboat"),
    373: ("Shipwright", "shipwright"),
    374: ("Careening", "careening"),
    375: ("DryDock", "dry_dock"),
    376: ("EliteWarGalley", "elite_war_galley"),
    377: ("SiegeEngineers", "siege_engineers"),
    379: ("Hoardings", "hoardings"),
    380: ("HeatedShot", "heated_shot"),
    398: ("EliteBerserk", "elite_berserk"),
    408: ("Spies", "spies"),
    428: ("Hussar", "hussar"),
    429: ("Helbardier", "helbardier"),
    432: ("EliteJaguarWarrior", "elite_jaguar_warrior"),
    434: ("EliteEagleWarrior", "elite_eagle_warrior"),
    435: ("Bloodlines", "bloodlines"),
    436: ("ParthianTactics", "parthian_tactics"),
    437: ("ThumbRing", "thumb_ring"),
    438: ("Theocracy", "theocracy"),
    439: ("Heresy", "heresy"),
    440: ("Supremacy", "supremacy"),
    441: ("HerbalMedicine", "herbal_medicine"),
    445: ("Shinkichon", "shinkichon"),
    448: ("EliteTurtleShip", "elite_turtle_ship"),
    450: ("EliteWarWaggon", "elite_war_waggon"),
    457: ("Perfusion", "perfusion"),
}

CIV_GROUP_LOOKUPS = {
    0: "Gaia",
    1: "Britons",
    2: "Franks",
    3: "Goths",
    4: "Teutons",
    5: "Japanese",
    6: "Chinese",
    7: "Byzantines",
    8: "Persians",
    9: "Saracens",
    10: "Turks",
    11: "Vikings",
    12: "Mongols",
    13: "Celts",
    14: "Spanish",
    15: "Aztecs",
    16: "Mayans",
    17: "Huns",
    18: "Koreans",
}

CLASS_ID_LOOKUPS = {
    0: "Archer",
    1: "Artifact",
    2: "TradeBoat",
    3: "BuildingMisc",
    4: "Villager",
    5: "OceanFish",
    6: "Infantry",
    7: "BerryBush",
    8: "StoneMine",
    9: "AnimalPrey",
    10: "AnimalPredator",
    11: "DeadOrProjectileOrBird",     # do not use this as GameEntityType
    12: "Cavalry",
    13: "SiegeWeapon",
    14: "Ambient",
    15: "Tree",
    18: "Monk",
    19: "TradecCart",
    20: "TransportShip",
    21: "FishingShip",
    22: "Warship",
    23: "Conquistador",
    27: "Wall",
    28: "Phalanx",
    29: "DomesticAnimal",
    30: "AmbientFlag",
    31: "DeepSeaFish",
    32: "GoldMine",
    33: "ShoreFish",
    34: "Cliff",
    35: "Petard",
    36: "CavalryArcher",
    37: "Doppelgaenger",
    38: "Bird",
    39: "Gate",
    40: "AmbientPile",
    41: "AmbientResourcePile",
    42: "Relic",
    43: "MonkWithRelic",            # should not be present in final modpack
    44: "HandConnoneer",
    45: "TwoHandedSwordsman",       # should not be present in final modpack (unused anyway)
    46: "Pikeman",                  # should not be present in final modpack (unused anyway)
    47: "CavalryScout",
    48: "OreMine",
    49: "Restockable",
    50: "Spearman",
    51: "Trebuchet",                # packed
    52: "Tower",
    53: "BoardingShip",
    54: "Trebuchet",                # unpacked
    55: "Scorpion",
    56: "Raider",
    57: "CavalryRaider",
    58: "Herdable",
    59: "King",
    61: "Horse",
}
