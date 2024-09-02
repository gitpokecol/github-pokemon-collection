"""0003-pokemon-column-update

Revision ID: 2f4a1e34bb23
Revises: 355bcc98cde5
Create Date: 2024-09-02 23:05:48.613565

"""

from typing import Sequence, Union

import sqlalchemy as sa
import sqlmodel
from alembic import op
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = "2f4a1e34bb23"
down_revision: Union[str, None] = "355bcc98cde5"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute("TRUNCATE TABLE commit_point")
    op.execute("TRUNCATE TABLE pokemon")

    op.add_column("pokemon", sa.Column("level", sa.Integer(), nullable=False))
    op.add_column("pokemon", sa.Column("friendship", sa.Integer(), nullable=False))
    op.add_column("pokemon", sa.Column("gender", sa.String(), nullable=False))
    op.add_column("pokemon", sa.Column("form", sa.String(), nullable=True))
    op.drop_column("pokemon", "type")
    op.add_column("pokemon", sa.Column("type", sa.Integer(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    op.drop_column("pokemon", "type")
    op.add_column(
        "pokemon",
        sa.Column(
            "type",
            sa.Enum(
                "Bulbasaur",
                "Ivysaur",
                "Venusaur",
                "Charmander",
                "Charmeleon",
                "Charizard",
                "Squirtle",
                "Wartortle",
                "Blastoise",
                "Caterpie",
                "Metapod",
                "Butterfree",
                "Weedle",
                "Kakuna",
                "Beedrill",
                "Pidgey",
                "Pidgeotto",
                "Pidgeot",
                "Rattata",
                "Raticate",
                "Spearow",
                "Fearow",
                "Ekans",
                "Arbok",
                "Pikachu",
                "Raichu",
                "Sandshrew",
                "Sandslash",
                "Nidoran_female",
                "Nidorina",
                "Nidoqueen",
                "Nidoran_male",
                "Nidorino",
                "Nidoking",
                "Clefairy",
                "Clefable",
                "Vulpix",
                "Ninetales",
                "Jigglypuff",
                "Wigglytuff",
                "Zubat",
                "Golbat",
                "Oddish",
                "Gloom",
                "Vileplume",
                "Paras",
                "Parasect",
                "Venonat",
                "Venomoth",
                "Diglett",
                "Dugtrio",
                "Meowth",
                "Persian",
                "Psyduck",
                "Golduck",
                "Mankey",
                "Primeape",
                "Growlithe",
                "Arcanine",
                "Poliwag",
                "Poliwhirl",
                "Poliwrath",
                "Abra",
                "Kadabra",
                "Alakazam",
                "Machop",
                "Machoke",
                "Machamp",
                "Bellsprout",
                "Weepinbell",
                "Victreebel",
                "Tentacool",
                "Tentacruel",
                "Geodude",
                "Graveler",
                "Golem",
                "Ponyta",
                "Rapidash",
                "Slowpoke",
                "Slowbro",
                "Magnemite",
                "Magneton",
                "d",
                "Doduo",
                "Dodrio",
                "Seel",
                "Dewgong",
                "Grimer",
                "Muk",
                "Shellder",
                "Cloyster",
                "Gastly",
                "Haunter",
                "Gengar",
                "Onix",
                "Drowzee",
                "Hypno",
                "Krabby",
                "Kingler",
                "Voltorb",
                "Electrode",
                "Exeggcute",
                "Exeggutor",
                "Cubone",
                "Marowak",
                "Hitmonlee",
                "Hitmonchan",
                "Lickitung",
                "Koffing",
                "Weezing",
                "Rhyhorn",
                "Rhydon",
                "Chansey",
                "Tangela",
                "Kangaskhan",
                "Horsea",
                "Seadra",
                "Goldeen",
                "Seaking",
                "Staryu",
                "Starmie",
                "Mime",
                "Scyther",
                "Jynx",
                "Electabuzz",
                "Magmar",
                "Pinsir",
                "Tauros",
                "Magikarp",
                "Gyarados",
                "Lapras",
                "Ditto",
                "Eevee",
                "Vaporeon",
                "Jolteon",
                "Flareon",
                "Porygon",
                "Omanyte",
                "Omastar",
                "Kabuto",
                "Kabutops",
                "Aerodactyl",
                "Snorlax",
                "Articuno",
                "Zapdos",
                "Moltres",
                "Dratini",
                "Dragonair",
                "Dragonite",
                "Mewtwo",
                "Mew",
                name="pokemontype",
            ),
            nullable=False,
        ),
    )
    op.drop_column("pokemon", "form")
    op.drop_column("pokemon", "gender")
    op.drop_column("pokemon", "friendship")
    op.drop_column("pokemon", "level")
    # ### end Alembic commands ###
