# import requests
from API import API
from userData import *
import time





api = API(API_KEY, USERNAME, PASSWORD)

market = "CS.D.AUDUSD.MINI.IP"
timeFrame = "MINUTE"
nPeriods = 10

priceRange = api.getPrices(market, timeFrame, nPeriods)




