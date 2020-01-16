import requests

import paths
from entities import Position, Market

class API:
    def __init__(self, key, ID, password):
        self.key = key
        self.ID = ID
        self.password = password

        print (self.authenticate())


    def getOrders(self):
        return self.get(paths.ORDER).json()['workingOrders']

    def getPositions(self):
        # return self.get(paths.POSITION).json()['positions']
        return [Position(json) for json in self.get(paths.POSITION).json()['positions']]

    def getWatchlist(self):
        return self.get(paths.WATCHLIST).json()
    
    def get(self, url):
        return requests.get(url, headers=self.HEADER, json=self.BODY)

    def post(self, url):
        return requests.post(url, headers=self.HEADER, json=self.BODY)
                       
    def authenticate(self):
        self.HEADER = {
            'X-IG-API-KEY' : self.key,
            'Content-Type' : 'application/json; charset=UTF-8',
            'Accept' : 'application/json; charset=UTF-8',
            'VERSION' : '2',
        }

        self.BODY = {
            "identifier": self.ID, 
            "password": self.password 
        }


        response = self.post(paths.ACCOUNT)
        if response.status_code != 200:
            return "FAILED TO AUTHENTICATE"
        self.HEADER['CST'] = response.headers['CST']
        self.HEADER['X-SECURITY-TOKEN'] = response.headers['X-SECURITY-TOKEN']


        return "AUTHENTICATION SUCESSFUL"
