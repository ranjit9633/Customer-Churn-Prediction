import numpy as np
import pickle
import pandas as pd
import streamlit as st

from PIL import Image

pickle_in = open("bagging_clf.pkl", "rb")
bagging_clf = pickle.load(pickle_in)

def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://p4.wallpaperbetter.com/wallpaper/25/1010/360/nature-black-widow-light-digital-wallpaper-preview.jpg");
             background-attachment: fixed;
	     background-position:75%;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url()

def welcome():
    return "Welcome All"



def predict_note_authentication(voice_plan,voice_messages,intl_plan,day_min,day_charge,eve_mins,eve_charge,customer_calls):


    prediction =bagging_clf.predict([[voice_plan,voice_messages,intl_plan,day_min,day_charge,eve_mins,eve_charge,customer_calls]])
    print(prediction)
    return prediction


# noinspection PyUnreachableCode
def main():
    st.title("Customer Churn Prediction")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Customer Churn Prediction ML App </h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    voice_plan = st.text_input("voice_plan", "Type Here")
    voice_messages = st.text_input("voice_messages", "Type Here")
    intl_plan = st.text_input("intl_plan", "Type Here")
    day_min = st.text_input("day_min", "Type Here")
    day_charge = st.text_input("day_charge", "Type Here")
    eve_mins = st.text_input("eve_mins", "Type Here")
    eve_charge = st.text_input("eve_charge", "Type Here")
    customer_calls = st.text_input("customer_calls", "Type Here")

    result = ""
    if st.button("Predict"):
        result = predict_note_authentication(voice_plan,voice_messages,intl_plan,day_min,day_charge,eve_mins,eve_charge,customer_calls)
    st.success('The output is {}'.format(result))
    if st.button("About"):
        st.text("Lets LEarn")
        st.text("Built with Streamlit")


if __name__ == '__main__':
    main()