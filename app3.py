import streamlit as st
import numpy as np
import pandas as pd
import pickle


pipe = pickle.load(open("pipe.pkl", "rb+"))
df = pd.read_csv("final_data.csv")
#st.title("Food delivery time Prediction App")
st.image("food.jpg")
backgroundColor ="#E8F0FE"
st.set_page_config(
    page_title="Food Delivery Time Predictor",
    page_icon="🍔",
    layout="centered"
)

st.title("🍔 Food Delivery Time Prediction App")
st.markdown("Predict food delivery time quickly and accurately.")
st.markdown("---")

pipe = pickle.load(open("pipe.pkl","rb"))
df = pd.read_csv("final_data.csv")


distances=sorted(df['Distance_km'].unique())
Distance_km=st.selectbox("select distance",distances)
Weathers=sorted(df['Weather'].unique())
Weather=st.selectbox("select weather",Weathers)
Traffic_Levels=sorted(df['Traffic_Level'].unique())
Traffic_level=st.selectbox("select traffic level",Traffic_Levels)
Time_of_Days=sorted(df['Time_of_Day'].unique())
Time_of_Day=st.selectbox("select traffic level",Time_of_Days)
Vehicle_Types=sorted(df['Vehicle_Type'].unique())
Vehicle_Type=st.selectbox("select Vehicle_Type",Vehicle_Types)
Preparation_Time_mins=sorted(df['Preparation_Time_min'].unique())
Preparation_Time_min=st.selectbox("select Preparation Time min",Preparation_Time_mins)
Courier_Experience_yrss=sorted(df['Courier_Experience_yrs'].unique())
Courier_Experience_yrs=st.selectbox("select Courier Experience yrs",Courier_Experience_yrss)

if st.button('predict time'):
    st.write("you have selected")
    st.write(f"Distance: {Distance_km}")
    st.write(f"Weather: {Weather}")
    st.write(f"Traffic_level: {Traffic_level}")
    st.write(f"Time_of_Day: {Time_of_Day}")
    st.write(f"Vehicle_Type: {Vehicle_Type}")
    st.write(f"Preparation_Time_min: {Preparation_Time_min}")
    st.write(f"Courier_Experience_yrs: {Courier_Experience_yrs}")

    myinput=[[Distance_km, Weather,Traffic_level,Time_of_Day,
        Vehicle_Type,Preparation_Time_min,Courier_Experience_yrs]]
    columns=['Distance_km', 'Weather', 'Traffic_Level', 'Time_of_Day',
        'Vehicle_Type', 'Preparation_Time_min', 'Courier_Experience_yrs']
    myinput=pd.DataFrame(data=myinput,columns=columns)
    result=pipe.predict(myinput)
    st.markdown("---")

    
    if result[0,0] < 0:
        st.write("Sorry, the predicted price is negative. Please check your input values.")
    else:
        #st.write("Predicted time is:", str(round(result[0,0])))
        st.metric("🚚 Estimated Delivery Time",f"{round(result[0,0])} min")

        st.success("Prediction completed successfully!")
        st.info("Fill all details before predicting")
        

