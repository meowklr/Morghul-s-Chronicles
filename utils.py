def nick():
    #choix du pseudo
    #demander le pseudo
    #verifier si valide selon x criteres
    #sinon redemander
    pseudo = input("Quel est votre pseudo ?")
    if pseudo.strip() and pseudo.isalnum() and len(pseudo)<=15 :
        print(f"Votre pseudo est {pseudo} .")
    else :
        print("Pseudo invalide (vide/plus de 15 caractères), veuillez réessayer.")
        nick()
    return pseudo

def validate_main_menu_choice(choice):
    #verifier l'entree du choix du debut
    #si entre 1,2,3 lancer sinon redemander
    if choice in [1, 2, 3]:
        return True
    else:
        print("Choix invalide, veuillez entrer 1, 2 ou 3.")
        return False


def validate_hero(selected, heroes, chosen_indices):
    #verifier le choix du hero
    #demander
    try:
        choice = int(selected)
        if 1 <= choice <= len(heroes) and choice not in chosen_indices:
            return True, choice
        elif choice in chosen_indices:
            return False, "Héros déjà sélectionné, choisissez-en un autre."
        else:
            return False, f"Entrez un nombre entre 1 et {len(heroes)}."
    except ValueError:
        return False, "Veuillez entrer un nombre valide."
    
def validate_quit_choice(choice):
    if choice in [1,2]:
        return True
    else:
        print("Choix invlaide, veuillez entrer 1 ou 2.")


