# database.py

PERKS_DB = {
    "Armor": {
        "HP UP": {"d": "Aumenta significativamente seus pontos de vida.", "v": "11% (S)"},
        "Rough Skin": {"d": "Chance de refletir dano recebido.", "v": "9% (S)"},
        "Fortress": {"d": "Grande bônus de defesa.", "v": "39% (S)"},
        "Attack UP": {"d": "Aumenta o dano total causado.", "v": "15% (S)"},
        "Critical Eye": {"d": "Aumenta a chance de críticos.", "v": "12% (S)"},
        "Brawler": {"d": "Dano extra próximo a inimigos.", "v": "45% (S)"}
    },
    "Weapon": {
        "Boss Damage": {"d": "Dano massivo contra chefes.", "v": "25% (S)"},
        "Executioner": {"d": "Dano extra a inimigos com pouco HP.", "v": "50% (S)"},
        "Lifesteal": {"d": "Recupera HP a cada golpe.", "v": "5% (S)"},
        "Stun Hit": {"d": "Chance de atordoar o alvo.", "v": "8% (S)"},
        "Block Rate": {"d": "Aumenta chance de mitigar dano.", "v": "15% (S)"}
    },
    "Pet": {
        "Burn Aura": {"d": "Dano de fogo ao redor do pet.", "v": "Lvl 50"},
        "Fire Mastery": {"d": "Fortalece elemento fogo.", "v": "Max"},
        "Shell": {"d": "Barreira que reduz o dano.", "v": "S"},
        "Taunt": {"d": "Atrai atenção dos monstros.", "v": "Max"}
    }
}

BUILDS_DB = {
    "FULL DPS": {
        "stats": {"Dano": 98, "Defesa": 25, "Velocidade": 65, "Sorte": 30},
        "classes_recomendadas": ["Swordmaster", "Arcane Mage", "Dualwilder"],
        "armor": {"nome": "Zero Armor", "stars": "★★★★★★", "perks": ["Attack UP", "Critical Eye", "Brawler"]},
        "weapons": [{"nome": "Void Blade", "stars": "★★★★★★", "tipo": "Primary Weapon", "perks": ["Boss Damage", "Executioner", "Lifesteal"]}],
        "pet": {"nome": "Phoenix", "stars": "★★★★★", "perks": ["Burn Aura", "Fire Mastery", "Attack UP"]}
    },
    "FULL TANK": {
        "stats": {"Dano": 35, "Defesa": 100, "Velocidade": 30, "Sorte": 45},
        "classes_recomendadas": ["Defender", "Guardian"],
        "armor": {"nome": "Guardian Plate", "stars": "★★★★★★", "perks": ["HP UP", "Rough Skin", "Fortress"]},
        "weapons": [{"nome": "Bulwark Hammer", "stars": "★★★★★★", "tipo": "Main Hand", "perks": ["Stun Hit", "Lifesteal", "Block Rate"]}],
        "pet": {"nome": "Turtle", "stars": "★★★★★", "perks": ["Shell", "Taunt", "HP UP"]}
    }
}

