import yaml
from pymongo import mongo_client


def get_client(config):
    client = mongo_client.MongoClient(config)
    return client


def resolve_config():
    with open("../config.yaml", "r") as cfg:
        return yaml.load(cfg)



def operations(client:mongo_client.MongoClient , operations:str)
    match operations:
        case "insert":
            client.write_concern()
