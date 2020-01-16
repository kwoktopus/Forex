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
        result = self.market.instrumentName + ":\n"
        for key in self.json:
            result += key + " " + str(self.json[key]) + "\n"

        return result

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
        result = ""
        for key in self.json:
            result += key + " " + self.json[key] + "\n"

        return result