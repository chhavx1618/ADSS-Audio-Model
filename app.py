from flask import Flask, request, jsonify
from model_predict import predict_class

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    text = data['text']
    prediction = predict_class(text)
    return jsonify({'class': prediction})

if __name__ == '__main__':
    app.run(debug=True, port=3000)
    
    
# http://127.0.0.1:8000/detect