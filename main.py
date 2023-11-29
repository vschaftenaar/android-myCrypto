from src.func import *

import kivy 
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
#import pandas as pd
#from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg

kivy.require("1.9.1") 

class Root(BoxLayout):
    n=get_saldo()
    prices=price_info()
    xvg = round(float(get_price(prices,'xvg','usdt')['price']),6)
    portfolio_init=portfolio_str(xvg,n)
    price_watch_init=price_watch_str(prices)
    

class myCrypto(App):
    def build(self):
        return Root()

    def on_start(self):
        Clock.schedule_interval(self.update_portfolio, 2)        
             
    def update_portfolio(self,*args):
        n=get_saldo()
        prices=price_info()
        xvg = round(float(get_price(prices,'xvg','usdt')['price']),6)
        self.root.ids.portfolio.text=portfolio_str(xvg,n)
        self.root.ids.price_watch.text=price_watch_str(prices)


myCrypto().run()
