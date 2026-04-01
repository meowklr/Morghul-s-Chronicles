from db_init import *
from models import *
import random
import time
from utils import validate_quit_choice

#======================================================== Déroulement du jeu =================================================================#

def waves(team):
    #selection du mosntre
    #boucle de combat
    #victoire ou defaite calculé avec win()
    #renvoie le compteur de vagues pour leaderboard
    #compteur -> toutes les deuix vagues, le joueur peut obtenir un bonus parmis différentes raretés, toutes les dix vagues, il a le choix de quitter et d'enregistrer son score
    wave_count = 0
    while team:
        choosen_monster = monster_selection()
        round(team, choosen_monster)
        if win(team, choosen_monster):
            wave_count += 1
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print()
            print(f"Félicitations ! Vous avez survécu à la vague {wave_count}.")
            print()
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            bonuses_verifier(wave_count)
            events_verifier(wave_count)
            if not ask_to_quit(wave_count):
                break
        else:
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print()
            print(f"Vous avez survécu à {wave_count} vague(s).")
            print()
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            break
    return wave_count

def bonuses_verifier(waves):
    #toutes les deux vagues obtenir un loot
    if waves % 2 == 0:
        print()
        print("\n--- BONUS ---")
        print("Vous avez trouvé un coffre !")
        print("-------------")
        print()
    

def events_verifier(waves):
    #toutes les dix vagues il se passe un truc
    if waves % 10 == 0:
        print("\n=== EVENEMENT ===")
        print("Un evenement est sur le point de se produire, préparez-vous...")
        print("=================")

def ask_to_quit(waves):
    #verifier si la vauge est un miultiple de dix
    #si oui on propose de continuer ou de leave
    #si leave return false pour waves()
    #sinon juste ça continue
    if waves % 10 == 0:
        while True:
            print("\n############################")
            print(f"VAGUE {waves}")
            print("1 : Continuer")
            print("2 : Quitter et enregistrer")
            print("############################")
            choice = int(input("Choix: "))
            if validate_quit_choice(choice):
                if choice == 1:
                    print("Vous choisissez de continuer.")
                    return True
                elif choice == 2:
                    print("Vous choisissez de quitter.")
                    return False
    #continue automatiquement si pas multiple de 10
    return True

def monster_selection():
    #random pour selectionner le monstre de la v ague
    monsters = get_all_monsters()
    choosen_monster = random.choice(monsters)
    print(f"Le monstre de cette vague est un {choosen_monster.name} - ATK: {choosen_monster.attack_power}, DEF: {choosen_monster.defense}, HP: {choosen_monster.hp}")
    return choosen_monster


def round(team, monster):
    #tant que l'equipe est en vie ou que le monstre est en vie le round continue
    #textes et sleep pour habillage et fluidité
    while team and monster.hp > 0 :
        print("=========================================")
        print()
        print("Ton équipe attaque...")
        print()
        print("=========================================")
        time.sleep(0.3)
        team_turn(team, monster)
        if monster.is_alive():
            print("=========================================")
            print()
            print("Le monstre attaque...")
            print()
            print("=========================================")
            time.sleep(0.3)
            if monster_turn(team, monster):
                kill_hero(team)


def team_turn(team, monster):
    #si en vie attaquer le mosntre
    #si monstre mort alors true
    for hero in team:
        if hero.is_alive():
            hero.deal_damage(monster)
            print(f"{hero.name} a infligé {max(1, hero.attack_power - monster.defense)} dégâts à {monster.name}. Il lui reste {max(0, monster.hp)} PVs. ")
            time.sleep(0.3)
            if not monster.is_alive():
                print(f"{monster.name} a été vaincu !")
                print()
                return True
    return False


def monster_turn(team, monster):
    #attaquer si en vie
    #verifier si mort
    if not monster.is_alive():
        return False
    target = random.choice(team)
    monster.deal_damage(target)
    print(f"{monster.name} a infligé {max(1, monster.attack_power - target.defense)} dégâts à {target.name}. Il lui reste {max(0, target.hp)} PVs.")
    time.sleep(0.3)
    if not target.is_alive():
        print(f"{target.name} a été vaincu par le {monster.name} !")
        print("=========================================")
        return True
    return False


def kill_hero(team):
    #tuer les héros morts et les retirer de l'équipe
    for hero in team[:]: #itérer sur copie de la team de base
        if not hero.is_alive():
            team.remove(hero)
    return team


def win(team, monster):
    #verifier si toute la team est morte ou si le monstre est mort
    if not team:
        print("Votre équipe a été entièrement vaincue. Vous avez perdu !")
        return False
    elif not monster.is_alive():
        return True
