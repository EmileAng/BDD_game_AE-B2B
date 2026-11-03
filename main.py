from pymongo import MongoClient 
SERVER = MongoClient("localhost:27017")
DB = SERVER("FG")
TEAM_SIZE = 3

# lancer le jeu
    # afficher le menu

# afficher le menu 
    # tant qu'une option n'est pas sélectionnée
        # demander un input valide
        # si l'input est valide 
            # lancer l'option correspondante

# commencer une nouvelle partie 
    # afficher la collection classes
    # choisir son équipe
    # tant qu'il reste un personnage de l'équipe vivant
        # nouvelle vague
    # fin de partie

# nouvelle vague (équipe)
    # choisir un monstre 
    # tant que le monstre et l'équipe sont vivants :
        # lancer un tour

# lancer un tour (équipe, monstre)
    # afficher le tour
    # vérifier les personnages vivants
    # l'équipe vivante attaque monstre
    # vérifier les monstres vivants
    # si le monstre est en vie 
        # le monstre attaque équipe vivante
    # retourner l'équipe, le monstre, le tour

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

# choisir son équipe 
    # l'équipe n'est pas complète
    # tant que l'équipe n'est pas complète 
        # demander de choisir un personnage valide 
        # si il y a TEAM_SIZE personnages dans l'équipe
            # l'équipe est complète
    # retourner l'équipe 

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


