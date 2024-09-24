import pandas as pd
import yfinance as yf

def Get_latest_data():
    features = ['Open', 'High', 'Low', 'Volume', 'MA10', 'MA20', 'RSI', 'Volatility']
    data = yf.download('BTC-USD', period='1mo', interval='1d')

    data = data.sort_index()

    data['MA10'] = data['Close'].rolling(window=10).mean()
    data['MA20'] = data['Close'].rolling(window=20).mean()

    delta = data['Close'].diff(1)
    delta = delta.dropna()
    up = delta.copy()
    down = delta.copy()
    up[up < 0] = 0
    down[down > 0] = 0
    time_period = 14
    avg_gain = up.rolling(window=time_period).mean()
    avg_loss = abs(down.rolling(window=time_period).mean())
    rs = avg_gain / avg_loss
    rsi = 100.0 - (100.0 / (1.0 + rs))
    data['RSI'] = rsi

    data['Volatility'] = data['Close'].rolling(window=10).std()

    data = data.dropna()

    latest_data = data.iloc[-1]
    if latest_data['Volume'] == 0 or pd.isnull(latest_data['Volume']):
        latest_data = data.iloc[-2]

    input_data = latest_data[features].to_frame().T

    return input_data
