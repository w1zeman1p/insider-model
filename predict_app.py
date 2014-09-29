import model
import db
from flask import Flask, request, Response, json

app = Flask(__name__)
port = 8765

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    prediction = model.predict(data)
    data['prediction'] = prediction[0]
    db.save_prediction(data)
    resp = { 'prediction': prediction[0] }
    return json.dumps(resp)

@app.route('/top')
def top():
    predictions = db.top_predictions()
    return predictions

if __name__ == '__main__':
    app.run(port=port, host='0.0.0.0', debug=True)
