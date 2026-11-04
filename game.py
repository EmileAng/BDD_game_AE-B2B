import db_init
import utils
import displays
import random


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
        displays.display_wave(wave)
        new_wave(team)
    return wave

# nouvelle vague (équipe)
    # tour = 0
    # choisir un monstre 
    # tant que le monstre et l'équipe sont vivants :
        # tour += 1
        # lancer un tour (équipe, monstre)
def new_wave(team):
    turn = 0
    enemies = utils.choose_monster()
    while utils.is_group_alive(enemies) and utils.is_group_alive(team):
        turn += 1
        displays.display_turn(turn)
        new_turn(team, enemies)

# lancer un tour (équipe, monstre)
    # équipe attaque 
    # monstre attaque
def new_turn(team, enemies):
    team_attack(team, enemies)
    enemies_attack(team, enemies)

# monstre attaque 
    # récupérer monstres vivants
    # si il y a des monstres vivants
        # monstres vivants attaque équipe
def enemies_attack(team, enemies):
    alive_enemies = utils.get_alive_characters(enemies)
    if alive_enemies:
        group_attack(enemies, team)

# équipe attaque (équipe, monstre)
    # récupérer équipe vivants
    # l'équipe vivants attaque monstre(équipe vivante, monstre)
def team_attack(team, enemies):
    alive_team = utils.get_alive_characters(team)
    group_attack(alive_team, enemies)

# groupe1 attaque groupe2
    # pour chaque personnage dans groupe1 
        # trouver une cible valide (groupe2)
        # si une cible valide trouvée
            # infliger dégâts
def group_attack(group_1, group_2):
    for character in group_1:
        target = find_valid_target(group_2)
        if target :
            deal_damages(character, group_2, target)

# infliger dégâts(attaquant, groupe2, cible)
    # pv de la groupe2(cible) -= (attaque attaquant - défense groupe2(cible))
def deal_damages(aggressor, group_2, target):
    group_2(target["PV"]) = group_2(target["PV"]) - (aggressor["ATK"] - group_2(target["DEF"]))

# trouver une cible valide (groupe)
    # RECUPERER les personnages vivants dans groupe 
    # si il y a des personnages vivants
        # choisir une cible au hasard
        # retourner la cible
    # retourner None
def find_valid_target(group):
    alive_targets = utils.get_alive_characters(group)
    if alive_targets :
        target = random.choice(alive_targets)
        return target
    return None