CLASSES_DB = {
    "Tier 1": {
        "Swordmaster": {
            "img": "assets/class/swordmaster.png",
            "equip": "1x Longsword", "lvl": 1, "hp_mult": "x1.0", "aggro": "x1.0",
            "lore": "Mestre da espada que foca em cortes rápidos e precisos.",
            "skills": {
                "E": {"nome": "Crescent Strike", "cd": "5s", "desc": "Ataque crescente."},
                "R": {"nome": "Leap Dash", "cd": "8s", "desc": "Salte em direção aos inimigos."},
                "X": {"nome": "Sword Cyclone", "cd": "30s", "desc": "Giro devastador com críticos."},
                "C": {"nome": "Dash", "cd": "2s", "desc": "Esquiva rápida."}
            }
        },
        "Arcane Mage": {
            "img": "assets/class/arcanemage.png",
            "equip": "Staff", "lvl": 1, "hp_mult": "x0.9", "aggro": "x1.2",
            "lore": "Mago poderoso que utiliza mana para ataques em área.",
            "skills": {
                "E": {"nome": "Arcane Blast", "cd": "5s", "desc": "Orbe explosivo de energia."},
                "R": {"nome": "Arcane Wave", "cd": "8s", "desc": "Explosões no chão."},
                "X": {"nome": "Arcane Ascension", "cd": "30s", "desc": "Orbe gigante."},
                "C": {"nome": "Dash", "cd": "2s", "desc": "Teleporte curto."}
            }
        },
        "Defender": {
            "img": "https://via.placeholder.com/400x600.png?text=Defender",
            "equip": "Shield & Hammer", "lvl": 1, "hp_mult": "x1.5", "aggro": "x2.0",
            "lore": "A muralha inquebrável que protege seus aliados.",
            "skills": {
                "E": {"nome": "Shield Bash", "cd": "6s", "desc": "Atordoa com o escudo."},
                "R": {"nome": "Iron Will", "cd": "12s", "desc": "Defesa temporária."},
                "X": {"nome": "Aegis Protection", "cd": "45s", "desc": "Redução de dano em área."},
                "C": {"nome": "Dash", "cd": "2.5s", "desc": "Avanço pesado."}
            }
        }
    },
    "Tier 2": {
        "Dualwilder": {"img": "https://via.placeholder.com/400x600.png?text=Dualwilder", "equip": "2x Swords", "lvl": 15, "hp_mult": "x1.0", "aggro": "x1.0", "lore": "Edite aqui", "skills": {"E": {"nome": "S1", "cd": "5s", "desc": "D"}, "R": {"nome": "S2", "cd": "5s", "desc": "D"}, "F": {"nome": "S3", "cd": "5s", "desc": "D"}, "X": {"nome": "S4", "cd": "5s", "desc": "D"}, "C": {"nome": "S5", "cd": "5s", "desc": "D"}}},
        "Elementalist": {"img": "https://via.placeholder.com/400x600.png?text=Elementalist", "equip": "Staff", "lvl": 15, "hp_mult": "x0.9", "aggro": "x1.2", "lore": "Edite aqui", "skills": {"E": {"nome": "S1", "cd": "5s", "desc": "D"}, "R": {"nome": "S2", "cd": "5s", "desc": "D"}, "F": {"nome": "S3", "cd": "5s", "desc": "D"}, "X": {"nome": "S4", "cd": "5s", "desc": "D"}, "C": {"nome": "S5", "cd": "5s", "desc": "D"}}},
        "Guardian": {"img": "https://via.placeholder.com/400x600.png?text=Guardian", "equip": "Shield & Sword", "lvl": 15, "hp_mult": "x1.5", "aggro": "x2.0", "lore": "Edite aqui", "skills": {"E": {"nome": "S1", "cd": "5s", "desc": "D"}, "R": {"nome": "S2", "cd": "5s", "desc": "D"}, "F": {"nome": "S3", "cd": "5s", "desc": "D"}, "X": {"nome": "S4", "cd": "5s", "desc": "D"}, "C": {"nome": "S5", "cd": "5s", "desc": "D"}}}
    },
    "Tier 3": {
        "Paladin": {"img": "https://via.placeholder.com/400x600.png?text=Paladin", "equip": "Mace", "lvl": 30, "hp_mult": "1.0", "aggro": "1.0", "lore": "Lore", "skills": {"E": {"nome": "E", "cd": "5s", "desc": "D"}, "R": {"nome": "R", "cd": "5s", "desc": "D"}, "F": {"nome": "F", "cd": "5s", "desc": "D"}, "X": {"nome": "X", "cd": "5s", "desc": "D"}, "C": {"nome": "C", "cd": "5s", "desc": "D"}}},
        "Mage of Light": {"img": "https://via.placeholder.com/400x600.png?text=MageOfLight", "equip": "Staff", "lvl": 30, "hp_mult": "1.0", "aggro": "1.0", "lore": "Lore", "skills": {"E": {"nome": "E", "cd": "5s", "desc": "D"}, "R": {"nome": "R", "cd": "5s", "desc": "D"}, "F": {"nome": "F", "cd": "5s", "desc": "D"}, "X": {"nome": "X", "cd": "5s", "desc": "D"}, "C": {"nome": "C", "cd": "5s", "desc": "D"}}},
        "Berserker": {"img": "https://via.placeholder.com/400x600.png?text=Berserker", "equip": "Greatsword", "lvl": 30, "hp_mult": "1.0", "aggro": "1.0", "lore": "Lore", "skills": {"E": {"nome": "E", "cd": "5s", "desc": "D"}, "R": {"nome": "R", "cd": "5s", "desc": "D"}, "F": {"nome": "F", "cd": "5s", "desc": "D"}, "X": {"nome": "X", "cd": "5s", "desc": "D"}, "C": {"nome": "C", "cd": "5s", "desc": "D"}}}
    },
    "Tier 4": {
        "Demon": {"img": "https://via.placeholder.com/400x600.png?text=Demon", "equip": "Scythe", "lvl": 50, "hp_mult": "1.0", "aggro": "1.0", "lore": "Lore", "skills": {"E": {"nome": "E", "cd": "5s", "desc": "D"}, "R": {"nome": "R", "cd": "5s", "desc": "D"}, "F": {"nome": "F", "cd": "5s", "desc": "D"}, "X": {"nome": "X", "cd": "5s", "desc": "D"}, "C": {"nome": "C", "cd": "5s", "desc": "D"}}},
        "Dragon": {"img": "https://via.placeholder.com/400x600.png?text=Dragon", "equip": "Gauntlets", "lvl": 50, "hp_mult": "1.0", "aggro": "1.0", "lore": "Lore", "skills": {"E": {"nome": "E", "cd": "5s", "desc": "D"}, "R": {"nome": "R", "cd": "5s", "desc": "D"}, "F": {"nome": "F", "cd": "5s", "desc": "D"}, "X": {"nome": "X", "cd": "5s", "desc": "D"}, "C": {"nome": "C", "cd": "5s", "desc": "D"}}},
        "Spirit Archer": {"img": "https://via.placeholder.com/400x600.png?text=SpiritArcher", "equip": "Bow", "lvl": 50, "hp_mult": "1.0", "aggro": "1.0", "lore": "Lore", "skills": {"E": {"nome": "E", "cd": "5s", "desc": "D"}, "R": {"nome": "R", "cd": "5s", "desc": "D"}, "F": {"nome": "F", "cd": "5s", "desc": "D"}, "X": {"nome": "X", "cd": "5s", "desc": "D"}, "C": {"nome": "C", "cd": "5s", "desc": "D"}}}
    },
    "Tier 5": {
        "Warlord": {"img": "https://via.placeholder.com/400x600.png?text=Warlord", "equip": "Sword", "lvl": 75, "hp_mult": "1.0", "aggro": "1.0", "lore": "Lore", "skills": {"E": {"nome": "E", "cd": "5s", "desc": "D"}, "R": {"nome": "R", "cd": "5s", "desc": "D"}, "F": {"nome": "F", "cd": "5s", "desc": "D"}, "X": {"nome": "X", "cd": "5s", "desc": "D"}, "C": {"nome": "C", "cd": "5s", "desc": "D"}}},
        "Summoner": {"img": "https://via.placeholder.com/400x600.png?text=Summoner", "equip": "Staff", "lvl": 75, "hp_mult": "1.0", "aggro": "1.0", "lore": "Lore", "skills": {"E": {"nome": "E", "cd": "5s", "desc": "D"}, "R": {"nome": "R", "cd": "5s", "desc": "D"}, "F": {"nome": "F", "cd": "5s", "desc": "D"}, "X": {"nome": "X", "cd": "5s", "desc": "D"}, "C": {"nome": "C", "cd": "5s", "desc": "D"}}},
        "Shadowblade": {"img": "https://via.placeholder.com/400x600.png?text=Shadowblade", "equip": "Daggers", "lvl": 75, "hp_mult": "1.0", "aggro": "1.0", "lore": "Lore", "skills": {"E": {"nome": "E", "cd": "5s", "desc": "D"}, "R": {"nome": "R", "cd": "5s", "desc": "D"}, "F": {"nome": "F", "cd": "5s", "desc": "D"}, "X": {"nome": "X", "cd": "5s", "desc": "D"}, "C": {"nome": "C", "cd": "5s", "desc": "D"}}}
    },
    "Maestria": {
        "Shadowmage": {"img": "https://via.placeholder.com/400x600.png?text=Shadowmage", "equip": "Soul Staff", "lvl": 100, "hp_mult": "1.0", "aggro": "1.0", "lore": "Lore", "skills": {"E": {"nome": "E", "cd": "5s", "desc": "D"}, "R": {"nome": "R", "cd": "5s", "desc": "D"}, "F": {"nome": "F", "cd": "5s", "desc": "D"}, "X": {"nome": "X", "cd": "5s", "desc": "D"}, "C": {"nome": "C", "cd": "5s", "desc": "D"}}},
        "Hunter": {"img": "assets/class/swordmaster.png", "equip": "Crossbow", "lvl": 100, "hp_mult": "1.0", "aggro": "1.0", "lore": "Lore", "skills": {"E": {"nome": "E", "cd": "5s", "desc": "D"}, "R": {"nome": "R", "cd": "5s", "desc": "D"}, "F": {"nome": "F", "cd": "5s", "desc": "D"}, "X": {"nome": "X", "cd": "5s", "desc": "D"}, "C": {"nome": "C", "cd": "5s", "desc": "D"}}},
        "Stormcaller": {"img": "https://via.placeholder.com/400x600.png?text=Stormcaller", "equip": "Orb", "lvl": 100, "hp_mult": "1.0", "aggro": "1.0", "lore": "Lore", "skills": {"E": {"nome": "E", "cd": "5s", "desc": "D"}, "R": {"nome": "R", "cd": "5s", "desc": "D"}, "F": {"nome": "F", "cd": "5s", "desc": "D"}, "X": {"nome": "X", "cd": "5s", "desc": "D"}, "C": {"nome": "C", "cd": "5s", "desc": "D"}}},
        "Leviathan": {"img": "https://via.placeholder.com/400x600.png?text=Leviathan", "equip": "Trident", "lvl": 100, "hp_mult": "1.0", "aggro": "1.0", "lore": "Lore", "skills": {"E": {"nome": "E", "cd": "5s", "desc": "D"}, "R": {"nome": "R", "cd": "5s", "desc": "D"}, "F": {"nome": "F", "cd": "5s", "desc": "D"}, "X": {"nome": "X", "cd": "5s", "desc": "D"}, "C": {"nome": "C", "cd": "5s", "desc": "D"}}},
        "Starbreaker": {"img": "https://via.placeholder.com/400x600.png?text=Starbreaker", "equip": "Hammer", "lvl": 100, "hp_mult": "1.0", "aggro": "1.0", "lore": "Lore", "skills": {"E": {"nome": "E", "cd": "5s", "desc": "D"}, "R": {"nome": "R", "cd": "5s", "desc": "D"}, "F": {"nome": "F", "cd": "5s", "desc": "D"}, "X": {"nome": "X", "cd": "5s", "desc": "D"}, "C": {"nome": "C", "cd": "5s", "desc": "D"}}},
        "Necromancer": {"img": "https://via.placeholder.com/400x600.png?text=Necromancer", "equip": "Grimoire", "lvl": 100, "hp_mult": "1.0", "aggro": "1.0", "lore": "Lore", "skills": {"E": {"nome": "E", "cd": "5s", "desc": "D"}, "R": {"nome": "R", "cd": "5s", "desc": "D"}, "F": {"nome": "F", "cd": "5s", "desc": "D"}, "X": {"nome": "X", "cd": "5s", "desc": "D"}, "C": {"nome": "C", "cd": "5s", "desc": "D"}}}
    }
}
