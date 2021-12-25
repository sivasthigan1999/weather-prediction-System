import pyrebase
import json

firebaseConfig={'apiKey': "AIzaSyDz1Tx7KXLJqFBwRbk6MtBQNEsJyhTk4cQ",
  'authDomain': "rainfallprediction-24923.firebaseapp.com",
  'projectId': "rainfallprediction-24923",
  'storageBucket': "rainfallprediction-24923.appspot.com",
  'messagingSenderId': "48101360372",
  'appId': "1:48101360372:web:7ff9204dcc367f587e54a1",
  'measurementId': "G-3D0N7LEM9K",
  "databaseURL":"https://rainfallprediction-24923-default-rtdb.asia-southeast1.firebasedatabase.app/-Ml9x5DCLYqfz1cYfrj3"}

firebase=pyrebase.initialize_app(firebaseConfig)

db=firebase.database()



from flask import Flask, render_template, request
import pickle
import numpy as np


modelc1 = pickle.load(open('colombodaily_binary_01.pickle', 'rb'))
modelc2 = pickle.load(open('colombodailyrange_new01.pickle', 'rb'))
modelv1 = pickle.load(open('vavuniya_dailybinary1.pickle', 'rb'))
modelv2 = pickle.load(open('vavuniya_dailyrange1.pickle', 'rb'))
modelk1 = pickle.load(open('katugastota_dailybinary.pickle', 'rb'))
modelk2 = pickle.load(open('katugastota_dailyrange.pickle', 'rb'))
app = Flask(__name__)


@app.route('/')
def man():
    return render_template('Home.html')


@app.route('/Prediction', methods=['POST'])
def Home():
    data1 = request.form['a']
    data2 = request.form['b']
    data3 = request.form['c']
    data4 = request.form['d']
    data5 = request.form['Location']
    


    if data5=='colombo':
        
        arr = np.array([[data1, data2, data3, data4]])
        pred = modelc1.predict(arr)
        lists = pred.tolist()
        json_str = json.dumps(lists)
        arr2= np.array([[data1, data2, data3, data4,pred]])
        pred2 = modelc2.predict(arr2)
        lists1 = pred2.tolist()
        json_str1 = json.dumps(lists1)
        dat={"Month":data1,"Tem_Max":data2,"Pressure":data3,"RH_Min":data4,"Location":data5,"Rain or not":json_str,"Rain range":json_str1}
        db.push(dat)
        return render_template('Prediction.html',data=pred2,data0=pred)



        
    
    elif data5=='vavuniya':
        arr = np.array([[data1, data2, data3, data4]])
        pred = modelv1.predict(arr)
        lists = pred.tolist()
        json_str = json.dumps(lists)
        arr2= np.array([[data1, data2, data3, data4,pred]])
        pred2 = modelv2.predict(arr2)
        lists1 = pred2.tolist()
        json_str1 = json.dumps(lists1)
        dat={"Month":data1,"Tem_Max":data2,"Pressure":data3,"RH_Min":data4,"Location":data5,"Rain or not":json_str,"Rain range":json_str1}
        db.push(dat)

        return render_template('Prediction.html',data=pred2,data0=pred)
 
    
    elif data5=='katugastota':
        arr = np.array([[data1, data2, data3, data4]])
        pred = modelk1.predict(arr)
        lists = pred.tolist()
        json_str = json.dumps(lists)
        arr2= np.array([[data1, data2, data3, data4,pred]])
        pred2 = modelk2.predict(arr2)
        lists1 = pred2.tolist()
        json_str1 = json.dumps(lists1)
        dat={"Month":data1,"Tem_Max":data2,"Pressure":data3,"RH_Min":data4,"Location":data5,"Rain or not":json_str,"Rain range":json_str1}
        db.push(dat)

        return render_template('Prediction.html',data=pred2,data0=pred)





if __name__ == "__main__":
    app.run(debug=True)
