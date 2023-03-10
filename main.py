import pickle
from flask import Flask, render_template, request


app = Flask(__name__)
model = pickle.load(open('C:/Users/vaish/workspace/static/model.pkl', 'rb'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict' , methods=['GET', 'POST'])
def predict():
    prediction = model.predict([[int(request.form.get('temperature'))]])
    output = round(prediction[0], 2)
    print(prediction)
    return render_template('index.html', prediction_text= f'Total revenue generated is Rs. {output}/-')

if __name__ == '__main__':
    app.run(debug=True)