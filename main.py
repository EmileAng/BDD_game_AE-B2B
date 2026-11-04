from pymongo import MongoClient 
SERVER = MongoClient("localhost:27017")
DB = SERVER("FG")
TEAM_SIZE = 3
NAME_SIZE = 3

# lancer le jeu
    # afficher le menu
    # demander un choix valide
    # lancer l'option correspondante

# lancer l'option correspondante (choix)
    # si le choix == 1 
        # commencer une nouvelle partie
    # si le choix == 2 
        # afficher leaderboard
    # si le choix == 3 
        # quitter

# quitter 
    # message de fin 

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

# afficher le leaderboard
    # récupérer la collection des scores (format liste)
    # trier les scores
    # afficher les 10 premiers scores

# enregistrer le score 
    # demander un nom valide 
    # insérer le score + nom à la collection

# demander un nom valide
    # nom = ""
    # tant que vrai
        # demander input 
        # si la longueur de nom == NAME_SIZE
            # retourner nom
        # message d'erreur

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

# équipe attaque (équipe, monstre)
    # récupérer équipe vivants
    # l'équipe vivants attaque monstre(équipe vivante, monstre)

# monstre attaque 
    # vérifier monstres vivants
    # si il y a des monstres vivants
        # monstres vivants attaque équipe

# groupe1 attaque groupe2
    # pour chaque personnage dans groupe1 
        # trouver une cible valide (groupe2)
        # si une cible valide trouvée
            # infliger dégâts
            
# infliger dégâts(attaquant, groupe2, cible)
    # pv de la groupe2(cible) -= (attaque attaquant - défense groupe2(cible))

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

# afficher une collection 
    # récupérer la collection voulue (format liste)
    # pour chaque entité dans la collection
        # afficher entité

# récupérer la collection 
    # choisir la collection depuis DB
    # retourner la collection
