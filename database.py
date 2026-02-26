# database.py

PERKS_DB = {
    "Armor": {
        "HP UP": {"d": "Aumenta significativamente seus pontos de vida.", "v": "11% (S)"},
        "Rough Skin": {"d": "Chance de refletir dano recebido.", "v": "9% (S)"},
        "Fortress": {"d": "Grande bônus de defesa.", "v": "39% (S)"},
        "Attack UP": {"d": "Aumenta o dano total causado.", "v": "15% (S)"},
        "Critical Eye": {"d": "Aumenta a chance de críticos.", "v": "12% (S)"},
        "Brawler": {"d": "Dano extra próximo a inimigos.", "v": "45% (S)"},
        "Mana Font": {"d": "Aumenta a regeneração de mana.", "v": "20% (S)"}
    },
    "Weapon": {
        "Boss Bane": {"d": "Causa mais dano (perk % ) a chefes, mas recebe mais dano (perfil % ) deles. Esse perk afeta qualquer inimigo com barras de vida grandes.", "v": "30 % (S+)"},
        "Elite Assassin": {"d": "Causa perk % a mais de dano a monstros Elite, mas recebe perk % a mais de dano de monstros de elite.", "v": "30% (S+)"},
        "Mob Slayer": {"d": "Causa perk % a mais de dano a monstros normais, mas recebe perk % a mais de dano de monstros normais.", "v": "30% (S+)"},
        "Life Drain": {"d": "Recupere sua própria saúde em exatamente uma porcentagem do dano causado.", "v": "6% (S+)"},
        "Oblivion": {"d": "Possui uma chance de perk % de derrotar instantaneamente qualquer inimigo, mas possui um tempo de recarga de 20 segundos.", "v": "5% (S+)"},
        "Opening Strike": {"d": "Aumenta a chance de acerto crítico contra inimigos com mais de 75% de vida em perk %. (ex.: 10 %= aumento de 1, 1x). Essa vantagem é um monte de lixo (kkk).", "v": "25% (S+)"},
        "Ferocious": {"d": "Ao sofrer dano, o efeito de Ferocious é aplicado por 3 segundos, aumentando seu dano em uma porcentagem equivalente ao seu bônus. O efeito de status não pode durar mais de 10 segundos. Não é ativado se esquivado com Intocável. Obtido em World 10.", "v": "40% (S+)"},
        "Vampiric": {"d": "Todos os ataques têm uma perk % de infligir 3 segundos de Vampirismo (exibido como CURSED). O inimigo perde 5% da sua vida por segundo, enquanto o jogador recupera 6,67% da sua vida máxima por segundo. Obtido em World 10.", "v": "15% (S+)"},
        "Crit Stack": {"d": "Cada acerto aumenta multiplicativamente a chance de acerto crítico em (1/5*perk %), acumulando até um total de perk % após 5 acertos. (ex.: 10 % de perk = aumento de 1, 1x). Cada acúmulo é removido após 3, 5 segundos..", "v": "15 % (S+)"},
        "Attack Up": {"d": "Aumenta o dano de acordo com a porcentagem exibida.", "v": "8% (S+)"},
        "Burn Chance": {"d": "Todos os ataques têm uma chance de perk % de infligir o efeito de status Queimadura por 3 segundos, que causa dano equivalente a 5% da vida por segundo.", "v": "15% (S+)"},
        "Frost Chance": {"d": "Todos os ataques têm uma chance de perk % de infligir o efeito de status Super Frost por 3 segundos, que causa dano equivalente a 3% da vida por segundo e reduz a velocidade dos inimigos em 90%. Obtido em World 3.", "v": "15% (S+)"},
        "Poison Chance": {"d": "Todos os ataques têm uma chance de perk % de infligir o efeito de status Veneno por 3 segundos, que causa dano equivalente a 2% de HP por segundo. Obtido em World 8.", "v": "15% (S+)"},
        "Agility": {"d": "Aumenta a velocidade de movimento em perk %.", "v": "10% (S+)"},
        "Bonus Health Regen": {"d": "Aumenta a regeneração de HP em perk %. Por padrão o valor é 20%.", "v": "5% (S+)"},
        "Elemental Resistance": {"d": "Reduz a duração dos Efeitos de Status Negativos em perk %. (Poison, Frost, Burn, etc...)", "v": "40% (S+)"},
        "Energized": {"d": "Aumenta multiplicativamente a taxa de carregamento da sua habilidade suprema passiva e a quantidade de energia que você ganha ao eliminar mobs. (Exemplo: bônus de 10 %= aumento de 1, 1x) por padrão: 0, 5 % por segundo, 1 % por kill.", "v": "15% (S+)"},
        "Gold Hoarder": {"d": "Aumenta a quantidade de ouro obtida ao derrotar mobs, em eventos mundiais e em caças ao tesouro.", "v": "20% (S+)"},
        "Lucky Looter": {"d": "Aumenta a taxa de obtenção de itens especiais de inimigos. (ex.: perk 10% = aumento de 1,1x)", "v": "10% (S+)"},
        "Resist Burn": {"d": "Aumenta a chance de evitar os efeitos de status Burn e Aether Burn.", "v": "90% (S+)"},
        "Resist Frost": {"d": "Aumenta a chance de evitar os efeitos de status Freeze, Frost e Super Frost.", "v": "90% (S+)"},
        "Resist Knockdown": {"d": "Aumenta a chance de evitar os efeitos de status Knockdown e Slowed.", "v": "90% (S+)"},
        "Resist Poison": {"d": "Aumenta a chance de evitar os efeitos de status Poison e Inked.", "v": "90% (S+)"},
        "Shifted Aggro": {"d": "Aumenta(positivo) ou diminui(negativo) a frequência com que os inimigos atacam você em comparação com outros aliados. Não tem efeito se você estiver jogando solo.", "v": "35% (S+)"}
    },
    "Pet": {
        "Burn Aura": {"d": "Dano de fogo ao redor do pet.", "v": "Lvl 50"},
        "Fire Mastery": {"d": "Fortalece elemento fogo.", "v": "Max"},
        "Shell": {"d": "Barreira que reduz o dano.", "v": "S"},
        "Taunt": {"d": "Atrai atenção dos monstros.", "v": "Max"},
        "Healing Breeze": {"d": "Cura o mestre periodicamente.", "v": "Lvl 30"}
    }
}

