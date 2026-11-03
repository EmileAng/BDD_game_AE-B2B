from pymongo import MongoClient 
SERVER = MongoClient("localhost:27017")
DB = SERVER("FG")
TEAM_SIZE = 3
 vérifier relancer nouvelle vague

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
    # vague = 0
    # créer une équipe
    # lancer boucle principale (équipe)
    # fin du jeu
    
# lancer boucle principale
    # tant que vrai
            # vague += 1
            # nouvelle vague (équipe)
            # relancer une vague
            # si non 
                # return

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
    # tour = 0
    # choisir un monstre 
    # tant que le monstre et l'équipe sont vivants :
        # tour += 1
        # lancer un tour (équipe, monstre)
    # retourner équipe 

# groupe est vivant
    # vérifier les personnages vivants
    # si groupe vide 
        # retourner False
    # retourner True

# lancer un tour (équipe, monstre)
    # afficher le tour
    # équipe attaque 
    # monstre attaque
    # retourner équipe, monstre

# équipe attaque (équipe, monstre)
    # vérifier équipe vivants
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
    # vérifier les personnages vivants dans groupe 
    # si il y a des personnages vivants
        # choisir une cible au hasard
        # retourner la cible
    # retourner None



# vérifier les characters vivants (groupe)
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
    # récupérer la collection des monstres
    # choisir un monstre au hasard dans la liste des monstres
    # retourner le monstre

'''# les persos sont vivants(liste)
    # pour chaque personnage dans l'équipe
        # si la vie du personnage est supérieure à 0 
            # retourner True
    # retourner False'''

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


