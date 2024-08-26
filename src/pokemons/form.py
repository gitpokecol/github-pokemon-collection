from enum import Enum


class Form(str, Enum):
    def __str__(self) -> str:
        return self.value


class UnownForm(Form):
    EXCLAMATION = "-exclamation"
    QUESTION = "-question"
    A = "a"
    B = "b"
    C = "c"
    D = "d"
    E = "e"
    F = "f"
    G = "g"
    H = "h"
    I = "i"  # noqa E741
    J = "j"
    K = "k"
    L = "l"
    M = "m"
    N = "n"
    O = "o"  # noqa E741
    P = "p"
    Q = "q"
    R = "r"
    S = "s"
    T = "t"
    U = "u"
    V = "v"
    W = "w"
    X = "x"
    Y = "y"
    Z = "z"


class BurmyWormadamForm(Form):
    PLANT = "plant"
    SANDY = "sandy"
    TRASH = "trash"


class ShellosGastrodonForm(Form):
    WEST = "west"
    EAST = "east"


class RotomForm(Form):
    DEFAULT = ""
    HEAT = "heat"
    WASH = "wash"
    FROST = "frost"
    FAN = "fan"
    MOW = "mow"


class GiratinaForm(Form):
    ALTERED = "altered"
    ORIGIN = "origin"


class ShayminFrom(Form):
    LAND = "land"
    SKY = "sky"


class ArceusForm(Form):
    DEFAULT = ""
    UNKNOWN = "-unknown"
    BUG = "bug"
    DARK = "dark"
    DRAGON = "dragon"
    ELECTRIC = "electric"
    FIGHTING = "fighting"
    FIRE = "fire"
    FLYING = "flying"
    GHOST = "ghost"
    GRASS = "grass"
    GROUND = "ground"
    ICE = "ice"
    POISON = "poison"
    PSYCHIC = "psychic"
    ROCK = "rock"
    STEEL = "steel"
    WATER = "water"
