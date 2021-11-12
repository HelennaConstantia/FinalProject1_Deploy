from flask import Flask, render_template, request
import numpy as np
import pickle
app=Flask(__name__)
model=pickle.load(open('model_LR.pkl','rb'))
@app.route("/")
def form():
    return render_template("LR_Predict.html")
@app.route("/predict",methods=['POST'])
def predict():
    dict_service={'Shared':0,'Lyft':1,'Lyft XL':2,
              'Lux':3,'Lux Black':4,'Lux Black XL':5,
              'UberX':6,'UberXL':7,'UberPool':8,
             'Black':9,'BlackSUV':10,'WAV':11}
    distance=float(request.form['distance'])
    surge=float(request.form['surge'])
    service=request.form['service']
    x_input=[distance,surge]
    for i in range(0,12):
        if dict_service[service]==i:
             x_input.append(1)
        else:
            x_input.append(0)
    prediction=model.predict([x_input])
    prediction=round(prediction[0],2)
    if prediction<0:
        prediction=0
  
    return render_template('LR_Predict.html',prediction_text="Price : ${}".format(prediction))

if __name__ == "__main__":
    app.run(debug=True)


