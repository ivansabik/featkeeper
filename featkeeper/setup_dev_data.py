# setup_dev_data.py
from schemas import *
from pymongo import MongoClient
import shortuuid

# Product areas: Policies, Billing, Claims, Reports
# Clients: A, B, C
# Agents: Eleuthere, Amanda, Jean Claude

def _insert_feature_requests(client):
    client.drop_database('featkeeper')
    db = client.featkeeper
    collection = db.feature_requests
    FeatureRequest = create_model(feature_request_schema(), collection)
    feature_request = FeatureRequest({
        'title': 'Support custom themes',
        'description': 'Client wants to be able to choose different colors, fonts, and layouts for each module',
        'client_name': 'A',
        'client_priority': 1,
        'target_date': '2016-08-21',
        'product_area': 'Policies',
        'agent_name': 'Eleuthere',
        'ticket_url': 'http://localhost:5000/' + shortuuid.ShortUUID().random(length=6)
    })
    feature_request.save()
    feature_request = FeatureRequest({
        'title': 'CSV export',
        'description': 'Client wants to be able to export their monthly payments to CSV file',
        'client_name': 'A',
        'client_priority': 2,
        'target_date': '2016-06-01',
        'product_area': 'Billing',
        'agent_name': 'Jean Claude',
        'ticket_url': 'http://localhost:5000/' + shortuuid.ShortUUID().random(length=6)
    })
    feature_request.save()
    feature_request = FeatureRequest({
        'title': 'Batch excel import',
        'description': 'Client wants to be able to batch import Claims from an xlsx file',
        'client_name': 'A',
        'client_priority': 3,
        'target_date': '2016-08-25',
        'product_area': 'Claims',
        'agent_name': 'Jean Claude',
        'ticket_url': 'http://localhost:5000/' + shortuuid.ShortUUID().random(length=6)
    })
    feature_request.save()
    feature_request = FeatureRequest({
        'title': 'Add sales channel field',
        'description': 'Client wants to be able to see the sales channel associated',
        'client_name': 'B',
        'client_priority': 1,
        'target_date': '2016-11-21',
        'product_area': 'Policies',
        'agent_name': 'Eleuthere',
        'ticket_url': 'http://localhost:5000/' + shortuuid.ShortUUID().random(length=6)
    })
    feature_request.save()
    feature_request = FeatureRequest({
        'title': 'Implement claim workflow',
        'description': 'Client wants to be able to create new workflows and track them for each claim',
        'client_name': 'B',
        'client_priority': 2,
        'target_date': '2016-03-21',
        'product_area': 'Claims',
        'agent_name': 'Amanda',
        'ticket_url': 'http://localhost:5000/' + shortuuid.ShortUUID().random(length=6)
    })
    feature_request.save()
    feature_request = FeatureRequest({
        'title': 'Sales by product area mobile',
        'description': 'Client wants to be able to see sales by product area using mobile devices',
        'client_name': 'B',
        'client_priority': 3,
        'target_date': '2016-06-12',
        'product_area': 'Reports',
        'agent_name': 'Eleuthere',
        'ticket_url': 'http://localhost:5000/' + shortuuid.ShortUUID().random(length=6)
    })
    feature_request.save()
    feature_request = FeatureRequest({
        'title': 'Send e-mail on new claim',
        'description': 'Client wants to be able to send e-mail to client and agent when new claims get created',
        'client_name': 'C',
        'client_priority': 1,
        'target_date': '2016-12-10',
        'product_area': 'Claims',
        'agent_name': 'Jean Claude',
        'ticket_url': 'http://localhost:5000/' + shortuuid.ShortUUID().random(length=6)
    })
    feature_request.save()
    feature_request = FeatureRequest({
        'title': 'Send telegram message on new policy',
        'description': 'Client wants to be able to send a telegram message to client when new policies gets created',
        'client_name': 'C',
        'client_priority': 2,
        'target_date': '2016-06-25',
        'product_area': 'Policies',
        'agent_name': 'Eleuthere',
        'ticket_url': 'http://localhost:5000/' + shortuuid.ShortUUID().random(length=6)
    })
    feature_request.save()
    feature_request = FeatureRequest({
        'title': 'Add customer satisfaction survey',
        'description': 'Client wants to be able to send out a survey to evaluate customer satisfaction after issuing a new claim',
        'client_name': 'C',
        'client_priority': 3,
        'target_date': '2016-05-16',
        'product_area': 'Claims',
        'agent_name': 'Amanda',
        'ticket_url': 'http://localhost:5000/' + shortuuid.ShortUUID().random(length=6)
    })
    feature_request.save()
    feature_request = FeatureRequest({
        'title': 'Claims by status',
        'description': 'Client wants to be able to see a report showing claims by status where he can filter',
        'client_name': 'C',
        'client_priority': 4,
        'target_date': '2016-07-25',
        'product_area': 'Reports',
        'agent_name': 'Amanda',
        'ticket_url': 'http://localhost:5000/' + shortuuid.ShortUUID().random(length=6)
    })
    feature_request.save()

if __name__ == '__main__':
    client = MongoClient()
    _insert_feature_requests(client)
