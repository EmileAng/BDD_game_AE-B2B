from pymongo import MongoClient 
SERVER = MongoClient("localhost:27017")
DB = SERVER("FG")
TEAM_SIZE = 3

# lancer le jeu
    # afficher le menu
    # demander un choix valide
    # lancer l'option correspondante

# lancer l'option correspondante (choix)
    # si le choix == 1 
        # commencer une nouvelle partie
    # si le choix == 2 
        # afficher les scores
    # si le choix == 3 
        # quitter

# demander un choix valide (min=1, max)
    # tant que vrai
        # demander input
        # si le choix est un nombre 
            # si le choix < min et > max
                # retourner choix
        # message d'erreur 

# commencer une nouvelle partie 
    # vague = 0
    # créer une équipe
    # lancer boucle principale (équipe)
    # fin du jeu
    
# lancer boucle principale
    # vague = 0
    # tant que équipe en vie
        # vague += 1
        # nouvelle vague (équipe)

# fin du jeu 
    # afficher le score
    # enregistrer le score
    # afficher le leaderboard

# enregistrer le score 
    # demander un nom valide 
    # ajouter le score avec le nom à la DB

# créer une équipe 
    # afficher la collection classes
    # équipe =[]
    # tant que la taille de l'équipe < TEAM_SIZE
        # demander un choix entité valide(liste)
        # ajouter le choix entité valide (-1) à l'équipe
    # retourner équipe

# choisir entité (liste)
    # trouver la taille min max de la liste
    # demander choix valide (min, max)

# trouver la taille min max d'une liste (liste)
    # taille max = longueur - 1
    # taille min = 1
    # retourner min et max

# nouvelle vague (équipe)
    # tour = 0
    # choisir un monstre 
    # tant que le monstre et l'équipe sont vivants :
        # tour += 1
        # lancer un tour (équipe, monstre)
    # retourner équipe 

# groupe est vivant
    # récupérer les personnages vivants
    # si groupe vide 
        # retourner False
    # retourner True

# lancer un tour (équipe, monstre)

    # afficher le tour
    # équipe attaque 
    # monstre attaque
    # retourner équipe, monstre

# équipe attaque (équipe, monstre)
    # récupérer équipe vivants
    # l'équipe vivants attaque monstre(équipe vivante, monstre)
    # retourner monstre

# monstre attaque 
    # vérifier monstres vivants
    # si il y a des monstres vivants
        # monstres vivants attaque équipe
    # retourner équipe

# groupe1 attaque groupe2
    # pour chaque personnage dans groupe1 
        # trouver une cible valide (groupe2)
        # si une cible valide trouvée
            # pv de la groupe2(cible) -= (attaque personnage - défense groupe2(cible)) ### FAIRE UNE FONCTION CALCULER DEGATS
    # retourner groupe2


# trouver une cible valide (groupe)
    # RECUPERER les personnages vivants dans groupe 
    # si il y a des personnages vivants
        # choisir une cible au hasard
        # retourner la cible
    # retourner None


# RECUPERER les characters vivants (groupe)
    # équipe vivante = []
    # pour chaque personnage dans le groupe
        # si le personnage est en vie
            # l'ajouter à l'équipe vivante
    # retourner l'équipe vivante

# vérifier si character est en vie
    # si la vie est > 0 
        # retourner True
    # retourner False

# choisir un monstre 
    # récupérer la collection des monstres (format liste)
    # choisir un monstre au hasard dans la liste des monstres
    # retourner le monstre

# mon personnage est valide(équipe)
    # vérifier si le personnage existe 
    # si oui et n'est pas dans l'équipe 
        # ajouter personnage à l'équipe
    # si non
        # message d'erreur
    # retourner l'équipe

# afficher une collection 
    # récupérer la collection voulue (format liste)
    # pour chaque entité dans la collection
        # afficher entité

# récupérer la collection 
    # choisir la collection depuis DB
    # retourner la collection


# afficher les scores

# quitter le jeu








