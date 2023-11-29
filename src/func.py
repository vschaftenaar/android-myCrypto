import requests
import json

def get_saldo():
    address="DEcweqkJkCwhiaira35o9DnYvYW7sCHwom"
    lnk="https://verge-blockchain.info/api/address/"+address
    x = float(requests.get(lnk).json()['data']['balance'])
    return x

def price_info():
    lnk='https://api.binance.com/api/v3/ticker/24hr?symbols=[%22BTCEUR%22,%22XVGUSDT%22,%22ETHEUR%22,%22BTCUSDT%22,%22DOGEEUR%22]'
    ticker=requests.get(lnk).json()
    return ticker

def get_price(prices,coin,value):    
    eur=float(list(filter(lambda prices: prices['symbol'] == 'BTCEUR', prices))[0]['lastPrice'])
    usdt=float(list(filter(lambda prices: prices['symbol'] == 'BTCUSDT', prices))[0]['lastPrice'])
    ex=eur/usdt  
    if value == 'usdt':
        convert = ex
    else:
        convert = 1
    x=list(filter(lambda prices: prices['symbol'] == coin.upper()+value.upper(), prices))[0]
    x={'price': float(x['lastPrice'])*convert,'change': float(x['priceChangePercent'])}
        

    return x

def portfolio_str(price,n):
    x=str('\u20ac ' + f"{round(price*n,2):,}")
    return x

#def price_watch_str(price_info):
#    x=str('BTC : \u20ac' + str(f"{round(btc,2):,}")+'\nXVG : \u20ac' + str(xvg))
#    return x


def price_watch_str(price_info):
    btc=get_price(price_info,'btc','eur')
    eth=get_price(price_info,'eth','eur')
    xvg=get_price(price_info,'xvg','usdt')   
    doge=get_price(price_info,'doge','eur')

    price_len = 13
    btc_spaces=price_len-len(str(f"{round(btc['price'],2):,}"))
    xvg_spaces=price_len-len(str(f"{round(xvg['price'],6):,}"))
    eth_spaces=price_len-len(str(f"{round(eth['price'],2):,}"))
    doge_spaces=price_len-len(str(f"{round(doge['price'],2):,}"))
    
    spaces='                 '    

    x=str(
            'BTC  : \u20ac' + str(f"{round(btc['price'],2):,}"+spaces[0:btc_spaces]+'('+str(btc['change'])+'%)')
         +'\nXVG  : \u20ac' + str(f"{round(xvg['price'],6):,}"+spaces[0:xvg_spaces]+'('+str(xvg['change'])+'%)')
         +'\nETH  : \u20ac' + str(f"{round(eth['price'],2):,}"+spaces[0:eth_spaces]+'('+str(eth['change'])+'%)')
         +'\nDOGE : \u20ac' + str(f"{round(doge['price'],2):,}"+spaces[0:doge_spaces]+'('+str(doge['change'])+'%)')
        )

    return x

#price_info=price_info()
#print(price_watch_str(price_info))
