from enum import Enum

from src.pokemons.form import ArceusForm
from src.pokemons.item_effect import EvolutionItemEffect, ItemEffect, PlateEffect, RareCandyEffect


class ItemType(int, Enum):
    title: str
    effect: None | ItemEffect

    FIRE_STONE = ("Fire Stone", EvolutionItemEffect())
    WATER_STONE = ("Water Stone", EvolutionItemEffect())
    THUNDER_STONE = ("Thunder Stone", EvolutionItemEffect())
    LEAF_STONE = ("Leaf Stone", EvolutionItemEffect())
    MOON_STONE = ("Moon Stone", EvolutionItemEffect())
    SUN_STONE = ("Sun Stone", EvolutionItemEffect())
    SHINY_STONE = ("Shiny Stone", EvolutionItemEffect())
    DUSK_STONE = ("Dusk Stone", EvolutionItemEffect())
    DAWN_STONE = ("Dawn Stone", EvolutionItemEffect())
    ICE_STONE = ("Ice Stone", EvolutionItemEffect())

    ELECTIRIZER = ("Electirizer", EvolutionItemEffect())
    MAGMARIZER = ("Magmarizer", EvolutionItemEffect())
    DRAGON_SCALE = ("Dragon Scale", EvolutionItemEffect())
    REAPER_CLOTH = ("Reaper Cloth", EvolutionItemEffect())
    PROTECTOR = ("Protector", EvolutionItemEffect())
    UP_GRADE = ("Up-Grade", EvolutionItemEffect())
    DUBIOUS_DISC = ("Dubious Disc", EvolutionItemEffect())
    PRISM_SCALE = ("Prism Scale", EvolutionItemEffect())
    OVAL_STONE = ("Oval Stone", EvolutionItemEffect())

    KINGS_ROCK = ("King's Rock", EvolutionItemEffect())
    RAZOR_FANG = ("Razor Fang", EvolutionItemEffect())
    RAZOR_CLAW = ("Razor Claw", EvolutionItemEffect())

    DEEP_SEA_TOOTH = ("Deep Sea Tooth", EvolutionItemEffect())
    DEEP_SEA_SCALE = ("Deep Sea Scale", EvolutionItemEffect())
    METAL_COAT = ("Metal Coat", EvolutionItemEffect())

    LINKING_CORD = ("Linking Cord", EvolutionItemEffect())

    FLAME_PLATE = ("Flame Plate", PlateEffect(ArceusForm.FIRE))
    SPLASH_PLATE = ("Splash Plate", PlateEffect(ArceusForm.WATER))
    ZAP_PLATE = ("Zap Plate", PlateEffect(ArceusForm.ELECTRIC))
    MEADOW_PLATE = ("Meadow Plate", PlateEffect(ArceusForm.GRASS))
    ICICLE_PLATE = ("Icicle Plate", PlateEffect(ArceusForm.ICE))
    FIST_PLATE = ("Fist Plate", PlateEffect(ArceusForm.FIGHTING))
    TOXIC_PLATE = ("Toxic Plate", PlateEffect(ArceusForm.POISON))
    EARTH_PLATE = ("Earth Plate", PlateEffect(ArceusForm.GROUND))
    SKY_PLATE = ("Sky Plate", PlateEffect(ArceusForm.FLYING))
    MIND_PLATE = ("Mind Plate", PlateEffect(ArceusForm.PSYCHIC))
    INSECT_PLATE = ("Insect Plate", PlateEffect(ArceusForm.BUG))
    STONE_PLATE = ("Stone Plate", PlateEffect(ArceusForm.ROCK))
    SPOOKY_PLATE = ("Spooky Plate", PlateEffect(ArceusForm.GHOST))
    DRACO_PLATE = ("Draco Plate", PlateEffect(ArceusForm.DRAGON))
    DREAD_PLATE = ("Dread Plate", PlateEffect(ArceusForm.DARK))
    IRON_PLATE = ("Iron Plate", PlateEffect(ArceusForm.STEEL))
    BLANK_PLATE = ("Blank Plate", PlateEffect(ArceusForm.DEFAULT))

    POKEBALL = ("Pokeball", None)
    RARE_CANDY = ("Rare Candy", RareCandyEffect())

    def __new__(cls, title: str, effect: ItemEffect | None) -> "ItemType":
        value = len(cls.__members__) + 1
        instance = int.__new__(cls, value)
        instance._value_ = value
        instance.title = title
        instance.effect = effect

        return instance
