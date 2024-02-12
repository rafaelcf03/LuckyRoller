import os
from pymongo import MongoClient
from dotenv import load_dotenv, find_dotenv


def mongo_connection():
    load_dotenv(find_dotenv())

    password = os.environ.get('MONGO_PWD')

    url = f'mongodb+srv://rafaelcf03:{password}@cluster0.mdumcga.mongodb.net/?retryWrites=true&w=majority'

    return MongoClient(url)


client = mongo_connection()

db_dnd = client.production
collection = db_dnd.dnd_weapons


def insert():
    weapons = [{"weapon": "Adaga", "damage_dice": 4},
               {"weapon": "Azagaia", "damage_dice": 6},
               {"weapon": "Bordão", "damage_dice": 6},
               {"weapon": "Clava Grande", "damage_dice": 8},
               {"weapon": "Foice Curta", "damage_dice": 4},
               {"weapon": "Lança", "damage_dice": 6},
               {"weapon": "Maça", "damage_dice": 6},
               {"weapon": "Machadinha", "damage_dice": 6},
               {"weapon": "Martelo Leve", "damage_dice": 4},
               {"weapon": "Porrete", "damage_dice": 4},
               {"weapon": "Arco Curto", "damage_dice": 6},
               {"weapon": "Besta Leve", "damage_dice": 8},
               {"weapon": "Dardo", "damage_dice": 4},
               {"weapon": "Funda", "damage_dice": 4},
               {"weapon": "Alabarda", "damage_dice": 10},
               {"weapon": "Cimitarra", "damage_dice": 6},
               {"weapon": "Chicote", "damage_dice": 4},
               {"weapon": "Espada Curta", "damage_dice": 6},
               {"weapon": "Espada Grande", "damage_dice": 6},
               {"weapon": "Espada Longa", "damage_dice": 8},
               {"weapon": "Glaive", "damage_dice": 10},
               {"weapon": "Lança de Montaria", "damage_dice": 12},
               {"weapon": "Lança Longa", "damage_dice": 10},
               {"weapon": "Maça Estrela", "damage_dice": 8},
               {"weapon": "Machado Grande", "damage_dice": 12},
               {"weapon": "Machado de Batalha", "damage_dice": 8},
               {"weapon": "Malho", "damage_dice": 6},
               {"weapon": "Mangual", "damage_dice": 8},
               {"weapon": "Martelo de Guerra", "damage_dice": 8},
               {"weapon": "Picareta de Guerra", "damage_dice": 8},
               {"weapon": "Rapieira", "damage_dice": 8},
               {"weapon": "Tridente", "damage_dice": 6},
               {"weapon": "Arco Longo", "damage_dice": 8},
               {"weapon": "Besta de Mão", "damage_dice": 6},
               {"weapon": "Besta Pesada", "damage_dice": 10},
               {"weapon": "Zarabatana", "damage_dice": 1}]

    collection.insert_many(weapons)


def all_weapons():
    weapons_db = collection.find({}, {"weapon": 1})
    weapons = [weapon["weapon"] for weapon in weapons_db]

    return weapons


def search_item(value):
    data = collection.find_one({"weapon": value})

    if data is None:
        return "Objeto não encontrado. Cheque a lista de armas disponíveis e tente novamente."
    else:
        return collection.find_one({"weapon": value})


