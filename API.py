import requests

import paths
from entities import *

class API:
    def __init__(self, key, ID, password):
        self.key = key
        self.ID = ID
        self.password = password

        print (self.authenticate())


    def getOrders(self):
        self.HEADER['VERSION'] = '2'
        return self.get(paths.ORDER).json()['workingOrders']

    def getPositions(self):
        self.HEADER['VERSION'] = '2'
        return [Position(json) for json in self.get(paths.POSITION).json()['positions']]

    def getMarket(self, market):
        self.HEADER['VERSION'] = '2'
        return self.get(paths.MARKET, {'epics' : market}).json()

    def getPrices(self, market, timeFrame="MINUTE", nPeriods="10"):
        self.HEADER['VERSION'] = '3'
        params = {'resolution':timeFrame, 'max':str(nPeriods), 'pageSize' : str(nPeriods)}

        return PricesRange(self.get(paths.PRICE + market, params).json(), timeFrame, market)

    def getWatchlist(self):
        return self.get(paths.WATCHLIST).json()
    
    def get(self, url, params={}):
        return requests.get(url, headers=self.HEADER, json=self.BODY, params=params)

    def post(self, url, params={}):
        return requests.post(url, headers=self.HEADER, json=self.BODY, params=params)
                       
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
