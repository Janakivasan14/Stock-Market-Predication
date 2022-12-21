def histo():
    import pandas_datareader as web
    df = web.DataReader('RELIANCE.NS', data_source='yahoo', start='2012-01-01', end='2020-02-24')
    s=[df.columns.tolist()] + df.reset_index().values.tolist()
    historical_dates=[]
    histo={}
    historical_price=[]
    for i in s:
        t=str(i[0])
        historical_dates.append(t[:11])
        historical_price.append(i[3])
    historical_dates.remove("High")
    historical_price.remove("Close")
    return historical_dates,historical_price

