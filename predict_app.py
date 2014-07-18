import model
from lib.json import jsonify
import db

from flask import Flask, request, Response

app = Flask(__name__)
port = 8765

@app.route('/predict', methods=['POST'])
@jsonify
def predict():
    data = request.json

    prediction = model.predict(data)
    data['prediction'] = prediction

    db.save_prediction(data)

    resp = { 'prediction': prediction }
    return resp

@app.route('/top')
@jsonify
def top():
    predictions = db.top_predictions()
    return predictions

if __name__ == '__main__':
    app.run(port=port, host='0.0.0.0', debug=True)

