import model
import db

from flask import Flask, request, Response, json

app = Flask(__name__)
port = 8765

@app.route('/predict', methods=['POST'])
def predict():
    data = json.dumps(request.json)

    print "----------------"
    print data
    print "----------------"

    prediction = model.predict(data)
    data['prediction'] = prediction

    db.save_prediction(data)

    resp = { 'prediction': prediction }
    return json.dumps(resp)

@app.route('/top')
def top():
    predictions = db.top_predictions()
    return predictions

if __name__ == '__main__':
    app.run(port=port, host='0.0.0.0', debug=True)

