from pymongo import MongoClient

def populate_test_feature_requests(client):
    pass

def populate_test_agents(client):
    pass

def populate_test_clients(client):
    pass

if __name__ == '__main__':
    client = MongoClient()
    populate_test_feature_requests(client)
    populate_test_agents(client)
    populate_test_clients(client)
