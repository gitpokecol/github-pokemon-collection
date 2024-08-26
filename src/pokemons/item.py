from enum import Enum


class Item(str, Enum):
    FIRE_STONE = "Fire Stone"
    WATER_STONE = "Water Stone"
    THUNDER_STONE = "Thunder Stone"
    LEAF_STONE = "Leaf Stone"
    MOON_STONE = "Moon Stone"
    SUN_STONE = "Sun Stone"
    SHINY_STONE = "Shiny Stone"
    DUSK_STONE = "Dusk Stone"
    DAWN_STONE = "Dawn Stone"
    ICE_STONE = "Ice Stone"

    ELECTIRIZER = "Electirizer"
    MAGMARIZER = "Magmarizer"
    DRAGON_SCALE = "Dragon Scale"
    REAPER_CLOTH = "Reaper Cloth"
    PROTECTOR = "Protector"
    UP_GRADE = "Up-Grade"
    DUBIOUS_DISC = "Dubious Disc"
    PRISM_SCALE = "Prism Scale"
    OVAL_STONE = "Oval Stone"

    KINGS_ROCK = "King's Rock"
    RAZOR_FANG = "Razor Fang"
    RAZOR_CLAW = "Razor Claw"

    DEEP_SEA_TOOTH = "Deep Sea Tooth"
    DEEP_SEA_SCALE = "Deep Sea Scale"
    METAL_COAT = "Metal Coat"

    LINKING_CORD = "Linking Cord"

    FLAME_PLATE = "Flame Plate"
    SPLASH_PLATE = "Splash Plate"
    ZAP_PLATE = "Zap Plate"
    MEADOW_PLATE = "Meadow Plate"
    ICICLE_PLATE = "Icicle Plate"
    FIST_PLATE = "Fist Plate"
    TOXIC_PLATE = "Toxic Plate"
    EARTH_PLATE = "Earth Plate"
    SKY_PLATE = "Sky Plate"
    MIND_PLATE = "Mind Plate"
    INSECT_PLATE = "Insect Plate"
    STONE_PLATE = "Stone Plate"
    SPOOKY_PLATE = "Spooky Plate"
    DRACO_PLATE = "Draco Plate"
    DREAD_PLATE = "Dread Plate"
    IRON_PLATE = "Iron Plate"
    PIXIE_PLATE = "Pixie Plate"
    BLANK_PLATE = "Blank Plate"
    LEGEND_PLATE = "Legend Plate"

    POKEBALL = "Pokeball"
    RARE_CANDY = "Rare Candy"

    def __str__(self) -> str:
        return self.value
