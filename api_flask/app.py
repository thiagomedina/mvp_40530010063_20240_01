from flask import Flask, request, jsonify
import joblib
import numpy as np
import pandas as pd
import yfinance as yf
from datetime import datetime, timedelta
from flask_cors import CORS, cross_origin
from services.get_lastest_data import Get_latest_data
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


model = joblib.load('bitcoin_trend_model.pkl')

@app.route('/trend', methods=['GET'])
def predict():

    input_data = Get_latest_data()
    prediction = model.predict(input_data)

    result = {
        'trend': int(prediction[0]),
        'description': 'Alta' if prediction[0] == 1 else 'Baixa'
    }

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