BUILDS_DB = {
    "FULL DPS": {
        "stats": {"Dano": 100, "Defesa": 30, "Movimentação": 65, "Dificuldade": 30},
        "classes_recomendadas": ["Swordmaster", "Arcane Mage", "Dualwilder", "Berserker", "Spirit Archer", "Shadowblade"],
        "armor": {"nome": "Zero Armor", "stars": "★★★★★★", "img": "assets/items/zero_armor.png", "tipo": "Armadura", "perks": ["Attack UP", "Critical Eye", "Brawler"]},
        # TAGS E VIDEO SOBRE AS SKILLS DA CLASSE NESSA FUNCAO
        "detalhes_classes": {
            "Swordmaster": {
                "tags": ["Melee", "High Burst", "End Game"],
                "video": "https://www.youtube.com/watch?v=VIDEO_SWORDMASTER",
                "dica": "Use a habilidade 'Dash' para cancelar a animação do terceiro golpe e dobrar seu DPS."
            },
            "Arcane Mage": {
                "tags": ["Ranged", "AoE", "Farming"],
                "video": "https://www.youtube.com/watch?v=VIDEO_MAGE",
                "dica": "Mantenha distância dos inimigos e abuse da passiva de regeneração de mana."
            }
        },
        "weapons": {
            "Swordmaster": [
                {"nome": "Zero Longsword", "stars": "★★★★★★", "tipo": "Espada",
                    "img": "assets/items/zero_longsword.png", "perks": ["Attack Up", "Burn Chance", "Vampiric"]}
            ],
            "Arcane Mage": [
                {"nome": "Zero Staff", "stars": "★★★★★★", "tipo": "Cajado",
                    "img": "assets/items/zero_staff.png", "perks": ["Attack Up", "Burn Chance", "Vampiric"]}
            ],
            "Dualwilder": [
                {"nome": "Zero Longsword (D)", "stars": "★★★★★★", "tipo": "Espada",
                 "img": "assets/items/twin_blade.png", "perks": ["Attack Up", "Burn Chance", "Vampiric"]},
                {"nome": "Zero Longsword (E)", "stars": "★★★★★★", "tipo": "Espada",
                 "img": "assets/items/twin_blade.png", "perks": ["Attack Up", "Critical Chance", "Boss Bane"]}
            ],
            "Berserker": [
                {"nome": "Zero Greataxe", "stars": "★★★★★★", "tipo": "Machado",
                    "img": "assets/items/zero_greataxe.png", "perks": ["Attack Up", "Lifesteal", "Executioner"]},
                {"nome": "Zero Greataxe", "stars": "★★★★★★", "tipo": "Machado",
                 "img": "assets/items/zero_greataxe.png", "perks": ["Attack Up", "Lifesteal", "Executioner"]}
            ],
            "Spirit Archer": [
                {"nome": "Zero Bow", "stars": "★★★★★★", "tipo": "Arco", "img": "assets/items/zero_bow.png",
                    "perks": ["Attack Speed", "Critical Eye", "Boss Damage"]}
            ],
            "Shadowblade": [
                {"nome": "Zero Longsword (R)", "stars": "★★★★★★", "tipo": "Espada",
                 "img": "assets/items/zero_longsword.png", "perks": ["Executioner", "Attack Speed", "Lifesteal"]},
                {"nome": "Zero Longsword (L)", "stars": "★★★★★★", "tipo": "Espada",
                 "img": "assets/items/zero_longsword.png", "perks": ["Critical Eye", "Attack UP", "Lifesteal"]}
            ]
        },
        "pet": {"nome": "Status do Pet", "stars": "★★★★★", "img": "assets/pets/fire_pet.png", "perks": ["Burn Aura", "Fire Mastery", "Attack UP"]}
    },
    "FULL TANK": {
        "stats": {"Dano": 35, "Defesa": 100, "Movimentação": 30, "Dificuldade": 45},
        "classes_recomendadas": ["Defender", "Guardian", "Paladin"],
        "armor": {"nome": "Guardian Plate", "stars": "★★★★★★", "img": "assets/items/guardian_armor.png", "tipo": "Armadura", "perks": ["HP UP", "Rough Skin", "Fortress"]},
        "weapons": {
            "Defender": [
                {"nome": "Bulwark Hammer", "stars": "★★★★★★", "tipo": "Martelo",
                    "img": "assets/items/hammer.png", "perks": ["Stun Hit", "Block Rate", "Lifesteal"]},
                {"nome": "Bulwark Shield", "stars": "★★★★★★", "tipo": "Escudo",
                    "img": "assets/items/shield.png", "perks": ["Defense UP", "Block Rate", "Fortress"]}
            ],
            "Guardian": [
                {"nome": "Iron Aegis Sword", "stars": "★★★★★★", "tipo": "Espada",
                    "img": "assets/items/sword.png", "perks": ["Block Rate", "Stun Hit", "Lifesteal"]},
                {"nome": "Iron Aegis Shield", "stars": "★★★★★★", "tipo": "Escudo",
                    "img": "assets/items/shield.png", "perks": ["HP UP", "Defense UP", "Block Rate"]}
            ],
            "Paladin": [
                {"nome": "Holy Mace", "stars": "★★★★★★", "tipo": "Maça",
                    "img": "assets/items/mace.png", "perks": ["Stun Hit", "Lifesteal", "Block Rate"]},
                {"nome": "Holy Shield", "stars": "★★★★★★", "tipo": "Escudo",
                    "img": "assets/items/shield.png", "perks": ["Holy Aura", "Defense UP", "Block Rate"]}
            ]
        },
        "pet": {"nome": "Turtle", "stars": "★★★★★", "img": "assets/pets/turtle.png", "perks": ["Shell", "Taunt", "HP UP"]}
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
            "equip": "Greataxe", "lvl": 1, "hp_mult": "x1.5", "aggro": "x2.0",
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
        "Dualwilder": {"img": "https://via.placeholder.com/400x600.png?text=Dualwilder", "equip": "2x Longswords", "lvl": 15, "hp_mult": "x1.0", "aggro": "x1.0", "lore": "Especialista em combate com duas lâminas.", "skills": {"E": {"nome": "S1", "cd": "5s", "desc": "D"}, "R": {"nome": "S2", "cd": "5s", "desc": "D"}, "F": {"nome": "S3", "cd": "5s", "desc": "D"}, "X": {"nome": "S4", "cd": "5s", "desc": "D"}, "C": {"nome": "S5", "cd": "5s", "desc": "D"}}},
        "Elementalist": {"img": "https://via.placeholder.com/400x600.png?text=Elementalist", "equip": "Staff", "lvl": 15, "hp_mult": "x0.9", "aggro": "x1.2", "lore": "Controlador dos elementos naturais.", "skills": {"E": {"nome": "S1", "cd": "5s", "desc": "D"}, "R": {"nome": "S2", "cd": "5s", "desc": "D"}, "F": {"nome": "S3", "cd": "5s", "desc": "D"}, "X": {"nome": "S4", "cd": "5s", "desc": "D"}, "C": {"nome": "S5", "cd": "5s", "desc": "D"}}},
        "Guardian": {"img": "https://via.placeholder.com/400x600.png?text=Guardian", "equip": "Shield & Sword", "lvl": 15, "hp_mult": "x1.5", "aggro": "x2.0", "lore": "Protetor avançado de elite.", "skills": {"E": {"nome": "S1", "cd": "5s", "desc": "D"}, "R": {"nome": "S2", "cd": "5s", "desc": "D"}, "F": {"nome": "S3", "cd": "5s", "desc": "D"}, "X": {"nome": "S4", "cd": "5s", "desc": "D"}, "C": {"nome": "S5", "cd": "5s", "desc": "D"}}}
    },
    "Tier 3": {
        "Paladin": {"img": "https://via.placeholder.com/400x600.png?text=Paladin", "equip": "Mace", "lvl": 30, "hp_mult": "1.3", "aggro": "1.5", "lore": "Guerreiro sagrado que cura e protege.", "skills": {"E": {"nome": "E", "cd": "5s", "desc": "D"}, "R": {"nome": "R", "cd": "5s", "desc": "D"}, "F": {"nome": "F", "cd": "5s", "desc": "D"}, "X": {"nome": "X", "cd": "5s", "desc": "D"}, "C": {"nome": "C", "cd": "5s", "desc": "D"}}},
        "Mage of Light": {"img": "https://via.placeholder.com/400x600.png?text=MageOfLight", "equip": "Staff", "lvl": 30, "hp_mult": "1.0", "aggro": "1.0", "lore": "Mago focado em magias radiantes.", "skills": {"E": {"nome": "E", "cd": "5s", "desc": "D"}, "R": {"nome": "R", "cd": "5s", "desc": "D"}, "F": {"nome": "F", "cd": "5s", "desc": "D"}, "X": {"nome": "X", "cd": "5s", "desc": "D"}, "C": {"nome": "C", "cd": "5s", "desc": "D"}}},
        "Berserker": {"img": "https://via.placeholder.com/400x600.png?text=Berserker", "equip": "Greatsword", "lvl": 30, "hp_mult": "1.2", "aggro": "1.2", "lore": "Força bruta e fúria incontrolável.", "skills": {"E": {"nome": "E", "cd": "5s", "desc": "D"}, "R": {"nome": "R", "cd": "5s", "desc": "D"}, "F": {"nome": "F", "cd": "5s", "desc": "D"}, "X": {"nome": "X", "cd": "5s", "desc": "D"}, "C": {"nome": "C", "cd": "5s", "desc": "D"}}}
    },
    "Tier 4": {
        "Demon": {"img": "https://via.placeholder.com/400x600.png?text=Demon", "equip": "Scythe", "lvl": 50, "hp_mult": "1.0", "aggro": "1.0", "lore": "Edite aqui", "skills": {"E": {"nome": "E", "cd": "5s", "desc": "D"}, "R": {"nome": "R", "cd": "5s", "desc": "D"}, "F": {"nome": "F", "cd": "5s", "desc": "D"}, "X": {"nome": "X", "cd": "5s", "desc": "D"}, "C": {"nome": "C", "cd": "5s", "desc": "D"}}},
        "Dragon": {"img": "https://via.placeholder.com/400x600.png?text=Dragon", "equip": "Gauntlets", "lvl": 50, "hp_mult": "1.0", "aggro": "1.0", "lore": "Edite aqui", "skills": {"E": {"nome": "E", "cd": "5s", "desc": "D"}, "R": {"nome": "R", "cd": "5s", "desc": "D"}, "F": {"nome": "F", "cd": "5s", "desc": "D"}, "X": {"nome": "X", "cd": "5s", "desc": "D"}, "C": {"nome": "C", "cd": "5s", "desc": "D"}}},
        "Spirit Archer": {"img": "https://via.placeholder.com/400x600.png?text=SpiritArcher", "equip": "Bow", "lvl": 50, "hp_mult": "1.0", "aggro": "1.0", "lore": "Precisão espiritual à distância.", "skills": {"E": {"nome": "E", "cd": "5s", "desc": "D"}, "R": {"nome": "R", "cd": "5s", "desc": "D"}, "F": {"nome": "F", "cd": "5s", "desc": "D"}, "X": {"nome": "X", "cd": "5s", "desc": "D"}, "C": {"nome": "C", "cd": "5s", "desc": "D"}}}
    },
    "Tier 5": {
        "Warlord": {"img": "https://via.placeholder.com/400x600.png?text=Warlord", "equip": "Sword", "lvl": 75, "hp_mult": "1.0", "aggro": "1.0", "lore": "Edite aqui", "skills": {"E": {"nome": "E", "cd": "5s", "desc": "D"}, "R": {"nome": "R", "cd": "5s", "desc": "D"}, "F": {"nome": "F", "cd": "5s", "desc": "D"}, "X": {"nome": "X", "cd": "5s", "desc": "D"}, "C": {"nome": "C", "cd": "5s", "desc": "D"}}},
        "Summoner": {"img": "https://via.placeholder.com/400x600.png?text=Summoner", "equip": "Staff", "lvl": 75, "hp_mult": "1.0", "aggro": "1.0", "lore": "Edite aqui", "skills": {"E": {"nome": "E", "cd": "5s", "desc": "D"}, "R": {"nome": "R", "cd": "5s", "desc": "D"}, "F": {"nome": "F", "cd": "5s", "desc": "D"}, "X": {"nome": "X", "cd": "5s", "desc": "D"}, "C": {"nome": "C", "cd": "5s", "desc": "D"}}},
        "Shadowblade": {"img": "https://via.placeholder.com/400x600.png?text=Shadowblade", "equip": "2x Longswords", "lvl": 75, "hp_mult": "1.0", "aggro": "1.0", "lore": "Lâmina das sombras letal.", "skills": {"E": {"nome": "E", "cd": "5s", "desc": "D"}, "R": {"nome": "R", "cd": "5s", "desc": "D"}, "F": {"nome": "F", "cd": "5s", "desc": "D"}, "X": {"nome": "X", "cd": "5s", "desc": "D"}, "C": {"nome": "C", "cd": "5s", "desc": "D"}}}
    },
    "Maestria": {
        "Shadowmage": {"img": "https://via.placeholder.com/400x600.png?text=Shadowmage", "equip": "Soul Staff", "lvl": 100, "hp_mult": "1.0", "aggro": "1.0", "lore": "Edite aqui", "skills": {"E": {"nome": "E", "cd": "5s", "desc": "D"}, "R": {"nome": "R", "cd": "5s", "desc": "D"}, "F": {"nome": "F", "cd": "5s", "desc": "D"}, "X": {"nome": "X", "cd": "5s", "desc": "D"}, "C": {"nome": "C", "cd": "5s", "desc": "D"}}},
        "Hunter": {"img": "assets/class/swordmaster.png", "equip": "Crossbow", "lvl": 100, "hp_mult": "1.0", "aggro": "1.0", "lore": "Edite aqui", "skills": {"E": {"nome": "E", "cd": "5s", "desc": "D"}, "R": {"nome": "R", "cd": "5s", "desc": "D"}, "F": {"nome": "F", "cd": "5s", "desc": "D"}, "X": {"nome": "X", "cd": "5s", "desc": "D"}, "C": {"nome": "C", "cd": "5s", "desc": "D"}}},
        "Stormcaller": {"img": "https://via.placeholder.com/400x600.png?text=Stormcaller", "equip": "Orb", "lvl": 100, "hp_mult": "1.0", "aggro": "1.0", "lore": "Edite aqui", "skills": {"E": {"nome": "E", "cd": "5s", "desc": "D"}, "R": {"nome": "R", "cd": "5s", "desc": "D"}, "F": {"nome": "F", "cd": "5s", "desc": "D"}, "X": {"nome": "X", "cd": "5s", "desc": "D"}, "C": {"nome": "C", "cd": "5s", "desc": "D"}}},
        "Leviathan": {"img": "https://via.placeholder.com/400x600.png?text=Leviathan", "equip": "Trident", "lvl": 100, "hp_mult": "1.0", "aggro": "1.0", "lore": "Edite aqui", "skills": {"E": {"nome": "E", "cd": "5s", "desc": "D"}, "R": {"nome": "R", "cd": "5s", "desc": "D"}, "F": {"nome": "F", "cd": "5s", "desc": "D"}, "X": {"nome": "X", "cd": "5s", "desc": "D"}, "C": {"nome": "C", "cd": "5s", "desc": "D"}}},
        "Starbreaker": {"img": "https://via.placeholder.com/400x600.png?text=Starbreaker", "equip": "Hammer", "lvl": 100, "hp_mult": "1.0", "aggro": "1.0", "lore": "Edite aqui", "skills": {"E": {"nome": "E", "cd": "5s", "desc": "D"}, "R": {"nome": "R", "cd": "5s", "desc": "D"}, "F": {"nome": "F", "cd": "5s", "desc": "D"}, "X": {"nome": "X", "cd": "5s", "desc": "D"}, "C": {"nome": "C", "cd": "5s", "desc": "D"}}},
        "Necromancer": {"img": "https://via.placeholder.com/400x600.png?text=Necromancer", "equip": "Grimoire", "lvl": 100, "hp_mult": "1.0", "aggro": "1.0", "lore": "Edite aqui", "skills": {"E": {"nome": "E", "cd": "5s", "desc": "D"}, "R": {"nome": "R", "cd": "5s", "desc": "D"}, "F": {"nome": "F", "cd": "5s", "desc": "D"}, "X": {"nome": "X", "cd": "5s", "desc": "D"}, "C": {"nome": "C", "cd": "5s", "desc": "D"}}}
    }
}
