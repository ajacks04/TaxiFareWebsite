import streamlit as st
import requests
import datetime


'''
# Taxi Fare Prediction
'''

st.markdown('''
## Please provide the following inputs to calculate the approximate taxi fare.

''')

dt = str(st.date_input("Pickup date:", datetime.datetime(2021, 2, 26)))
tm = str(st.time_input('Pickup time:', datetime.time(8, 45)))
pickup_datetime = dt+' '+tm+' UTC'

passenger_count = st.number_input('Passenger count',value=1)
pickup_latitude = st.number_input('Pickup latitude',value=1)
pickup_longitude = st.number_input('Pickup longitude',value=1)
dropoff_latitude = st.number_input('Dropoff latitude',value=1)
dropoff_longitude = st.number_input('Dropoff longitude',value=1)

url = 'https://taxfaremodel-t46mh5ncta-ew.a.run.app/predict_fare/'

params = {
    "key" : "2012-10-06 12:10:20.0000001",
    "pickup_datetime" : pickup_datetime,
    "pickup_longitude" : pickup_longitude, 
    "pickup_latitude" : pickup_latitude, 
    "dropoff_longitude" : dropoff_longitude,
    "dropoff_latitude" : dropoff_latitude,
    "passenger_count" : int(passenger_count)
}

params2 = {
    "key" : "2012-10-06 12:10:20.0000001",
    "pickup_datetime" : "2012-10-06 12:10:20 UTC",
    "pickup_longitude" : 40.7614327, 
    "pickup_latitude" : 73.9798156, 
    "dropoff_longitude" : 40.6513111,
    "dropoff_latitude" : -73.8803331,
    "passenger_count" : 3
}


if st.button('Submit'):
    # print is visible in server output, not in the page
    print('button clicked!')
    st.write('Submitted 🎉')
    st.write('Further clicks are not visible but are executed')
    response = requests.get(url, params=params).json()
    (prediction, price), *rest = response.items()
    fare = round(price, 2)

    st.write(f'Your fare will be approximately $', fare)
    print(response)
else:
    st.write('I was not clicked 😞')
