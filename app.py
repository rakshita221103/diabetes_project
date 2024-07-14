from flask import *
import pandas as pd
from sklearn.linear_model import LinearRegression

app=Flask(__name__)
####################################
url = "https://raw.githubusercontent.com/sarwansingh/Python/master/ClassExamples/data/diabetes.csv"
df = pd.read_csv(url)
df.gender.unique()
df.gender.replace(['Male','Female','Other'],[1,2,3],inplace=True)
df.smoking_history.unique()
df.smoking_history.replace(['never', 'No Info', 'current', 'former', 'ever', 'not current'],[1,2,3,4,5,6],inplace=True)

X = df[['gender',	'age'	,'hypertension'	,'heart_disease',	'smoking_history'	,'bmi'	,'HbA1c_level',	'blood_glucose_level'	]]
Y = df['diabetes']

from sklearn.linear_model import LinearRegression
model = LinearRegression( )
model.fit(X, Y)
res = model.predict([[2,67.0,0,0,3,19,6.6,200]])
op= (str( round(res[0]*100 ,2)) + "%")
###################################

@app.route('/')
def hello_world():
  return render_template("index.html")
  # return 'HELLO AIML FOR PYTHON WEB DEVELOPMENT !!' + op  

@app.route('/project')
def project():
  return render_template("form.html") 
 
@app.route('/predict',methods=['POST'])
def predict():
  gender=int(request.form['gender'])
  age=float(request.form['age'])
  hypertension=int(request.form['hypertension'])
  heartdisease=int(request.form['heartdisease'])  
  smokinghistory=int(request.form['smokinghistory'])
  bmi=float(request.form['bmi'])
  hba1clevel=float(request.form['hba1clevel'])
  bloodglucoselevel=float(request.form['bloodglucoselevel'])
  
  res=model.predict([[gender,age,hypertension,heartdisease,smokinghistory,bmi,hba1clevel,bloodglucoselevel]])
  op=res[0]
  if op==1:
     result='Predicted Result :'+'DIABETES'
  else:
     result='Predicted Result :'+'NO DIABETES'
     return render_template("form.html",result=result) 
  # op="Predicted Result :"+ (str(round(res[0]*100 ,2)) + "%")
  # return render_template("form.html",result=op) 
  
@app.route('/home')
def home():
  return render_template("index.html")

if __name__=='__main__':
  app.run(debug=True)        