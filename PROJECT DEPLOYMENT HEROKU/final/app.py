# save this as app.py
from flask import Flask,request, render_template
import pickle
import numpy as np



app = Flask(__name__)
gtb = pickle.load(open('model.pkl','rb'))


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['GET','POST'])
def predict():
    if request.method ==  'POST':
        Gender = request.form['Gender']
        Married = request.form['Married']
        Dependents = request.form['Dependents']
        Education = request.form['Education']
        Self_Employed = request.form['Self_Employed']
        Credit_History = float(request.form['Credit_History'])
        Property_Area = request.form['Property_Area']
        ApplicantIncome = float(request.form['ApplicantIncome'])
        CoapplicantIncome = float(request.form['CoapplicantIncome'])
        LoanAmount = float(request.form['LoanAmount'])
        Loan_Amount_Term = float(request.form['Loan_Amount_Term'])
        

            
        # gender
        if (Gender == "Male"):
            Gender=1
        else:
            Gender=0
        
        # married
        if(Married=="Yes"):
            Married = 1
        else:
            Married=0

        # dependents
        if(Dependents=='1'):
            Dependents = 1
        elif(Dependents == '2'):
            Dependents = 2
        elif(Dependents=='3+'):
            Dependents = 3
        else:
            Dependents = 0 

        # education
        if (Education=="Graduate"):
            Education=1
        else:
            Education=0

        # employed
        if (Self_Employed == "Yes"):
            Self_Employed = 1
        else:
            Self_Employed = 0

        # property area

        if(Property_Area=="Urban"):
            Property_Area=2
        elif(Property_Area=="Rural"):
            Property_Area=0
        else:
            Property_Area=1
            

        Total_Income = ApplicantIncome + CoapplicantIncome
    
       
        
 
        prediction = gtb.predict([[Gender , Married , Dependents , Education , Self_Employed ,Credit_History , Property_Area , Total_Income , LoanAmount , Loan_Amount_Term]])
        

        if(prediction==1):
            prediction="Eligible"
        elif(prediction==0):
            prediction="Not Eligible"
        else:
            print("fill correct info")            


        return render_template("prediction.html", prediction_text="Customer is {}".format(prediction))




    else:
        return render_template("prediction.html")



if __name__ == "__main__":
    app.run(debug=True)
