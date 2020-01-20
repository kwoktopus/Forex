class Position:
    def __init__(self, json):
        self.json = json['position']
        
        positionJson = self.json

        self.market = Market(json['market'])

        self.contractSize = positionJson['contractSize']
        self.dealId = positionJson['dealId']
        self.dealReference = positionJson['dealReference']
        self.size = positionJson['size']
        self.direction = positionJson['direction']
        self.limitLevel = positionJson['limitLevel']
        self.level = positionJson['level']
        self.currency = positionJson['currency']
        self.controlledRisk = positionJson['controlledRisk']
        self.stopLevel = positionJson['stopLevel']
        self.trailingStep = positionJson['trailingStep']
        self.trailingStopDistance = positionJson['trailingStopDistance']
        self.limitedRiskPremium = positionJson['limitedRiskPremium']

    def __str__(self):
        return "Position" + formatJson(self.json)

class Market:
    def __init__(self, json):
        self.json = json
        self.instrumentName = json['instrumentName']
        self.expiry = json['expiry']
        self.epic = json['epic']
        self.instrumentType = json['instrumentType']
        self.lotSize = json['lotSize']
        self.high = json['high']
        self.low = json['low']
        self.percentageChange = json['percentageChange']
        self.netChange = json['netChange']
        self.bid = json['bid']
        self.offer = json['offer']
        self.updateTime = json['updateTime']
        self.updateTimeUTC = json['updateTimeUTC']
        self.delayTime = json['delayTime']
    
    def __str__(self):
        return "Market" + formatJson(self.json)
    
class PricesRange:
    def __init__(self, json, timeFrame, market):
            
        self.market = market
        self.json = json
        if "errorCode" in json:
            self.prices = []
        else:
            self.prices = [Prices(price) for price in json['prices']]
        
        self.timeFrame = timeFrame
        self.nPeriods = len(self.prices)


    def movingAverage(self, start, end):
        if (start >= end):
            return 0
        
        avg = 0 
        for price in self.prices[start:end]:
            avg += price.closePrice.price

        return avg/(end - start)   
    
    def movingAverages(self, nPeriods):
        if nPeriods > len(self.prices) or nPeriods < 1:
            return []            

        results = []

        runningAvg = 0
        for price in self.prices[:nPeriods]:
            runningAvg += price.closePrice.price

        results.append(runningAvg/nPeriods)

        for i in range(nPeriods, len(self.prices)):
            runningAvg += self.prices[i].closePrice.price
            runningAvg -= self.prices[i - nPeriods].closePrice.price

            results.append(runningAvg/nPeriods)

        return results

    def __str__(self):
        return "PricesRange" + formatJson(self.json)

class Prices:
    def __init__(self, json):
        self.json = json
        self.time = json['snapshotTime']
        self.timeUTC = json['snapshotTimeUTC']
        self.openPrice = Price(json['openPrice'])
        self.closePrice = Price(json['closePrice'])
        self.highPrice = Price(json['highPrice'])
        self.lowPrice = Price(json['lowPrice'])
        self.lastTradedVolume = json['lastTradedVolume']

    def __str__(self):
        return "Prices" + formatJson(self.json)


class Price:
    def __init__(self, json):
        self.json = json
        self.bid = json['bid']
        self.ask = json['ask']
        self.price = (self.bid + self.ask)/2 # avg of bid and ask to calculate price
        self.lastTraded = json['lastTraded']
    
    def __str__(self):
        return "Price" + formatJson(self.json)







def formatJson(json):
    result = ""
    for key in json:
        value = json[key]
        result += ("\n|%s| = |%s|" % (key, value))

    return result


