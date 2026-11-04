import displays
import utils
import game

TEAM_SIZE = 3
NAME_SIZE = 3

# lancer le jeu
    # afficher le menu
    # demander un choix valide
    # lancer l'option correspondante
def main():
    displays.display_menu()
    choice = utils.ask_valid_choice(1,3)
    start_option(choice)

# lancer l'option correspondante (choix)
    # si le choix == 1 
        # commencer une nouvelle partie
    # si le choix == 2 
        # afficher leaderboard
    # si le choix == 3 
        # quitter
def start_option(choice):
    if choice == 1 :
        start_new_game()
    if choice == 2 :
        utils.display_leaderboard()
    if choice == 3 :
        displays.display_leave()


# commencer une nouvelle partie 
    # créer une équipe
    # lancer boucle principale (équipe)
    # fin du jeu
def start_new_game():
    team = game.create_team()
    score = game.main_loop(team)
    end_game(score)


# fin du jeu 
    # afficher le score
    # enregistrer le score
    # afficher le leaderboard
def end_game(score):
    displays.display_score(score)
    utils.save_score(score)
    utils.display_leaderboard()


