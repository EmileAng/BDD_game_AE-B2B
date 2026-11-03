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

# demander un choix valide (min, max)
    # tant que vrai
        # demander input
        # si le choix est un nombre 
            # si le choix < min et > max
                # retourner choix
        # message d'erreur 


# commencer une nouvelle partie 
    # créer une équipe
    # toute mon équipe est vivante
    # tant qu'il reste un personnage de l'équipe vivant
        # nouvelle vague
        # vérifier les personnages vivants
    # fin de partie

# créer une équipe 
    # afficher la collection classes
    # tant que la taille de l'équipe < TEAM_SIZE
        # demander un choix entité valide(liste)
        # ajouter le choix entité valide 
    # retourner équipe

# choisir entité (liste)
    # trouver la taille min max de la liste
    # demander choix valide (min, max)


# nouvelle vague (équipe, équipe vivante)
    # choisir un monstre 
    # tant que le monstre et l'équipe sont vivants :
        # lancer un tour

# lancer un tour (équipe, équipe vivante, monstre)
    # afficher le tour
    # équipe attaque 
    # monstre attaque
    # vérifier les monstres vivants
    # si le monstre est en vie 
        # le monstre attaque équipe vivante
    # retourner l'équipe, le monstre, le tour

# équipe attaque (équipe, équipe vivante, monstre)
    # vérifier les personnages vivants
    # l'équipe vivante attaque monstre

# monstre attaque 
    # vérifier les monstres vivants
    # monstre attaque équipe

# attaquant attaque cible
    # pour chaque personnage dans attaquant 
        # trouver une cible valide
        # pv de la cible -= (attaque attaquant - défense cible)

# vérifier les characters vivants (groupe)
    # équipe vivante = []
    # pour chaque personnage dans le groupe
        # vérifier si le personnage est en vie
        # si oui l'ajouter à l'équipe vivante
    # retourner l'équipe vivante





'''# l'équipe attaque(équipe, monstre)
    # pour chaque personnage dans l'équipe
        # si le personnage et le monstre sont en vie
            # le personnage attaque le monstre
    # retourner l'équipe et le monstre'''

# personnage attaque monstre (personnage, monstre)
    # vie du monstre -= (attaque personnage - défense monstre)
    # retourner monstre

# vérifier si character est en vie
    # si la vie est > 0 
        # retourner True
    # retourner False

# choisir un monstre 
    # récupérer la collection des monstres
    # choisir un monstre au hasard dans la liste des monstres
    # retourner le monstre

# les persos sont vivants(équipe)
    # pour chaque personnage dans l'équipe
        # si la vie du personnage est supérieure à 0 
            # retourner True
    # retourner False

# mon personnage est valide(équipe)
    # vérifier si le personnage existe 
    # si oui et n'est pas dans l'équipe 
        # ajouter personnage à l'équipe
    # si non
        # message d'erreur
    # retourner l'équipe


# afficher une collection 
    # récupérer la collection voulue
    # pour chaque character dans la collection
        # afficher character

# récupérer la collection 
    # choisir la collection (format liste)
    # retourner la collection


# afficher les scores

# quitter le jeu


