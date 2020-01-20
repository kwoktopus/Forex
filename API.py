import requests

import paths
from entities import *
from decorators import runtime

class API:
    def __init__(self, key, ID, password):
        self.key = key
        self.ID = ID
        self.password = password

        print (self.authenticate())

    def openPosition(self, market, direction, size, orderType="MARKET"):
        print ("OPENING POSITION")
        pass

    def getOrders(self):
        self.HEADER['VERSION'] = '2'
        return self.get(paths.ORDER).json()['workingOrders']

    def getPositions(self):
        self.HEADER['VERSION'] = '2'
        return [Position(json) for json in self.get(paths.POSITION).json()['positions']]

    def getMarket(self, market):
        self.HEADER['VERSION'] = '2'
        return self.get(paths.MARKET, {'epics' : market}).json()['marketDetails'][0]

    def getPrices(self, market, timeFrame="MINUTE", nPeriods="10"):
        self.HEADER['VERSION'] = '3'
        params = {'resolution':timeFrame, 'max':str(nPeriods), 'pageSize' : str(nPeriods)}
        json = self.get(paths.PRICE + market, params).json()
        return PricesRange(json, timeFrame, market)
    
    # @runtime
    def getCurrentPrice(self, market):
        price = {}
        snapshot = self.getMarket(market)['snapshot']
        price['bid'] = snapshot['bid']
        price['ask'] = snapshot['offer']
        price['lastTraded'] = None
        return Price(price)

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
