from pymongo import MongoClient
from models import Hero, Monster

def insert_heroes():
    heroes_list=get_db()["heroes"]
    heroes_list.insert_many([
        {"name": "Kaelis Forgefer", "attack": 15, "defense": 10, "hp": 100, "max_hp": 100},  # Guerrier
        {"name": "Lysandra l’Archimage", "attack": 20, "defense": 5, "hp": 80, "max_hp": 80},  # Mage
        {"name": "Faelan Flèche-Sylve", "attack": 18, "defense": 7, "hp": 90, "max_hp": 90},  # Archer
        {"name": "Nyssa l’Insaisissable", "attack": 22, "defense": 8, "hp": 85, "max_hp": 85},  # Voleur
        {"name": "Sigrid Lame-d’Acier", "attack": 14, "defense": 12, "hp": 110, "max_hp": 110},  # Paladin
        {"name": "Azrael Ombrefoutre", "attack": 25, "defense": 3, "hp": 70, "max_hp": 70},  # Sorcier
        {"name": "Tharion le Colosse", "attack": 17, "defense": 15, "hp": 120, "max_hp": 120},  # Chevalier
        {"name": "Elowen la Pure", "attack": 19, "defense": 9, "hp": 95, "max_hp": 95},  # Moine
        {"name": "Graven Brisecrâne", "attack": 23, "defense": 6, "hp": 105, "max_hp": 105},  # Berserker
        {"name": "Rowan Feuillombre", "attack": 16, "defense": 11, "hp": 100, "max_hp": 100},  # Chasseur
        {"name": "Morghul l’Apocalypse", "attack": 50, "defense": 50, "hp": 200, "max_hp": 200}  # Druide surpuissant
    ])

def insert_monsters():
    monsters_list=get_db()["monsters"]
    monsters_list.insert_many([
        {"name": "Gobelin", "attack": 10, "defense": 5, "hp": 50, "max_hp": 50},
        {"name": "Orc", "attack": 20, "defense": 8, "hp": 120, "max_hp": 120},
        {"name": "Dragon", "attack": 35, "defense": 20, "hp": 300, "max_hp": 300},
        {"name": "Zombie", "attack": 12, "defense": 6, "hp": 70, "max_hp": 70},
        {"name": "Troll", "attack": 25, "defense": 15, "hp": 200, "max_hp": 200},
        {"name": "Spectre", "attack": 18, "defense": 10, "hp": 100, "max_hp": 100},
        {"name": "Golem", "attack": 30, "defense": 25, "hp": 250, "max_hp": 250},
        {"name": "Vampire", "attack": 22, "defense": 12, "hp": 150, "max_hp": 150},
        {"name": "Loup-garou", "attack": 28, "defense": 18, "hp": 180, "max_hp": 180},
        {"name": "Squelette", "attack": 15, "defense": 7, "hp": 90, "max_hp": 90}
    ])

def insert_bonuses():
    bonuses_list=get_db()["bonuses"]
    bonuses_list.insert_many([
        {"name": "Potion de vie", "description": "Restaure complètement la vie d'un de vos héros aléatoire", "effect": "heal"},
        {"name": "Potion de force", "description": "Augmente l'attaque de 10 points à l'un de vos héros aléatoire", "effect": "increase_attack"},
        {"name": "Potion de défense", "description": "Augmente la défense de 10 points à l'un de vos héros aléatoire", "effect": "increase_defense"}
    ])

def get_db():
    client = MongoClient("mongodb://localhost:27017/MONGO_")
    db = client["game_db"]
    return db

# AJOUTER UN HÉROS
def add_hero(name, hp, attack, defense):
    db = get_db()
    heroes = db["heroes"]
    hero = {"name": name, "hp": hp, "attack": attack, "defense": defense, "max_hp": hp}
    result = heroes.insert_one(hero)
    return result.inserted_id

# AJOUTER PLUSIEURS HÉROS
def add_many_heroes(heroes_list):
    db = get_db()
    heroes = db["heroes"]
    result = heroes.insert_many(heroes_list)
    return result.inserted_ids

# RÉCUPÉRER TOUS LES HÉROS
def get_all_heroes():
    db = get_db()
    heroes_dict = list(db["heroes"].find({}, {"_id": 0}))  # Sans l'id MongoDB
    return [Hero(**hero) for hero in heroes_dict]  # Convertit les dicts en objets Hero


def add_many_monsters(monsters_list):
    db = get_db()
    monsters = db["monsters"]
    result = monsters.insert_many(monsters_list)
    return result.inserted_ids

def get_all_monsters():
    db = get_db()
    monsters_dict = list(db["monsters"].find({}, {"_id": 0}))  # Sans l'id MongoDB
    return [Monster(**monster) for monster in monsters_dict]  # Convertit les dicts en objets Monster


def add_to_leaderboard(name, count, team):
    db = get_db()
    leaderboard = db["leaderboard"]
    entry = {
        "name": name,
        "count": count,
        "team": team,
    }
    result = leaderboard.insert_one(entry)
    return result.inserted_id

#vider et recréer les collections au lancement de db_init()
db = get_db()
db["heroes"].delete_many({})
db["monsters"].delete_many({})
db["bonuses"].delete_many({})
insert_heroes()
insert_monsters()
insert_bonuses()