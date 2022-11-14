import streamlit as sl
import pickle
import numpy as np
import pandas as pd

file1=open("model.pkl","rb")
file2=open("scale.pkl","rb")

model=pickle.load(file1) #to read data from file1 and hold on object of model(user defined)
scale=pickle.load(file2)

sl.write(" # Heart_Disease Prediction ")
age=sl.number_input("Enter Age: ",format='%d',value=0) #only accept input in one line number_input is used to accept number as input
#text_input() inbuilt function which is used to accept string data from user on runtime
sex=sl.number_input("Enter sex 1-Male,0-Female: ",format='%d',min_value=0,max_value=1,value=0)
cp=sl.number_input("Enter :chest pain type 0-4  ")
trestbps=sl.number_input("Enter 'Resting Blood Sugar : 1-500 ")
chol=sl.number_input("Enter Serum Cholestoral in mg/dl 1-1000 ")
fbs=sl.number_input("EnterFasting Blood Sugar higher than 120 mg/dl Y-yes / N-No ")
restecg=sl.number_input("Enter Resting Electrocardiographic Results0,1,2,(ST Wave abnormality,Possible,definite left ventricular hypertroph "))
thalach=sl.number_input('Enter Maximum Heart Rate Achieved, 1-300')
exang=sl.number_input('EnterExercise Induced Angina,  Y-yes / N-No ')
oldpeak=sl.number_input('Oldpeak')
slope=sl.number_input(' Enter Slope ,0- Better Heart Rate With Excercise, 1-Typical Healthy Heart , 2-Unhealthy Heart  ')
ca=sl.number_input('Enter Number of Major Vessels Colored by Flourosopy, 0-5')
thal=sl.number_input('Enter Thalium Stress Result, 1-8')
if sl.button("Predict"):  #button is inbuilt function to get button
    features=[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]#create list of features in sequence with respect to dataframe
    #to change all the input features in numpy 2D array np.array():
    final_features=[np.array(features)]
    #Apply scaling on final_features
    final_features=scale.transform(final_features)
    Y_pred=model.predict(final_features)[0]
    if Y_pred==0:
        ans=" # Customer will not claim for Insurance"
    else:
        ans=" # Customer will claim for Insurance"
        
    sl.write(ans)
    #ans=np.where(Y_pred==0,"Customer will not claim for Insurance :,"Customer will claim Insurance]