import displays
import db_init
import random


NAME_SIZE = 3


# demander un choix valide (min=1, max)
    # tant que vrai
        # demander input
        # si le choix est un nombre 
            # si le choix < min et > max
                # retourner choix
        # message d'erreur 
def ask_valid_choice(minimum=1, maximum=None):
    while True:
        entry = input("Choisissez une option")
        if entry.isdigit() and entry < minimum and entry > maximum:
                return entry
        displays.error_message()      

# choisir entité (liste)
    # trouver la taille min max de la liste
    # demander choix valide (min, max)
    # retourner choix
def ask_valid_entity_choice(list):
     min_lenght, max_lenght = find_list_extrems(list)
     choice = ask_valid_choice(min_lenght, max_lenght)
     return choice

# trouver la taille min max d'une liste (liste)
    # taille max = longueur - 1
    # taille min = 1
    # retourner min et max
def find_list_extrems(list):
     max_lenght = len(list)-1
     min_lenght = 1
     return min_lenght, max_lenght

# groupe est vivant
    # récupérer les personnages vivants
    # si groupe vide 
        # retourner False
    # retourner True
def is_group_alive(group):
    alive_group = get_alive_characters(group)
    if not alive_group :
        return False
    return True

# RECUPERER les characters vivants (groupe)
    # équipe vivante = []
    # pour chaque personnage dans le groupe
        # si le personnage est en vie
            # l'ajouter à l'équipe vivante
    # retourner l'équipe vivante
def get_alive_characters(group):
    alive_group = []
    for character in group:
        if is_alive(character):
            alive_group.append(character)
    return alive_group        

# vérifier si character est en vie
    # si la vie est > 0 
        # retourner True
    # retourner False
def is_alive(character):
     if character["PV"] > 0 :
        return True
     return False

# choisir un monstre 
    # récupérer la collection des monstres (format liste)
    # choisir un monstre au hasard dans la liste des monstres
    # retourner le monstre
def choose_monster():
    ennemies = db_init.get_collection_from_db("FG_enemies")
    enemy = random.choice(ennemies)
    return enemy

# enregistrer le score 
    # demander un nom valide 
    # insérer le score + nom à la collection
def save_score(score):
    player_name = ask_valid_name()
    db_init.update_db_score(player_name, score)

# demander un nom valide
    # nom = ""
    # tant que vrai
        # demander input 
        # si la longueur de nom == NAME_SIZE
            # retourner nom
        # message d'erreur
def ask_valid_name():
    while True:
        name = input(f"Entrez un nom à {NAME_SIZE} caractères")
        if len(name) == NAME_SIZE:
            return name
        print("Nom invalide !")

# afficher le leaderboard
    # récupérer la collection des scores (format liste)
    # trier les scores
    # afficher les 10 premiers scores
def display_leaderboard():
    scores = list(db_init.get_collection_from_db("scores"))
    sorted_scores = sorted(scores, key=lambda entity: entity["score"], reverse=True)
    for score in range(10) :
        print(sorted_scores[score])
