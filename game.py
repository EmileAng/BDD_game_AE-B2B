import db_init
import utils

TEAM_SIZE = 3


# créer une équipe 
    # afficher la collection classes
    # récupérer la collection classes
    # équipe =[]
    # tant que la taille de l'équipe < TEAM_SIZE
        # demander un choix entité valide(liste)
        # ajouter le choix entité valide (-1) à l'équipe
    # retourner équipe
def create_team():
    db_init.display_collection("FG_characters")
    classes = db_init.get_collection_from_db("FG_characters")
    team = []
    while len(team) < TEAM_SIZE :
        choice = utils.ask_valid_entity_choice(classes)
        team.append(classes[choice-1])
    return team

# lancer boucle principale
    # vague = 0
    # tant que équipe en vie
        # vague += 1
        # nouvelle vague (équipe)
def main_loop(team):
    wave = 0
    while utils.is_group_alive(team):
        wave += 1
        new_wave(team)

# nouvelle vague (équipe)
    # tour = 0
    # choisir un monstre 
    # tant que le monstre et l'équipe sont vivants :
        # tour += 1
        # lancer un tour (équipe, monstre)
    # retourner équipe 
def new_wave(team):
    turn = 0
    monster = utils.choose_monster()

