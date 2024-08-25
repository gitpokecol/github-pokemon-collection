from enum import IntEnum

from src.pokemons.form import (ArceusForm, BurmyWormadamForm, Form, RotomForm,
                               ShayminFrom, ShellosGastrodonForm, UnownForm)
from src.pokemons.gender import Gender


class PokemonType(IntEnum):
    national_no: int
    title: str
    available_genders: tuple[Gender, ...]
    available_forms: tuple[Form, ...]

    Bulbasaur = (1, "Bulbasaur", (Gender.FEMALE, Gender.MALE))
    Ivysaur = (2, "Ivysaur", (Gender.FEMALE, Gender.MALE))
    Venusaur = (3, "Venusaur", (Gender.FEMALE, Gender.MALE))
    Charmander = (4, "Charmander", (Gender.FEMALE, Gender.MALE))
    Charmeleon = (5, "Charmeleon", (Gender.FEMALE, Gender.MALE))
    Charizard = (6, "Charizard", (Gender.FEMALE, Gender.MALE))
    Squirtle = (7, "Squirtle", (Gender.FEMALE, Gender.MALE))
    Wartortle = (8, "Wartortle", (Gender.FEMALE, Gender.MALE))
    Blastoise = (9, "Blastoise", (Gender.FEMALE, Gender.MALE))
    Caterpie = (10, "Caterpie", (Gender.FEMALE, Gender.MALE))
    Metapod = (11, "Metapod", (Gender.FEMALE, Gender.MALE))
    Butterfree = (12, "Butterfree", (Gender.FEMALE, Gender.MALE))
    Weedle = (13, "Weedle", (Gender.FEMALE, Gender.MALE))
    Kakuna = (14, "Kakuna", (Gender.FEMALE, Gender.MALE))
    Beedrill = (15, "Beedrill", (Gender.FEMALE, Gender.MALE))
    Pidgey = (16, "Pidgey", (Gender.FEMALE, Gender.MALE))
    Pidgeotto = (17, "Pidgeotto", (Gender.FEMALE, Gender.MALE))
    Pidgeot = (18, "Pidgeot", (Gender.FEMALE, Gender.MALE))
    Rattata = (19, "Rattata", (Gender.FEMALE, Gender.MALE))
    Raticate = (20, "Raticate", (Gender.FEMALE, Gender.MALE))
    Spearow = (21, "Spearow", (Gender.FEMALE, Gender.MALE))
    Fearow = (22, "Fearow", (Gender.FEMALE, Gender.MALE))
    Ekans = (23, "Ekans", (Gender.FEMALE, Gender.MALE))
    Arbok = (24, "Arbok", (Gender.FEMALE, Gender.MALE))
    Pikachu = (25, "Pikachu", (Gender.FEMALE, Gender.MALE))
    Raichu = (26, "Raichu", (Gender.FEMALE, Gender.MALE))
    Sandshrew = (27, "Sandshrew", (Gender.FEMALE, Gender.MALE))
    Sandslash = (28, "Sandslash", (Gender.FEMALE, Gender.MALE))
    Nidoran_female = (29, "Nidoran♀", (Gender.FEMALE,))
    Nidorina = (30, "Nidorina", (Gender.FEMALE,))
    Nidoqueen = (31, "Nidoqueen", (Gender.FEMALE,))
    Nidoran_male = (32, "Nidoran♂", (Gender.MALE,))
    Nidorino = (33, "Nidorino", (Gender.MALE,))
    Nidoking = (34, "Nidoking", (Gender.MALE,))
    Clefairy = (35, "Clefairy", (Gender.FEMALE, Gender.MALE))
    Clefable = (36, "Clefable", (Gender.FEMALE, Gender.MALE))
    Vulpix = (37, "Vulpix", (Gender.FEMALE, Gender.MALE))
    Ninetales = (38, "Ninetales", (Gender.FEMALE, Gender.MALE))
    Jigglypuff = (39, "Jigglypuff", (Gender.FEMALE, Gender.MALE))
    Wigglytuff = (40, "Wigglytuff", (Gender.FEMALE, Gender.MALE))
    Zubat = (41, "Zubat", (Gender.FEMALE, Gender.MALE))
    Golbat = (42, "Golbat", (Gender.FEMALE, Gender.MALE))
    Oddish = (43, "Oddish", (Gender.FEMALE, Gender.MALE))
    Gloom = (44, "Gloom", (Gender.FEMALE, Gender.MALE))
    Vileplume = (45, "Vileplume", (Gender.FEMALE, Gender.MALE))
    Paras = (46, "Paras", (Gender.FEMALE, Gender.MALE))
    Parasect = (47, "Parasect", (Gender.FEMALE, Gender.MALE))
    Venonat = (48, "Venonat", (Gender.FEMALE, Gender.MALE))
    Venomoth = (49, "Venomoth", (Gender.FEMALE, Gender.MALE))
    Diglett = (50, "Diglett", (Gender.FEMALE, Gender.MALE))
    Dugtrio = (51, "Dugtrio", (Gender.FEMALE, Gender.MALE))
    Meowth = (52, "Meowth", (Gender.FEMALE, Gender.MALE))
    Persian = (53, "Persian", (Gender.FEMALE, Gender.MALE))
    Psyduck = (54, "Psyduck", (Gender.FEMALE, Gender.MALE))
    Golduck = (55, "Golduck", (Gender.FEMALE, Gender.MALE))
    Mankey = (56, "Mankey", (Gender.FEMALE, Gender.MALE))
    Primeape = (57, "Primeape", (Gender.FEMALE, Gender.MALE))
    Growlithe = (58, "Growlithe", (Gender.FEMALE, Gender.MALE))
    Arcanine = (59, "Arcanine", (Gender.FEMALE, Gender.MALE))
    Poliwag = (60, "Poliwag", (Gender.FEMALE, Gender.MALE))
    Poliwhirl = (61, "Poliwhirl", (Gender.FEMALE, Gender.MALE))
    Poliwrath = (62, "Poliwrath", (Gender.FEMALE, Gender.MALE))
    Abra = (63, "Abra", (Gender.FEMALE, Gender.MALE))
    Kadabra = (64, "Kadabra", (Gender.FEMALE, Gender.MALE))
    Alakazam = (65, "Alakazam", (Gender.FEMALE, Gender.MALE))
    Machop = (66, "Machop", (Gender.FEMALE, Gender.MALE))
    Machoke = (67, "Machoke", (Gender.FEMALE, Gender.MALE))
    Machamp = (68, "Machamp", (Gender.FEMALE, Gender.MALE))
    Bellsprout = (69, "Bellsprout", (Gender.FEMALE, Gender.MALE))
    Weepinbell = (70, "Weepinbell", (Gender.FEMALE, Gender.MALE))
    Victreebel = (71, "Victreebel", (Gender.FEMALE, Gender.MALE))
    Tentacool = (72, "Tentacool", (Gender.FEMALE, Gender.MALE))
    Tentacruel = (73, "Tentacruel", (Gender.FEMALE, Gender.MALE))
    Geodude = (74, "Geodude", (Gender.FEMALE, Gender.MALE))
    Graveler = (75, "Graveler", (Gender.FEMALE, Gender.MALE))
    Golem = (76, "Golem", (Gender.FEMALE, Gender.MALE))
    Ponyta = (77, "Ponyta", (Gender.FEMALE, Gender.MALE))
    Rapidash = (78, "Rapidash", (Gender.FEMALE, Gender.MALE))
    Slowpoke = (79, "Slowpoke", (Gender.FEMALE, Gender.MALE))
    Slowbro = (80, "Slowbro", (Gender.FEMALE, Gender.MALE))
    Magnemite = (81, "Magnemite", (Gender.GENDERLESS,))
    Magneton = (82, "Magneton", (Gender.GENDERLESS,))
    d = (83, "Farfetch'd", (Gender.FEMALE, Gender.MALE))
    Doduo = (84, "Doduo", (Gender.FEMALE, Gender.MALE))
    Dodrio = (85, "Dodrio", (Gender.FEMALE, Gender.MALE))
    Seel = (86, "Seel", (Gender.FEMALE, Gender.MALE))
    Dewgong = (87, "Dewgong", (Gender.FEMALE, Gender.MALE))
    Grimer = (88, "Grimer", (Gender.FEMALE, Gender.MALE))
    Muk = (89, "Muk", (Gender.FEMALE, Gender.MALE))
    Shellder = (90, "Shellder", (Gender.FEMALE, Gender.MALE))
    Cloyster = (91, "Cloyster", (Gender.FEMALE, Gender.MALE))
    Gastly = (92, "Gastly", (Gender.FEMALE, Gender.MALE))
    Haunter = (93, "Haunter", (Gender.FEMALE, Gender.MALE))
    Gengar = (94, "Gengar", (Gender.FEMALE, Gender.MALE))
    Onix = (95, "Onix", (Gender.FEMALE, Gender.MALE))
    Drowzee = (96, "Drowzee", (Gender.FEMALE, Gender.MALE))
    Hypno = (97, "Hypno", (Gender.FEMALE, Gender.MALE))
    Krabby = (98, "Krabby", (Gender.FEMALE, Gender.MALE))
    Kingler = (99, "Kingler", (Gender.FEMALE, Gender.MALE))
    Voltorb = (100, "Voltorb", (Gender.FEMALE, Gender.MALE))
    Electrode = (101, "Electrode", (Gender.GENDERLESS,))
    Exeggcute = (102, "Exeggcute", (Gender.FEMALE, Gender.MALE))
    Exeggutor = (103, "Exeggutor", (Gender.FEMALE, Gender.MALE))
    Cubone = (104, "Cubone", (Gender.FEMALE, Gender.MALE))
    Marowak = (105, "Marowak", (Gender.FEMALE, Gender.MALE))
    Hitmonlee = (106, "Hitmonlee", (Gender.FEMALE, Gender.MALE))
    Hitmonchan = (107, "Hitmonchan", (Gender.FEMALE, Gender.MALE))
    Lickitung = (108, "Lickitung", (Gender.FEMALE, Gender.MALE))
    Koffing = (109, "Koffing", (Gender.FEMALE, Gender.MALE))
    Weezing = (110, "Weezing", (Gender.FEMALE, Gender.MALE))
    Rhyhorn = (111, "Rhyhorn", (Gender.FEMALE, Gender.MALE))
    Rhydon = (112, "Rhydon", (Gender.FEMALE, Gender.MALE))
    Chansey = (113, "Chansey", (Gender.FEMALE, Gender.MALE))
    Tangela = (114, "Tangela", (Gender.FEMALE, Gender.MALE))
    Kangaskhan = (115, "Kangaskhan", (Gender.FEMALE, Gender.MALE))
    Horsea = (116, "Horsea", (Gender.FEMALE, Gender.MALE))
    Seadra = (117, "Seadra", (Gender.FEMALE, Gender.MALE))
    Goldeen = (118, "Goldeen", (Gender.FEMALE, Gender.MALE))
    Seaking = (119, "Seaking", (Gender.FEMALE, Gender.MALE))
    Staryu = (120, "Staryu", (Gender.FEMALE, Gender.MALE))
    Starmie = (121, "Starmie", (Gender.FEMALE, Gender.MALE))
    Mime = (122, "Mr. Mime", (Gender.FEMALE, Gender.MALE))
    Scyther = (123, "Scyther", (Gender.FEMALE, Gender.MALE))
    Jynx = (124, "Jynx", (Gender.FEMALE, Gender.MALE))
    Electabuzz = (125, "Electabuzz", (Gender.FEMALE, Gender.MALE))
    Magmar = (126, "Magmar", (Gender.FEMALE, Gender.MALE))
    Pinsir = (127, "Pinsir", (Gender.FEMALE, Gender.MALE))
    Tauros = (128, "Tauros", (Gender.FEMALE, Gender.MALE))
    Magikarp = (129, "Magikarp", (Gender.FEMALE, Gender.MALE))
    Gyarados = (130, "Gyarados", (Gender.FEMALE, Gender.MALE))
    Lapras = (131, "Lapras", (Gender.FEMALE, Gender.MALE))
    Ditto = (132, "Ditto", (Gender.GENDERLESS,))
    Eevee = (133, "Eevee", (Gender.FEMALE, Gender.MALE))
    Vaporeon = (134, "Vaporeon", (Gender.FEMALE, Gender.MALE))
    Jolteon = (135, "Jolteon", (Gender.FEMALE, Gender.MALE))
    Flareon = (136, "Flareon", (Gender.FEMALE, Gender.MALE))
    Porygon = (137, "Porygon", (Gender.FEMALE, Gender.MALE))
    Omanyte = (138, "Omanyte", (Gender.FEMALE, Gender.MALE))
    Omastar = (139, "Omastar", (Gender.FEMALE, Gender.MALE))
    Kabuto = (140, "Kabuto", (Gender.FEMALE, Gender.MALE))
    Kabutops = (141, "Kabutops", (Gender.FEMALE, Gender.MALE))
    Aerodactyl = (142, "Aerodactyl", (Gender.FEMALE, Gender.MALE))
    Snorlax = (143, "Snorlax", (Gender.FEMALE, Gender.MALE))
    Articuno = (144, "Articuno", (Gender.GENDERLESS,))
    Zapdos = (145, "Zapdos", (Gender.FEMALE, Gender.MALE))
    Moltres = (146, "Moltres", (Gender.GENDERLESS,))
    Dratini = (147, "Dratini", (Gender.FEMALE, Gender.MALE))
    Dragonair = (148, "Dragonair", (Gender.FEMALE, Gender.MALE))
    Dragonite = (149, "Dragonite", (Gender.FEMALE, Gender.MALE))
    Mewtwo = (150, "Mewtwo", (Gender.GENDERLESS,))
    Mew = (151, "Mew", (Gender.GENDERLESS,))
    Chikorita = (152, "Chikorita", (Gender.FEMALE, Gender.MALE))
    Bayleef = (153, "Bayleef", (Gender.FEMALE, Gender.MALE))
    Meganium = (154, "Meganium", (Gender.FEMALE, Gender.MALE))
    Cyndaquil = (155, "Cyndaquil", (Gender.FEMALE, Gender.MALE))
    Quilava = (156, "Quilava", (Gender.FEMALE, Gender.MALE))
    Typhlosion = (157, "Typhlosion", (Gender.FEMALE, Gender.MALE))
    Totodile = (158, "Totodile", (Gender.FEMALE, Gender.MALE))
    Croconaw = (159, "Croconaw", (Gender.FEMALE, Gender.MALE))
    Feraligatr = (160, "Feraligatr", (Gender.FEMALE, Gender.MALE))
    Sentret = (161, "Sentret", (Gender.FEMALE, Gender.MALE))
    Furret = (162, "Furret", (Gender.FEMALE, Gender.MALE))
    Hoothoot = (163, "Hoothoot", (Gender.FEMALE, Gender.MALE))
    Noctowl = (164, "Noctowl", (Gender.FEMALE, Gender.MALE))
    Ledyba = (165, "Ledyba", (Gender.FEMALE, Gender.MALE))
    Ledian = (166, "Ledian", (Gender.FEMALE, Gender.MALE))
    Spinarak = (167, "Spinarak", (Gender.FEMALE, Gender.MALE))
    Ariados = (168, "Ariados", (Gender.FEMALE, Gender.MALE))
    Crobat = (169, "Crobat", (Gender.FEMALE, Gender.MALE))
    Chinchou = (170, "Chinchou", (Gender.FEMALE, Gender.MALE))
    Lanturn = (171, "Lanturn", (Gender.FEMALE, Gender.MALE))
    Pichu = (172, "Pichu", (Gender.FEMALE, Gender.MALE))
    Cleffa = (173, "Cleffa", (Gender.FEMALE, Gender.MALE))
    Igglybuff = (174, "Igglybuff", (Gender.FEMALE, Gender.MALE))
    Togepi = (175, "Togepi", (Gender.FEMALE, Gender.MALE))
    Togetic = (176, "Togetic", (Gender.FEMALE, Gender.MALE))
    Natu = (177, "Natu", (Gender.FEMALE, Gender.MALE))
    Xatu = (178, "Xatu", (Gender.FEMALE, Gender.MALE))
    Mareep = (179, "Mareep", (Gender.FEMALE, Gender.MALE))
    Flaaffy = (180, "Flaaffy", (Gender.FEMALE, Gender.MALE))
    Ampharos = (181, "Ampharos", (Gender.FEMALE, Gender.MALE))
    Bellossom = (182, "Bellossom", (Gender.FEMALE, Gender.MALE))
    Marill = (183, "Marill", (Gender.FEMALE, Gender.MALE))
    Azumarill = (184, "Azumarill", (Gender.FEMALE, Gender.MALE))
    Sudowoodo = (185, "Sudowoodo", (Gender.FEMALE, Gender.MALE))
    Politoed = (186, "Politoed", (Gender.FEMALE, Gender.MALE))
    Hoppip = (187, "Hoppip", (Gender.FEMALE, Gender.MALE))
    Skiploom = (188, "Skiploom", (Gender.FEMALE, Gender.MALE))
    Jumpluff = (189, "Jumpluff", (Gender.FEMALE, Gender.MALE))
    Aipom = (190, "Aipom", (Gender.FEMALE, Gender.MALE))
    Sunkern = (191, "Sunkern", (Gender.FEMALE, Gender.MALE))
    Sunflora = (192, "Sunflora", (Gender.FEMALE, Gender.MALE))
    Yanma = (193, "Yanma", (Gender.FEMALE, Gender.MALE))
    Wooper = (194, "Wooper", (Gender.FEMALE, Gender.MALE))
    Quagsire = (195, "Quagsire", (Gender.FEMALE, Gender.MALE))
    Espeon = (196, "Espeon", (Gender.FEMALE, Gender.MALE))
    Umbreon = (197, "Umbreon", (Gender.FEMALE, Gender.MALE))
    Murkrow = (198, "Murkrow", (Gender.FEMALE, Gender.MALE))
    Slowking = (199, "Slowking", (Gender.FEMALE, Gender.MALE))
    Misdreavus = (200, "Misdreavus", (Gender.FEMALE, Gender.MALE))
    Unown = (201, "Unown", (Gender.FEMALE, Gender.MALE), tuple(UnownForm))
    Wobbuffet = (202, "Wobbuffet", (Gender.FEMALE, Gender.MALE))
    Girafarig = (203, "Girafarig", (Gender.FEMALE, Gender.MALE))
    Pineco = (204, "Pineco", (Gender.FEMALE, Gender.MALE))
    Forretress = (205, "Forretress", (Gender.FEMALE, Gender.MALE))
    Dunsparce = (206, "Dunsparce", (Gender.FEMALE, Gender.MALE))
    Gligar = (207, "Gligar", (Gender.FEMALE, Gender.MALE))
    Steelix = (208, "Steelix", (Gender.FEMALE, Gender.MALE))
    Snubbull = (209, "Snubbull", (Gender.FEMALE, Gender.MALE))
    Granbull = (210, "Granbull", (Gender.FEMALE, Gender.MALE))
    Qwilfish = (211, "Qwilfish", (Gender.FEMALE, Gender.MALE))
    Scizor = (212, "Scizor", (Gender.FEMALE, Gender.MALE))
    Shuckle = (213, "Shuckle", (Gender.FEMALE, Gender.MALE))
    Heracross = (214, "Heracross", (Gender.FEMALE, Gender.MALE))
    Sneasel = (215, "Sneasel", (Gender.FEMALE, Gender.MALE))
    Teddiursa = (216, "Teddiursa", (Gender.FEMALE, Gender.MALE))
    Ursaring = (217, "Ursaring", (Gender.FEMALE, Gender.MALE))
    Slugma = (218, "Slugma", (Gender.FEMALE, Gender.MALE))
    Magcargo = (219, "Magcargo", (Gender.FEMALE, Gender.MALE))
    Swinub = (220, "Swinub", (Gender.FEMALE, Gender.MALE))
    Piloswine = (221, "Piloswine", (Gender.FEMALE, Gender.MALE))
    Corsola = (222, "Corsola", (Gender.FEMALE, Gender.MALE))
    Remoraid = (223, "Remoraid", (Gender.FEMALE, Gender.MALE))
    Octillery = (224, "Octillery", (Gender.FEMALE, Gender.MALE))
    Delibird = (225, "Delibird", (Gender.FEMALE, Gender.MALE))
    Mantine = (226, "Mantine", (Gender.FEMALE, Gender.MALE))
    Skarmory = (227, "Skarmory", (Gender.FEMALE, Gender.MALE))
    Houndour = (228, "Houndour", (Gender.FEMALE, Gender.MALE))
    Houndoom = (229, "Houndoom", (Gender.FEMALE, Gender.MALE))
    Kingdra = (230, "Kingdra", (Gender.FEMALE, Gender.MALE))
    Phanpy = (231, "Phanpy", (Gender.FEMALE, Gender.MALE))
    Donphan = (232, "Donphan", (Gender.FEMALE, Gender.MALE))
    Porygon2 = (233, "Porygon2", (Gender.FEMALE, Gender.MALE))
    Stantler = (234, "Stantler", (Gender.FEMALE, Gender.MALE))
    Smeargle = (235, "Smeargle", (Gender.FEMALE, Gender.MALE))
    Tyrogue = (236, "Tyrogue", (Gender.FEMALE, Gender.MALE))
    Hitmontop = (237, "Hitmontop", (Gender.FEMALE, Gender.MALE))
    Smoochum = (238, "Smoochum", (Gender.FEMALE, Gender.MALE))
    Elekid = (239, "Elekid", (Gender.FEMALE, Gender.MALE))
    Magby = (240, "Magby", (Gender.FEMALE, Gender.MALE))
    Miltank = (241, "Miltank", (Gender.FEMALE, Gender.MALE))
    Blissey = (242, "Blissey", (Gender.FEMALE, Gender.MALE))
    Raikou = (243, "Raikou", (Gender.FEMALE, Gender.MALE))
    Entei = (244, "Entei", (Gender.GENDERLESS,))
    Suicune = (245, "Suicune", (Gender.FEMALE, Gender.MALE))
    Larvitar = (246, "Larvitar", (Gender.FEMALE, Gender.MALE))
    Pupitar = (247, "Pupitar", (Gender.FEMALE, Gender.MALE))
    Tyranitar = (248, "Tyranitar", (Gender.FEMALE, Gender.MALE))
    Lugia = (249, "Lugia", (Gender.GENDERLESS,))
    HoOh = (250, "Ho-oh", (Gender.GENDERLESS,))
    Celebi = (251, "Celebi", (Gender.GENDERLESS,))
    Treecko = (252, "Treecko", (Gender.FEMALE, Gender.MALE))
    Grovyle = (253, "Grovyle", (Gender.FEMALE, Gender.MALE))
    Sceptile = (254, "Sceptile", (Gender.FEMALE, Gender.MALE))
    Torchic = (255, "Torchic", (Gender.FEMALE, Gender.MALE))
    Combusken = (256, "Combusken", (Gender.FEMALE, Gender.MALE))
    Blaziken = (257, "Blaziken", (Gender.FEMALE, Gender.MALE))
    Mudkip = (258, "Mudkip", (Gender.FEMALE, Gender.MALE))
    Marshtomp = (259, "Marshtomp", (Gender.FEMALE, Gender.MALE))
    Swampert = (260, "Swampert", (Gender.FEMALE, Gender.MALE))
    Poochyena = (261, "Poochyena", (Gender.FEMALE, Gender.MALE))
    Mightyena = (262, "Mightyena", (Gender.FEMALE, Gender.MALE))
    Zigzagoon = (263, "Zigzagoon", (Gender.FEMALE, Gender.MALE))
    Linoone = (264, "Linoone", (Gender.FEMALE, Gender.MALE))
    Wurmple = (265, "Wurmple", (Gender.FEMALE, Gender.MALE))
    Silcoon = (266, "Silcoon", (Gender.FEMALE, Gender.MALE))
    Beautifly = (267, "Beautifly", (Gender.FEMALE, Gender.MALE))
    Cascoon = (268, "Cascoon", (Gender.FEMALE, Gender.MALE))
    Dustox = (269, "Dustox", (Gender.FEMALE, Gender.MALE))
    Lotad = (270, "Lotad", (Gender.FEMALE, Gender.MALE))
    Lombre = (271, "Lombre", (Gender.FEMALE, Gender.MALE))
    Ludicolo = (272, "Ludicolo", (Gender.FEMALE, Gender.MALE))
    Seedot = (273, "Seedot", (Gender.FEMALE, Gender.MALE))
    Nuzleaf = (274, "Nuzleaf", (Gender.FEMALE, Gender.MALE))
    Shiftry = (275, "Shiftry", (Gender.FEMALE, Gender.MALE))
    Taillow = (276, "Taillow", (Gender.FEMALE, Gender.MALE))
    Swellow = (277, "Swellow", (Gender.FEMALE, Gender.MALE))
    Wingull = (278, "Wingull", (Gender.FEMALE, Gender.MALE))
    Pelipper = (279, "Pelipper", (Gender.FEMALE, Gender.MALE))
    Ralts = (280, "Ralts", (Gender.FEMALE, Gender.MALE))
    Kirlia = (281, "Kirlia", (Gender.FEMALE, Gender.MALE))
    Gardevoir = (282, "Gardevoir", (Gender.FEMALE, Gender.MALE))
    Surskit = (283, "Surskit", (Gender.FEMALE, Gender.MALE))
    Masquerain = (284, "Masquerain", (Gender.FEMALE, Gender.MALE))
    Shroomish = (285, "Shroomish", (Gender.FEMALE, Gender.MALE))
    Breloom = (286, "Breloom", (Gender.FEMALE, Gender.MALE))
    Slakoth = (287, "Slakoth", (Gender.FEMALE, Gender.MALE))
    Vigoroth = (288, "Vigoroth", (Gender.FEMALE, Gender.MALE))
    Slaking = (289, "Slaking", (Gender.FEMALE, Gender.MALE))
    Nincada = (290, "Nincada", (Gender.FEMALE, Gender.MALE))
    Ninjask = (291, "Ninjask", (Gender.FEMALE, Gender.MALE))
    Shedinja = (292, "Shedinja", (Gender.FEMALE, Gender.MALE))
    Whismur = (293, "Whismur", (Gender.FEMALE, Gender.MALE))
    Loudred = (294, "Loudred", (Gender.FEMALE, Gender.MALE))
    Exploud = (295, "Exploud", (Gender.FEMALE, Gender.MALE))
    Makuhita = (296, "Makuhita", (Gender.FEMALE, Gender.MALE))
    Hariyama = (297, "Hariyama", (Gender.FEMALE, Gender.MALE))
    Azurill = (298, "Azurill", (Gender.FEMALE, Gender.MALE))
    Nosepass = (299, "Nosepass", (Gender.FEMALE, Gender.MALE))
    Skitty = (300, "Skitty", (Gender.FEMALE, Gender.MALE))
    Delcatty = (301, "Delcatty", (Gender.FEMALE, Gender.MALE))
    Sableye = (302, "Sableye", (Gender.FEMALE, Gender.MALE))
    Mawile = (303, "Mawile", (Gender.FEMALE, Gender.MALE))
    Aron = (304, "Aron", (Gender.FEMALE, Gender.MALE))
    Lairon = (305, "Lairon", (Gender.FEMALE, Gender.MALE))
    Aggron = (306, "Aggron", (Gender.FEMALE, Gender.MALE))
    Meditite = (307, "Meditite", (Gender.FEMALE, Gender.MALE))
    Medicham = (308, "Medicham", (Gender.FEMALE, Gender.MALE))
    Electrike = (309, "Electrike", (Gender.FEMALE, Gender.MALE))
    Manectric = (310, "Manectric", (Gender.FEMALE, Gender.MALE))
    Plusle = (311, "Plusle", (Gender.FEMALE, Gender.MALE))
    Minun = (312, "Minun", (Gender.FEMALE, Gender.MALE))
    Volbeat = (313, "Volbeat", (Gender.MALE,))
    Illumise = (314, "Illumise", (Gender.FEMALE,))
    Roselia = (315, "Roselia", (Gender.FEMALE, Gender.MALE))
    Gulpin = (316, "Gulpin", (Gender.FEMALE, Gender.MALE))
    Swalot = (317, "Swalot", (Gender.FEMALE, Gender.MALE))
    Carvanha = (318, "Carvanha", (Gender.FEMALE, Gender.MALE))
    Sharpedo = (319, "Sharpedo", (Gender.FEMALE, Gender.MALE))
    Wailmer = (320, "Wailmer", (Gender.FEMALE, Gender.MALE))
    Wailord = (321, "Wailord", (Gender.FEMALE, Gender.MALE))
    Numel = (322, "Numel", (Gender.FEMALE, Gender.MALE))
    Camerupt = (323, "Camerupt", (Gender.FEMALE, Gender.MALE))
    Torkoal = (324, "Torkoal", (Gender.FEMALE, Gender.MALE))
    Spoink = (325, "Spoink", (Gender.FEMALE, Gender.MALE))
    Grumpig = (326, "Grumpig", (Gender.FEMALE, Gender.MALE))
    Spinda = (327, "Spinda", (Gender.FEMALE, Gender.MALE))
    Trapinch = (328, "Trapinch", (Gender.FEMALE, Gender.MALE))
    Vibrava = (329, "Vibrava", (Gender.FEMALE, Gender.MALE))
    Flygon = (330, "Flygon", (Gender.FEMALE, Gender.MALE))
    Cacnea = (331, "Cacnea", (Gender.FEMALE, Gender.MALE))
    Cacturne = (332, "Cacturne", (Gender.FEMALE, Gender.MALE))
    Swablu = (333, "Swablu", (Gender.FEMALE, Gender.MALE))
    Altaria = (334, "Altaria", (Gender.FEMALE, Gender.MALE))
    Zangoose = (335, "Zangoose", (Gender.FEMALE, Gender.MALE))
    Seviper = (336, "Seviper", (Gender.FEMALE, Gender.MALE))
    Lunatone = (337, "Lunatone", (Gender.GENDERLESS,))
    Solrock = (338, "Solrock", (Gender.FEMALE, Gender.MALE))
    Barboach = (339, "Barboach", (Gender.FEMALE, Gender.MALE))
    Whiscash = (340, "Whiscash", (Gender.FEMALE, Gender.MALE))
    Corphish = (341, "Corphish", (Gender.FEMALE, Gender.MALE))
    Crawdaunt = (342, "Crawdaunt", (Gender.FEMALE, Gender.MALE))
    Baltoy = (343, "Baltoy", (Gender.GENDERLESS,))
    Claydol = (344, "Claydol", (Gender.GENDERLESS,))
    Lileep = (345, "Lileep", (Gender.FEMALE, Gender.MALE))
    Cradily = (346, "Cradily", (Gender.FEMALE, Gender.MALE))
    Anorith = (347, "Anorith", (Gender.FEMALE, Gender.MALE))
    Armaldo = (348, "Armaldo", (Gender.FEMALE, Gender.MALE))
    Feebas = (349, "Feebas", (Gender.FEMALE, Gender.MALE))
    Milotic = (350, "Milotic", (Gender.FEMALE, Gender.MALE))
    Castform = (351, "Castform", (Gender.FEMALE, Gender.MALE))
    Kecleon = (352, "Kecleon", (Gender.FEMALE, Gender.MALE))
    Shuppet = (353, "Shuppet", (Gender.FEMALE, Gender.MALE))
    Banette = (354, "Banette", (Gender.FEMALE, Gender.MALE))
    Duskull = (355, "Duskull", (Gender.FEMALE, Gender.MALE))
    Dusclops = (356, "Dusclops", (Gender.FEMALE, Gender.MALE))
    Tropius = (357, "Tropius", (Gender.FEMALE, Gender.MALE))
    Chimecho = (358, "Chimecho", (Gender.FEMALE, Gender.MALE))
    Absol = (359, "Absol", (Gender.FEMALE, Gender.MALE))
    Wynaut = (360, "Wynaut", (Gender.FEMALE, Gender.MALE))
    Snorunt = (361, "Snorunt", (Gender.FEMALE, Gender.MALE))
    Glalie = (362, "Glalie", (Gender.FEMALE, Gender.MALE))
    Spheal = (363, "Spheal", (Gender.FEMALE, Gender.MALE))
    Sealeo = (364, "Sealeo", (Gender.FEMALE, Gender.MALE))
    Walrein = (365, "Walrein", (Gender.FEMALE, Gender.MALE))
    Clamperl = (366, "Clamperl", (Gender.FEMALE, Gender.MALE))
    Huntail = (367, "Huntail", (Gender.FEMALE, Gender.MALE))
    Gorebyss = (368, "Gorebyss", (Gender.FEMALE, Gender.MALE))
    Relicanth = (369, "Relicanth", (Gender.FEMALE, Gender.MALE))
    Luvdisc = (370, "Luvdisc", (Gender.FEMALE, Gender.MALE))
    Bagon = (371, "Bagon", (Gender.FEMALE, Gender.MALE))
    Shelgon = (372, "Shelgon", (Gender.FEMALE, Gender.MALE))
    Salamence = (373, "Salamence", (Gender.FEMALE, Gender.MALE))
    Beldum = (374, "Beldum", (Gender.GENDERLESS,))
    Metang = (375, "Metang", (Gender.GENDERLESS,))
    Metagross = (376, "Metagross", (Gender.GENDERLESS,))
    Regirock = (377, "Regirock", (Gender.FEMALE, Gender.MALE))
    Regice = (378, "Regice", (Gender.FEMALE, Gender.MALE))
    Registeel = (379, "Registeel", (Gender.FEMALE, Gender.MALE))
    Latias = (380, "Latias", (Gender.FEMALE, Gender.MALE))
    Latios = (381, "Latios", (Gender.FEMALE, Gender.MALE))
    Kyogre = (382, "Kyogre", (Gender.GENDERLESS,))
    Groudon = (383, "Groudon", (Gender.GENDERLESS,))
    Rayquaza = (384, "Rayquaza", (Gender.FEMALE, Gender.MALE))
    Jirachi = (385, "Jirachi", (Gender.GENDERLESS,))
    Deoxys = (386, "Deoxys", (Gender.GENDERLESS,))
    Turtwig = (387, "Turtwig", (Gender.FEMALE, Gender.MALE))
    Grotle = (388, "Grotle", (Gender.FEMALE, Gender.MALE))
    Torterra = (389, "Torterra", (Gender.FEMALE, Gender.MALE))
    Chimchar = (390, "Chimchar", (Gender.FEMALE, Gender.MALE))
    Monferno = (391, "Monferno", (Gender.FEMALE, Gender.MALE))
    Infernape = (392, "Infernape", (Gender.FEMALE, Gender.MALE))
    Piplup = (393, "Piplup", (Gender.FEMALE, Gender.MALE))
    Prinplup = (394, "Prinplup", (Gender.FEMALE, Gender.MALE))
    Empoleon = (395, "Empoleon", (Gender.FEMALE, Gender.MALE))
    Starly = (396, "Starly", (Gender.FEMALE, Gender.MALE))
    Staravia = (397, "Staravia", (Gender.FEMALE, Gender.MALE))
    Staraptor = (398, "Staraptor", (Gender.FEMALE, Gender.MALE))
    Bidoof = (399, "Bidoof", (Gender.FEMALE, Gender.MALE))
    Bibarel = (400, "Bibarel", (Gender.FEMALE, Gender.MALE))
    Kricketot = (401, "Kricketot", (Gender.FEMALE, Gender.MALE))
    Kricketune = (402, "Kricketune", (Gender.FEMALE, Gender.MALE))
    Shinx = (403, "Shinx", (Gender.FEMALE, Gender.MALE))
    Luxio = (404, "Luxio", (Gender.FEMALE, Gender.MALE))
    Luxray = (405, "Luxray", (Gender.FEMALE, Gender.MALE))
    Budew = (406, "Budew", (Gender.FEMALE, Gender.MALE))
    Roserade = (407, "Roserade", (Gender.FEMALE, Gender.MALE))
    Cranidos = (408, "Cranidos", (Gender.FEMALE, Gender.MALE))
    Rampardos = (409, "Rampardos", (Gender.FEMALE, Gender.MALE))
    Shieldon = (410, "Shieldon", (Gender.FEMALE, Gender.MALE))
    Bastiodon = (411, "Bastiodon", (Gender.FEMALE, Gender.MALE))
    Burmy = (412, "Burmy", (Gender.FEMALE, Gender.MALE), tuple(BurmyWormadamForm))
    Wormadam = (413, "Wormadam", (Gender.FEMALE, Gender.MALE), tuple(BurmyWormadamForm))
    Mothim = (414, "Mothim", (Gender.FEMALE, Gender.MALE))
    Combee = (415, "Combee", (Gender.FEMALE, Gender.MALE))
    Vespiquen = (416, "Vespiquen", (Gender.FEMALE, Gender.MALE))
    Pachirisu = (417, "Pachirisu", (Gender.FEMALE, Gender.MALE))
    Buizel = (418, "Buizel", (Gender.FEMALE, Gender.MALE))
    Floatzel = (419, "Floatzel", (Gender.FEMALE, Gender.MALE))
    Cherubi = (420, "Cherubi", (Gender.FEMALE, Gender.MALE))
    Cherrim = (421, "Cherrim", (Gender.FEMALE, Gender.MALE))
    Shellos = (422, "Shellos", (Gender.FEMALE, Gender.MALE), tuple(ShellosGastrodonForm))
    Gastrodon = (423, "Gastrodon", (Gender.FEMALE, Gender.MALE), tuple(ShellosGastrodonForm))
    Ambipom = (424, "Ambipom", (Gender.FEMALE, Gender.MALE))
    Drifloon = (425, "Drifloon", (Gender.FEMALE, Gender.MALE))
    Drifblim = (426, "Drifblim", (Gender.FEMALE, Gender.MALE))
    Buneary = (427, "Buneary", (Gender.FEMALE, Gender.MALE))
    Lopunny = (428, "Lopunny", (Gender.FEMALE, Gender.MALE))
    Mismagius = (429, "Mismagius", (Gender.FEMALE, Gender.MALE))
    Honchkrow = (430, "Honchkrow", (Gender.FEMALE, Gender.MALE))
    Glameow = (431, "Glameow", (Gender.FEMALE, Gender.MALE))
    Purugly = (432, "Purugly", (Gender.FEMALE, Gender.MALE))
    Chingling = (433, "Chingling", (Gender.FEMALE, Gender.MALE))
    Stunky = (434, "Stunky", (Gender.FEMALE, Gender.MALE))
    Skuntank = (435, "Skuntank", (Gender.FEMALE, Gender.MALE))
    Bronzor = (436, "Bronzor", (Gender.GENDERLESS,))
    Bronzong = (437, "Bronzong", (Gender.GENDERLESS,))
    Bonsly = (438, "Bonsly", (Gender.FEMALE, Gender.MALE))
    MimeJr = (439, "Mime Jr.", (Gender.FEMALE, Gender.MALE))
    Happiny = (440, "Happiny", (Gender.FEMALE, Gender.MALE))
    Chatot = (441, "Chatot", (Gender.FEMALE, Gender.MALE))
    Spiritomb = (442, "Spiritomb", (Gender.FEMALE, Gender.MALE))
    Gible = (443, "Gible", (Gender.FEMALE, Gender.MALE))
    Gabite = (444, "Gabite", (Gender.FEMALE, Gender.MALE))
    Garchomp = (445, "Garchomp", (Gender.FEMALE, Gender.MALE))
    Munchlax = (446, "Munchlax", (Gender.FEMALE, Gender.MALE))
    Riolu = (447, "Riolu", (Gender.FEMALE, Gender.MALE))
    Lucario = (448, "Lucario", (Gender.FEMALE, Gender.MALE))
    Hippopotas = (449, "Hippopotas", (Gender.FEMALE, Gender.MALE))
    Hippowdon = (450, "Hippowdon", (Gender.FEMALE, Gender.MALE))
    Skorupi = (451, "Skorupi", (Gender.FEMALE, Gender.MALE))
    Drapion = (452, "Drapion", (Gender.FEMALE, Gender.MALE))
    Croagunk = (453, "Croagunk", (Gender.FEMALE, Gender.MALE))
    Toxicroak = (454, "Toxicroak", (Gender.FEMALE, Gender.MALE))
    Carnivine = (455, "Carnivine", (Gender.FEMALE, Gender.MALE))
    Finneon = (456, "Finneon", (Gender.FEMALE, Gender.MALE))
    Lumineon = (457, "Lumineon", (Gender.FEMALE, Gender.MALE))
    Mantyke = (458, "Mantyke", (Gender.FEMALE, Gender.MALE))
    Snover = (459, "Snover", (Gender.FEMALE, Gender.MALE))
    Abomasnow = (460, "Abomasnow", (Gender.FEMALE, Gender.MALE))
    Weavile = (461, "Weavile", (Gender.FEMALE, Gender.MALE))
    Magnezone = (462, "Magnezone", (Gender.GENDERLESS,))
    Lickilicky = (463, "Lickilicky", (Gender.FEMALE, Gender.MALE))
    Rhyperior = (464, "Rhyperior", (Gender.FEMALE, Gender.MALE))
    Tangrowth = (465, "Tangrowth", (Gender.FEMALE, Gender.MALE))
    Electivire = (466, "Electivire", (Gender.FEMALE, Gender.MALE))
    Magmortar = (467, "Magmortar", (Gender.FEMALE, Gender.MALE))
    Togekiss = (468, "Togekiss", (Gender.FEMALE, Gender.MALE))
    Yanmega = (469, "Yanmega", (Gender.FEMALE, Gender.MALE))
    Leafeon = (470, "Leafeon", (Gender.FEMALE, Gender.MALE))
    Glaceon = (471, "Glaceon", (Gender.FEMALE, Gender.MALE))
    Gliscor = (472, "Gliscor", (Gender.FEMALE, Gender.MALE))
    Mamoswine = (473, "Mamoswine", (Gender.FEMALE, Gender.MALE))
    PorygonZ = (474, "Porygon-Z", (Gender.FEMALE, Gender.MALE))
    Gallade = (475, "Gallade", (Gender.FEMALE, Gender.MALE))
    Probopass = (476, "Probopass", (Gender.FEMALE, Gender.MALE))
    Dusknoir = (477, "Dusknoir", (Gender.FEMALE, Gender.MALE))
    Froslass = (478, "Froslass", (Gender.FEMALE, Gender.MALE))
    Rotom = (479, "Rotom", (Gender.FEMALE, Gender.MALE), tuple(RotomForm))
    Uxie = (480, "Uxie", (Gender.FEMALE, Gender.MALE))
    Mesprit = (481, "Mesprit", (Gender.GENDERLESS,))
    Azelf = (482, "Azelf", (Gender.GENDERLESS,))
    Dialga = (483, "Dialga", (Gender.GENDERLESS,))
    Palkia = (484, "Palkia", (Gender.FEMALE, Gender.MALE))
    Heatran = (485, "Heatran", (Gender.FEMALE, Gender.MALE))
    Regigigas = (486, "Regigigas", (Gender.FEMALE, Gender.MALE))
    Giratina = (487, "Giratina", (Gender.GENDERLESS,))
    Cresselia = (488, "Cresselia", (Gender.FEMALE, Gender.MALE))
    Phione = (489, "Phione", (Gender.FEMALE, Gender.MALE))
    Manaphy = (490, "Manaphy", (Gender.GENDERLESS,))
    Darkrai = (491, "Darkrai", (Gender.GENDERLESS,))
    Shaymin = (492, "Shaymin", (Gender.FEMALE, Gender.MALE), tuple(ShayminFrom))
    Arceus = (493, "Arceus", (Gender.GENDERLESS,), tuple(ArceusForm))

    def __new__(
        cls,
        national_no: int,
        title: str,
        available_genders: tuple[Gender, ...],
        available_forms: tuple[Form, ...] = tuple(),
    ) -> "PokemonType":
        instance = int.__new__(cls, national_no)
        instance._value_ = national_no
        instance.national_no = national_no
        instance.title = title
        instance.available_genders = available_genders
        instance.available_forms = available_forms

        return instance
