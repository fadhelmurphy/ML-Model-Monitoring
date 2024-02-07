from flask import Flask, request, jsonify, make_response
from preprocessing import Preprocessing
import pickle

app = Flask(__name__)

response = {
    'status': 200,
    'msg': 'success',
    'data': []
}

@app.post('/predict')
def predict():
    try:
        # Lakukan prediksi menggunakan model ML
        filename = 'model.pkl'
        model = pickle.load(open(filename,'rb'))
        dp = Preprocessing()
        data = request.get_json()
        value = dp.stem(data['text'])
        value = dp.remove_stopwords(value)
        h = model.predict([value])
        if not h[0]:
            response['data'] = 'Negatif review'
        else:
            response['data'] = 'Positif review'
    except Exception as e:
        response['status'] = 500
        response['msg'] = e
    return make_response(jsonify(response), 200)

if __name__ == '__main__':
    app.run(debug=True)