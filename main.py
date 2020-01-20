from API import API
from userData import *
from graph import Graph

api = API(API_KEY, USERNAME, PASSWORD)


market = "CS.D.AUDUSD.MINI.IP"
timeFrame = "MINUTE"
nPeriods = 100

priceRange = api.getPrices(market, timeFrame, nPeriods)
graph = Graph(priceRange)
graph.addCandlesticks()
graph.addMovingAverage(8)
graph.addMovingAverage(23)

graph.show()


