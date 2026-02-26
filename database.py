# database.py

PERKS_DB = {
    "Armor": {
        "Fortress": {"d": "Aumenta HP máximo em perk%, mas diminui toda a cura recebida em perk%.", "v": "40% (S+)"},
        "Glass": {"d": "Reduz HP máximo7 em 35%, mas aumenta o mínimo e máximo do dano crítico. Ex: Glass 90% como exemplo: O multiplicador de dano crítico base é de 150% a 200%. Acima de Vidro 91%, esse multiplicador passa a ser de 240% a 290%.", "v": "100% (S+)"},
        "Master Thief": {"d": "Derrotar inimigos concede 5 segundos de Movespeed, que aumenta em perk % por até 10 segundos.", "v": "35% (S+)"},
        "Self Destruct": {"d": "Ao sofrer dano letal, você não morre e fica com 1 de HP. Receberá 0,5 segundos de invencibilidade. Quando isso acontecer, uma explosão com raio de 15 studs causará dano equivalente a 100% + porcentagem da sua vida. Possui um tempo de recarga invisível de 120 segundos. Essa passiva não causa acerto crítico. Ter 50% de Self Destruct fará a explosão causar dano equivalente a 150% do seu HP máximo. Obtido em World 10.", "v": "50% (S+)"},
        "Damage Reduction": {"d": "Reduz o dano recebido  em perk %. Isso não afeta o dano de efeitos de status, apenas o dano de ataques.", "v": "8% (S+)"},
        "HP UP": {"d": "Aumenta HP máximo em perk %.", "v": "12% (S)"},
        "Poisonous Thorns": {"d": "Sempre que sofrer dano, o mob tem 50% de chance de receber o status negativo Posion. Sofrendo dano equivalente a 2% do HP máximo por segundo. Não é ativado ao sofrer algum dadno de efeito de status.", "v": "60% (S+)"},
        "Rough Skin": {"d": "Ao receber dano, você tem uma chance de 50% de anular o dano e refletir de volta ao mob. Será exibido a mensagem REFLECT quando ativado.", "v": "9% (S+)"},
        "Untouchable": {"d": "Ao receber dano, você tem uma chance de 50% de anular o dano. Será exibido a mensagem DODGED quando ativado.", "v": "20% (S+)"},
        "Agility": {"d": "Aumenta a velocidade de movimento em perk %.", "v": "10% (S+)"},
        "Bonus Health Regen": {"d": "Aumenta a regeneração de HP em perk %. Por padrão o valor é 20%.", "v": "5% (S+)"},
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
    "Weapon": {
        "Boss Bane": {"d": "Causa mais dano (perk%) a chefes, mas recebe mais dano (perk%) deles. Esse perk afeta qualquer inimigo com barras de vida grandes.", "v": "30 % (S+)"},
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
        "Agility": {"d": "Aumenta a velocidade de movimento em perk %.", "v": "10% (S+)"},
        "Gold Hoarder": {"d": "Aumenta a quantidade de ouro obtida ao derrotar mobs, em eventos mundiais e em caças ao tesouro.", "v": "10% (S+)"},
        "Mob Slayer": {"d": "Causa perk % a mais de dano a monstros normais, mas recebe perk % a mais de dano de monstros normais.", "v": "10% (S+)"},
        "Boss Bane": {"d": "Causa mais dano (perk%) a chefes, mas recebe mais dano (perk%) deles. Esse perk afeta qualquer inimigo com barras de vida grandes.", "v": "10 % (S+)"},
        "Lucky Looter": {"d": "Aumenta a taxa de obtenção de itens especiais de inimigos. (ex.: perk 10% = aumento de 1,1x)", "v": "10% (S+)"},
        "Attack Up": {"d": "Aumenta o dano de acordo com a porcentagem exibida.", "v": "5% (S+)"},
        "Energized": {"d": "Aumenta multiplicativamente a taxa de carregamento da sua habilidade suprema passiva e a quantidade de energia que você ganha ao eliminar mobs. (Exemplo: bônus de 10 %= aumento de 1, 1x) por padrão: 0, 5 % por segundo, 1 % por kill.", "v": "15% (S+)"},
        "Ferocious": {"d": "Ao sofrer dano, o efeito de Ferocious é aplicado por 3 segundos, aumentando seu dano em uma porcentagem equivalente ao seu bônus. O efeito de status não pode durar mais de 10 segundos. Não é ativado se esquivado com Intocável. Obtido em World 10.", "v": "15% (S+)"},
        "Vampiric": {"d": "Todos os ataques têm uma perk % de infligir 3 segundos de Vampirismo (exibido como CURSED). O inimigo perde 5% da sua vida por segundo, enquanto o jogador recupera 6,67% da sua vida máxima por segundo. Obtido em World 10.", "v": "5% (S+)"},
    }
}

BUILDS_DB = {
    "FULL DPS": {
        "stats": {"Dano": 100, "Defesa": 30, "Movimentação": 50, "Dificuldade": 70},
        "classes_recomendadas": ["Dualwilder", "Elementalist", "Berserker", "Spirit Archer", "Shadowblade"],
        "armor": {"nome": "Zero Armor", "stars": "★★★★★★", "img": "assets/items/zero_armor.png", "tipo": "Armadura", "perks": ["Damage Reduction", "Untouchable", "Glass"]},
        # TAGS E VIDEO SOBRE AS SKILLS DA CLASSE NESSA FUNCAO
        "detalhes_classes": {
            "Dualwilder": {
                "tags": ["Glass Cannon", "DPS", "End Game"],
                "dica": """Esta build é focada em <b style='color: #ffd700;'>Dano Explosivo e Velocidade</b>, aproveitando a mecânica nativa de <span style='color: #ffd700;'>Crit Stack</span> da classe.<br><br>
                <b style='color: #ffd700;'>Lembre-se:</b> No Pet você sempre terá 2 escolhas, <b>Agility e Energized</b>. Use Agility se quiser aumentar sua velocidade de movimento ou Energized se quiser ter sua Ultimate pronta com mais rapidez.<br><br>
                O conceito é <i style='color: #ff4b4b;'>Glass Cannon</i>: você derrete chefes e hordas, mas sua defesa é mínima. Use <b>Damage Reduction</b> para diminuir ainda mais o dano recebido ou, <b>Energized</b> para resetar sua Ultimate e abuse do <b>Untouchable</b> para esquivar de golpes fatais.<br><br>
                <b style='color: #ffd700;'>Dica de End Game:</b> Tenha sempre dois Pets preparados — um focado em <b>Boss Bane</b> para finalizar chefes e outro com <b>Vampiric</b> para sustentar o HP enquanto limpa hordas.""",
                
                "analise_tecnica": """
                <b style='color: #00ffcc;'>🛡️ ARMADURA:</b> Foco em gerenciamento de recarga da Ultimate e evasão (100% Glass).<br>
                <b style='color: #ff4b4b;'>🗡️ ARMA (BOSS):</b> Otimizada para alvos únicos com 30% Boss Bane e Attack UP.<br>
                <b style='color: #4b99ff;'>🗡️ ARMA (MOBS):</b> Controle de grupo com 15% Burn Chance e 15% Vampiric para recuperar HP.<br>
                <b style='color: #ffd700;'>🐾 PETS:</b> Alterne entre Agility (Boss) para mobilidade e Energized (Mobs) para recarga de Ultimate.
                """,
                
                "video": "https://www.youtube.com/watch?v=SEU_VIDEO",
                "creditos": "Guia montado por: <b>SeuNome</b>",
                "parceria": "Apoio: <b>CanalParceiro</b>"
            },
            "Elementalist": {
                "tags": ["Dano Corpo a Corpo", "Alvo Único", "Alta Taxa Crítica", "Jogabilidade Moderada", "Ultimate Fortíssima", "Glass Canon"],
                "video": "https://www.youtube.com/watch?v=VIDEO_SWORDMASTER",
                "dica": "Use a habilidade 'Dash' para cancelar a animação do terceiro golpe e dobrar seu DPS."
            },
            "Berserker": {
                "tags": ["Ranged", "AoE", "Farming"],
                "video": "https://www.youtube.com/watch?v=VIDEO_MAGE",
                "dica": "Mantenha distância dos inimigos e abuse da passiva de regeneração de mana."
            }
        },
        # ARMAS DE TODAS AS CLASSES DA BUILD
        "weapons": {
            "Dualwilder": [
                {"nome": "Zero Longsword (Boss)", "stars": "★★★★★★", "tipo": "Espada",
                    "img": "assets/items/zero_longsword.png", "perks": ["Attack Up", "Crit Stack", "Boss Bane"]},
                {"nome": "Zero Longsword (Mob)", "stars": "★★★★★★", "tipo": "Espada",
                    "img": "assets/items/zero_longsword.png", "perks": ["Attack Up", "Burn Chance", "Vampiric"]}
            ],
            "Elementalist": [
                {"nome": "Zero Staff", "stars": "★★★★★★", "tipo": "Cajado",
                    "img": "assets/items/zero_staff.png", "perks": ["Attack Up", "Crit Stack", "Boss Bane"]}
            ],
            "Berserker": [
                {"nome": "Zero Greataxe", "stars": "★★★★★★", "tipo": "Machado",
                    "img": "assets/items/zero_greataxe.png", "perks": ["Attack Up", "Burn Chance", "Vampiric"]},
                {"nome": "Zero Greataxe", "stars": "★★★★★★", "tipo": "Machado",
                    "img": "assets/items/zero_greataxe.png", "perks": ["Attack Up", "Crit Stack", "Boss Bane"]}
            ],
            "Spirit Archer": [
                {"nome": "Zero Bow", "stars": "★★★★★★", "tipo": "Arco", "img": "assets/items/zero_bow.png",
                    "perks": ["Attack Up", "Burn Chance", "Vampiric"]}
            ],
            "Shadowblade": [
                {"nome": "Zero Longsword", "stars": "★★★★★★", "tipo": "Espada",
                    "img": "assets/items/zero_longsword.png", "perks": ["Attack Up", "Burn Chance", "Vampiric"]},
                {"nome": "Zero Longsword", "stars": "★★★★★★", "tipo": "Espada",
                    "img": "assets/items/zero_longsword.png", "perks": ["Attack Up", "Crit Stack", "Boss Bane"]}
            ]
        },
        "pet": {"nome": "Status do Pet", "stars": "★★★★★", "img": "assets/pets/fire_pet.png", "perks": ["Attack Up", "Energized", "Vampiric"]}
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
