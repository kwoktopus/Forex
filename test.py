# import requests
from API import API


API_KEY = 'e43f5f6a30b84d4968f768899da1a5f52e4bba7f'
USERNAME = 'asjkldfasldkjflksajdf'
PASSWORD = 'ljaksdfsadf1DFDSF'
api = API(API_KEY, USERNAME, PASSWORD)

# HEADER = {
#     'X-IG-API-KEY' : API_KEY,
#     'Content-Type' : 'application/json; charset=UTF-8',
#     'Accept' : 'application/json; charset=UTF-8',
#     'VERSION' : '2',
# }

# JSON = { 
#     "identifier": "asjkldfasldkjflksajdf", 
#     "password": "ljaksdfsadf1DFDSF" 
# } 

# BASE_URL = 'https://demo-api.ig.com/gateway/deal/session'


# response = requests.post(BASE_URL, headers = HEADER, json = JSON)

# if response.status_code == 200: # success
#     CST = response.headers['CST']
#     TOKEN = response.headers['X-SECURITY-TOKEN']

#     HEADER['CST'] = CST
#     HEADER['X-SECURITY-TOKEN'] = TOKEN


# else:
#     print ("failed to connect")


# WATCHLIST_URL = 'https://demo-api.ig.com/gateway/deal/positions'
# watchlist = requests.get(WATCHLIST_URL, headers=HEADER, json=JSON)