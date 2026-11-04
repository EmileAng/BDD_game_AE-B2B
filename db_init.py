from pymongo import MongoClient

URL = "mongodb://localhost:27017/"
SERVER = MongoClient(URL)
DB = SERVER["FG"]
TEAM_SIZE = 3
NAME_SIZE = 3
# afficher une collection 
    # récupérer la collection voulue (format liste)
    # pour chaque entité dans la collection
        # afficher entité

# récupérer la collection 
    # choisir la collection depuis DB
    # retourner la collection

def display_collection(collection_name):
    collection = list(get_collection_from_db(collection_name))
    for entity in collection :
        print(entity)

def get_collection_from_db(collection_name):
    collection = DB.getCollection(collection_name)
    return collection

display_collection("FG_characters")