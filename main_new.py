from random import choice, randint
import os

first_name = ("Жран", "Жмых", "Бром", "Дин", "Ван", "Грим")
last_name = ("Дикий", "Ужасный", "Яросный", "Угрюмый", "Вонючий", "Свирепый", "Старый")

def make_hero(
name=None,
hp_curret=None,
hp_max=20,
lvl=0,
xp_next=None,
xp_curret=0,
ATK_base=3,
ATK_weapon=None,
weapon=None,
defense_base=0,
defense_shield=0,
defense_armor=0,
shield=None,
armor=None,
luck=1,
inventory=None,
money=None,
mage=None,
mp_max=None,
mp_curret=None,
stamina_max=None,
stamina_curret=None
 ) -> dict :
    if not name:
        name = choice(first_name) + " " + choice(last_name)
    if not money:
        money = randint(1, (5 + 10 * lvl))
    defense_curret = defense_base + defense_shield + defense_armor
    if not inventory:
        inventory = []
    if not xp_next:
        xp_next = 234 + 234 * (lvl * 2)
    if not hp_max:
        hp_max = 20 + 5 * lvl
    if not hp_curret:
        hp_curret = hp_max
    if not ATK_weapon and not weapon:
        ATK_weapon = 0
    ATK_curret = ATK_base + ATK_weapon
    if not mage:
        mage = choice([True, False])
    if mage == True and not mp_max:
        mp_max = 20 + 5 * lvl
    if not stamina_max:
        stamina_max = 20 + 5 * lvl
    if not mp_curret:
        mp_curret = mp_max
    if not stamina_curret:
        stamina_curret = stamina_max

    return {
        "name": name,
        "hp_max": hp_max,
        "hp_curret": hp_curret,
        "lvl": lvl,
        "xp_next": xp_next,
        "xp_curret": xp_curret,
        "ATK_base": ATK_base,
        "ATK_weapon": ATK_weapon,
        "ATK_curret": ATK_curret,
        "weapon": weapon,
        "defense_base": defense_base,
        "defense_shield": defense_shield,
        "defense_armor": defense_armor,
        "defense_curret": defense_curret,
        "shield": shield,
        "armor": armor,
        "luck": luck,
        "inventory": inventory,
        "money": money,
        "mage": mage,
        "mp_max": mp_max,
        "mp_curret": mp_curret,
        "stamina_max": stamina_max,
        "stamina_curret": stamina_curret
    }

def show_hero(hero):
    for k, v in hero.items():
        print(f"{k}:{v}")


