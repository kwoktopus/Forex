from entities import *
from decorators import runtime

from datetime import datetime

class Strategy1: # scalping strategy
    def __init__(self, api, markets, lowerSMA, upperSMA, lowerTimeframe, upperTimeframe, nLookbackPeriods):
        self.api = api
        self.markets = markets
        self.lowerSMA = lowerSMA
        self.upperSMA = upperSMA
        self.lowerTimeframe = lowerTimeframe
        self.upperTimeframe = upperTimeframe
        self.nLookbackPeriods = nLookbackPeriods

        self.positions = {}

        for market in markets:
            self.positions[market] = None

        
    
    def execute(self):
        print("====================")
        for market in self.markets:
            print(market)
            # if self.positions[market]: # we already have an open order for the market
            #     self.closePosition(market) # check if it is suitable to close
            # else: # we do not have an open position for market
            self.openPosition(market) # check if it is suitable to open
        print("====================")

    def closePosition(self, market): # 
        # check parameters and close if needed
        if (False):
            self.positions[market] = None
        
        pass
    
    # @runtime
    def openPosition(self, market):

        lowerMovingAverageLong = self.getMovingAverages(market, self.lowerSMA, self.upperTimeframe, 2)
        upperMovingAverageLong = self.getMovingAverages(market, self.upperSMA, self.upperTimeframe, 2)
        priceRangeLong = self.api.getPrices(market, self.upperTimeframe, 2)
 
        lowerMovingAverageShort = self.getMovingAverages(market, self.lowerSMA, self.lowerTimeframe, self.nLookbackPeriods)
        upperMovingAverageShort = self.getMovingAverages(market, self.upperSMA, self.lowerTimeframe, self.nLookbackPeriods)
        priceRangeShort = self.api.getPrices(market, self.lowerTimeframe, self.nLookbackPeriods)

        canBuy = True
        canSell = True
        for lower, upper, price in zip(lowerMovingAverageLong, upperMovingAverageLong, priceRangeLong.prices):
            if lower <= upper or price.lowPrice.price <= upper:
                canBuy = False

            if upper <= lower or price.highPrice.price >= lower:
                canSell = False

        if canBuy:
            self.goLong(market, lowerMovingAverageShort, upperMovingAverageShort, priceRangeShort)


        if canSell:
            self.goShort(market, lowerMovingAverageShort, upperMovingAverageShort, priceRangeShort)
           
    def goLong(self, market, lowerSMA, upperSMA, priceRange):
        # print ("potential buy")
        ceiling = 0
        floor = 100000

        for lower, upper, price in zip(lowerSMA[:-1], upperSMA[:-1], priceRange.prices[:-1]):

            if upper >= lower or price.lowPrice.price <= upper: # exit if these conditions occur
                # print ("unsuitable to buy")
                return 

            if price.lowPrice.price <= lower:
                floor = min((floor, lower))
            
            ceiling = max((ceiling, price.highPrice.price))

            

        if upperSMA[-1] >= lowerSMA[-1] or priceRange.prices[-1].lowPrice.price <= upperSMA[-1]: # exit if these conditions occur
            # print ("unsuitable to buy")
            return 
        

        # print(floor, ceiling, priceRange.prices[-1].closePrice.ask) 


        # recalculate current ask to make sure it's accruate
        if self.api.getCurrentPrice(market).ask >= ceiling: # reached threshold to buy
            # self.api.openPosition(market, "BUY", 10)
            log = market + str(datetime.now()) + "\n"
            with open("results.txt", "a") as results:
                results.write(log)

            # positions[market] = (floor, ceiling*2 - floor)


    def goShort(self, market, lowerSMA, upperSMA, priceRange):
        pass
        


    def getMovingAverages(self, market, nPeriods, timeframe, nLookbackPeriods):
        # returns a list of size nLookbackPeriods of moving averages
        priceRange = self.api.getPrices(market, timeframe, nPeriods + nLookbackPeriods - 1)
        return priceRange.movingAverages(nPeriods)       




    