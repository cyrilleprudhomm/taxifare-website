import streamlit as st
import requests
import numpy as np

'''
# Estimateur Taxifare
'''
url = 'https://taxifare.lewagon.ai/predict'

defaultdico = {
        "pickup_datetime" : "2013-07-06 17:18:00",
        "pickup_longitude":-73.950655,
        "pickup_latitude":40.783282,
        "dropoff_longitude":-73.984365,
        "dropoff_latitude":40.769802,
        "passenger_count":1
    }

if "dico" not in st.session_state:
    st.session_state['dico'] = defaultdico

amount={'fare':0}

with st.form("my_form"):
    '''## Où allons-nous ? 🚕'''
    pickup_datetime = st.text_input("date and time", st.session_state['dico']['pickup_datetime'])
    pickup_longitude = st.text_input("pickup longitude", st.session_state['dico']['pickup_longitude'])
    pickup_latitude = st.text_input("pickup latitude", st.session_state['dico']['pickup_latitude'])
    dropoff_longitude = st.text_input("dropoff longitude", st.session_state['dico']['dropoff_longitude'])
    dropoff_latitude = st.text_input("dropoff latitude", st.session_state['dico']['dropoff_latitude'])
    passenger_count = st.text_input("passenger count", st.session_state['dico']['passenger_count'])

    st.session_state['dico'] = {
        "pickup_datetime" : pickup_datetime,
        "pickup_longitude": pickup_longitude,
        "pickup_latitude":pickup_latitude,
        "dropoff_longitude":dropoff_longitude,
        "dropoff_latitude":dropoff_latitude,
        "passenger_count":passenger_count
    }
    if st.form_submit_button('Quel est le prix ?'):
        r = requests.get(url, params=st.session_state['dico'])
        amount = r.json()
        st.markdown(f'''
            ## 💵 prix de la course : {round(amount['fare'], 2)} $
        ''')
    else:
        st.markdown(f'''
            ## 💵 prix de la course : {0.00} $
        ''')
#if st.button("Reset", type="primary"):
#    st.session_state['dico'] = defaultdico
