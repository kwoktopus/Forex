from API import API
from userData import *
from graph import Graph
from strategy import Strategy1
from markets import markets

api = API(API_KEY, USERNAME, PASSWORD)
market = "CS.D.AUDUSD.MINI.IP"
market = "CS.D.AUDNZD.MINI.IP"


lowerSMA = 8
upperSMA = 21
lowerTimeframe = "MINUTE_5"
upperTimeframe = "HOUR"
nLookbackPeriods = 5

strategy1 = Strategy1(api, markets, lowerSMA, upperSMA, lowerTimeframe, upperTimeframe, nLookbackPeriods)
while (True):
    strategy1.execute()







if (False): # graph info
    timeFrame = "MINUTE_5"
    nPeriods = 50
    priceRange = api.getPrices(market, timeFrame, nPeriods)

    graph = Graph(priceRange)
    graph.addCandlesticks()
    graph.addMovingAverage(8)
    graph.addMovingAverage(21)



