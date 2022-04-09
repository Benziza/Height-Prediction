from flask import Flask,request, url_for, redirect, render_template
import pickle
import numpy as np

app = Flask(__name__)

model=pickle.load(open('model.pkl','rb'))


@app.route('/')
def hello_world():
    return render_template("your_height.html")


@app.route('/predict',methods=['POST','GET'])
def predict():
    int_features=[int(x) for x in request.form.values()]
    final=[np.array(int_features)]
    prediction=model.predict(final)
    # output='{0:.{1}f}'.format(prediction, 2)

    return render_template('your_height.html',pred='Your height is : {}'.format(prediction),bhai="what do you think?")

if __name__ == '__main__':
    app.run(debug=True)
