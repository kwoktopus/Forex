import plotly.graph_objects as plot
from entities import *


class Graph():
    def __init__(self, priceRange):
        self.priceRange = priceRange
        self.x = [p.time for p in priceRange.prices]
        
        self.reset()


    def addCandlesticks(self):
        prices = self.priceRange.prices

        times = self.x
        openPrices = [p.openPrice.price for p in prices]
        closePrices = [p.closePrice.price for p in prices]
        highPrices = [p.highPrice.price for p in prices]
        lowPrices = [p.lowPrice.price for p in prices]

        data = plot.Candlestick(x=times, open=openPrices, high=highPrices, low=lowPrices, close=closePrices,\
                                increasing_line_color= 'green', decreasing_line_color= 'red')

        self.graph.add_trace(data)

    def addMovingAverage(self, nPeriods):
        movingAverages = []
        for i in range(len(self.x) - nPeriods + 1):
            movingAverages.append(self.priceRange.movingAverage(i, i + nPeriods))

        data = plot.Scatter(x=self.x[nPeriods - 1:], y=movingAverages)
        self.graph.add_trace(data)
    
    def reset(self):
        self.graph = plot.Figure()
        self.graph.update_layout(title=self.priceRange.market, xaxis_title="time", yaxis_title='price')
        
    def show(self):
        self.graph.show()
