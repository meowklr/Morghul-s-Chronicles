from random import *

class Hero:
    #attaquer, subir, stocker le max de vie pour regen, vie actuelle
    def __init__(self, name, attack, defense, hp, max_hp):
        self.name = name
        self.attack_power = attack
        self.defense = defense
        self.hp = hp
        self.max_hp = max_hp

    def take_damage(self, damage):
        self.hp -= max(1, damage - self.defense)
    
    def is_alive(self):
        return self.hp > 0
    
    def deal_damage(self, target):
        target.take_damage(self.attack_power)

class Monster:
    #pareil que hero dans l'idee
    def __init__(self, name, attack, defense, hp, max_hp):
        self.name = name
        self.attack_power = attack
        self.defense = defense
        self.hp = hp
        self.max_hp = max_hp

    def take_damage(self, damage):
        self.hp -= max(1, damage - self.defense)
    
    def is_alive(self):
        return self.hp > 0
    
    def deal_damage(self, target):
        target.take_damage(self.attack_power)

class Bonus:
    #trouver des bonus a certians moments, description et effet
    #regen
    #boost attaque
    #boost def
    def __init__(self, name, description, effect):
        self.name = name
        self.description = description
        self.effect = effect

    def increase_attack(self, hero):
        hero.attack_power += 10

    def increase_defense(self, hero):
        hero.defense += 10
    
    def heal(self, hero):
        hero.hp = hero.max_hp

class Chest:
    #loot random (objet bonus) toutes les x vagues
    #stocker tout les loots existants
    #randomiser le loot obtenu
    #appliquer l'effet
    def __init__(self, loot):
        self.loot=loot

    """def random_loot(self):"""

class SpecialEvent:
    def __init__(self, nom, description, effet):
        #evenement random toutes les x vagues
        #idées: lune de sang regen le monstre, secours fait apparaitre gros hero, trahison un hero se corrompt et devient un monstre, benediction qui regen la team
        self.nom = nom
        self.description = description
        self.effet = effet


        