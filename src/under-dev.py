
def get_hist_data(coin,value,interval):
    market = coin.upper()+value.upper()
    tick_interval = interval
    lnk = 'https://api.binance.com/api/v3/klines?symbol='+market+'&interval='+tick_interval+'&limit=50'
    x=requests.get(lnk).json()
    df=pd.DataFrame(x)
    df.columns=  ['open_time','open','high','low','close','vol','close_time','quote','trades','buy_base','buy_quote','ignore']
    df['t']=pd.to_datetime(df['open_time'].astype(int)/1000,unit='s')
    return df

def make_plot(prices):

    #def make_plot(prices):
    plt.figure()

    #define width of candlestick elements
    width = .8
    width2 = .15

    #define up and down prices
    up = prices[prices.close>=prices.open]
    down = prices[prices.close<prices.open]

    #define colors to use
    col1 = 'black'
    col2 = 'steelblue'

    #plot up prices
    plt.bar(up.t,up.close.astype(float)-up.open.astype(float),width,bottom=up.open.astype(float),color=col1)
    plt.bar(up.t,up.high.astype(float)-up.close.astype(float),width2,bottom=up.close.astype(float),color=col1)
    plt.bar(up.t,up.low.astype(float)-up.open.astype(float),width2,bottom=up.open.astype(float),color=col1)

    #plot down prices
    plt.bar(down.t,down.close.astype(float)-down.open.astype(float),width,bottom=down.open.astype(float),color=col2)
    plt.bar(down.t,down.high.astype(float)-down.open.astype(float),width2,bottom=down.open.astype(float),color=col2)
    plt.bar(down.t,down.low.astype(float)-down.close.astype(float),width2,bottom=down.close.astype(float),color=col2)

    #rotate x-axis tick labels
    plt.xticks(rotation=45, ha='right')

    #display candlestick chart
    plt.show()

