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
    # tant que vrai
        # nouvelle vague (équipe)
        # relancer une vague
        # si non 
            # fin de partie

TODO # afficher scores  

# relancer une vague 
    # vérifier si les persos sont vivants
    # retourner résultat

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


# nouvelle vague (équipe)
    # choisir un monstre 
    # tant que le monstre et l'équipe sont vivants :
        # lancer un tour (équipe, monstre)

# lancer un tour (équipe, monstre)
    # afficher le tour
    # équipe attaque 
    # monstre attaque
    # retourner l'équipe, le monstre, le tour

# équipe attaque (équipe, monstre)
    # vérifier les personnages vivants
    # l'équipe vivante attaque monstre(équipe vivante, monstre)
    # retourner monstre

# monstre attaque 
    # vérifier les monstres vivants
    # monstre attaque équipe
    # retourner équipe

# groupe1 attaque groupe2()
    # pour chaque personnage dans groupe1 
        # trouver une cible valide (groupe2)
        # si une cible valide
            # pv de la groupe2(cible) -= (attaque personnage - défense groupe2(cible))


# trouver une cible valide (groupe)
    # vérifier les personnages vivants
    # choisir une cible au hasard
    # retourner la cible

# vérifier les characters vivants (groupe)
    # équipe vivante = []
    # pour chaque personnage dans le groupe
        # vérifier si le personnage est en vie
        # si oui 
            # l'ajouter à l'équipe vivante
    # retourner l'équipe vivante


# vérifier si character est en vie
    # si la vie est > 0 
        # retourner True
    # retourner False

# choisir un monstre 
    # récupérer la collection des monstres
    # choisir un monstre au hasard dans la liste des monstres
    # retourner le monstre

# les persos sont vivants(liste)
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
    # pour chaque entité dans la collection
        # afficher entité

# récupérer la collection 
    # choisir la collection depuis DB(format liste)
    # retourner la collection


# afficher les scores

# quitter le jeu


