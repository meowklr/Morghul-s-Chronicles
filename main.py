from db_init import *
from utils import *
from models import *
from game import *
import random

#======================================================== Avant-jeu =================================================================#

def main():
    #accueillir le joueur
    #afficher menu avec 3 options
    choice = display_main_menu()
    #recuperer le choix utilisateur
    #si choix = score => montrer les scores (leaderboard)
    if choice == 1 :
        print("Le but du jeu est de venir à bout du nombre maximum de vagues de monstres possible. Le jeu se joue automatiquement.")
        launch_game()
    elif choice == 2 :
        show_leaderboard()
        main()
    else :
        return 
    #si choix = demarrer => lanceer la creation d'equipe team_build(), nick()
    #si choix = quitter => arreter le programme leave()


def display_main_menu():
    #affichage des choix avec habillage et verif de l'entree
    print("\n+--------------------------------------+")
    print("|         BIENVENUE SUR LE JEU        |")
    print("+--------------------------------------+")
    print("| [1]  Demarrer le jeu               |")
    print("| [2]  Voir les scores               |")
    print("| [3]  Quitter                       |")
    print("+--------------------------------------+")

    try:
        choice = int(input("Choix: "))
    except ValueError:
        print("Choix invalide, veuillez entrer 1, 2 ou 3.")
        return display_main_menu()

    if validate_main_menu_choice(choice):
        return choice
    else:
        return display_main_menu()


def launch_game():
    #demander pseudo
    #creer la team
    #compter les vagues
    #leaderboard
    pseudo = nick()
    team = team_build()
    team_names = [hero.name for hero in team]
    wave_count = waves(team)
    add_to_leaderboard(pseudo, wave_count, team_names)
    print("Merci d'avoir joué ! Votre score a été enregistré dans le leaderboard.")
    show_leaderboard()


#======================================================== Introduction du jeu =================================================================#

def team_build():
    #affichage equipe actuelle
    #selection de perso
    team = []
    chosen_indices = []  #indices des héros choisis
    heroes = heroes_selection()  #affiche et retourne les héros
    print("Vous allez devoir constituer une équipe.")
    
    while len(team) < 3:
        select = input(f"Choisis un héros ({len(team)+1}/3) : ")
        valid, result = validate_hero(select, heroes, chosen_indices)
        if valid:
            hero = heroes[result-1]  #récupère l'objet Hero
            team.append(hero) 
            chosen_indices.append(result)  #garde l'indice
            print(f"{hero.name} ajouté à votre équipe.")
            print_team(team)
        else:
            print(f"{result}")
    return team


def print_team(team):
    #affichage de l'équipe actuelle
    if team:
        print("\nVotre équipe actuelle :")
        for i, hero in enumerate(team, 1):
            print(f"{i}. {hero.name} - ATK: {hero.attack_power}, DEF: {hero.defense}, HP: {hero.hp}")
        print()
    else:
        print("Toute votre équipe a été vaincue. Vous avez perdu !")


def heroes_selection():
    #affichage des specs des perso et des persos dispo
    heroes = get_all_heroes()
    for i, hero in enumerate(heroes, 1):
        print(f"{i}. {hero.name} - ATK: {hero.attack_power}, DEF: {hero.defense}, HP: {hero.hp}")
        print()
    return heroes

        
#======================================================== Leaderboard =================================================================#

def show_leaderboard():
    #recup la db des scores
    #trier les scores
    #aficher
    db = get_db()
    leaderboard = db["leaderboard"]
    entries = list(leaderboard.find({}, {"_id": 0}))

    print("\n+--------------------------------------------------------------+")
    print("|                         LEADERBOARD                         |")
    print("+--------------------------------------------------------------+")

    if not entries:
        print("Aucun score enregistré.                           ")
        print("+--------------------------------------------------------------+")
        return

    sorted_entries = sorted(entries, key=lambda entry: entry["count"], reverse=True)
    for i, entry in enumerate(sorted_entries, 1):
        print(
            f"#{i} {entry['name']} | Vagues: {entry['count']} | Equipe: {', '.join(entry['team'])}"
        )

    print("+--------------------------------------------------------------+")


#======================================================== Lancement du jeu =================================================================#

main()