import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

application = Flask(__name__) #Initialize the flask App
model = pickle.load(open('model.pkl', 'rb'))

@application.route('/')
def home():
    return render_template('index.html')

@application.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = round(prediction[0], 2)
    
    if output == 1:
        return render_template('index.html', prediction_text='YES ! he/she will donate blood as binary output is {}'.format(output))
    else:
        return render_template('index.html', prediction_text='NO ! he/she will not donate blood as binary output is {}'.format(output))


if __name__ == "__main__":
    application.run(debug=True)