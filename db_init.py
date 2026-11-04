from pymongo import MongoClient

URL = "mongodb://localhost:27017/"
SERVER = MongoClient(URL)
DB = SERVER["FG"]

# afficher une collection 
    # récupérer la collection voulue (format liste)
    # pour chaque entité dans la collection
        # afficher entité
def display_collection(collection_name):
    collection = list(get_collection_from_db(collection_name))
    for entity in range(len(collection)) :
        print(collection[entity])

# récupérer la collection 
    # choisir la collection depuis DB
    # retourner la collection
def get_collection_from_db(collection_name):
    collection = DB.get_collection(collection_name)
    collection_found = list(collection.find({}))
    return collection_found

def update_db_score(name, score):
    DB.scores.insert_one({"player_name" : name, "score" : score})

