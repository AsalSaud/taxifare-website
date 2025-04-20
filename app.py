import streamlit as st
import requests
import datetime

'''
# TaxiFareModel front
'''

st.markdown('''
Remember that there are several ways to output content into your web page...

Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
''')

'''
## Here we would like to add some controllers in order to ask the user to select the parameters of the ride

1. Let's ask for:
- date and time
- pickup longitude
- pickup latitude
- dropoff longitude
- dropoff latitude
- passenger count
'''

'''
## Once we have these, let's call our API in order to retrieve a prediction

See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

🤔 How could we call our API ? Off course... The `requests` package 💡
'''
# date and time of the ride
d = str(st.date_input(
    "When's your taxi ride?",
    datetime.date(2019, 7, 6)))
st.write('Your ride is on:', d)

t = str(st.time_input('Time of your ride', datetime.time(8, 45)))
st.write("You're taking a taxi at the following time:", t)

date_and_time = d + ' ' + t

date_and_time = datetime.datetime.strptime(date_and_time, '%Y-%m-%d %H:%M:%S')

st.write(date_and_time)

#pickup_longitude
pickup_longitude = st.number_input('enter pickup longitude:', step=0.0001, min_value=-180.0, max_value=180.0)
st.write(pickup_longitude)

#pickup_latitude
pickup_latitude = st.number_input('enter pickup latitude:', step=0.0001, min_value=-90.0, max_value=90.0)
st.write(pickup_latitude)

#dropoff_logitude
dropoff_logitude = st.number_input('enter dropoff longitude:', step=0.0001, min_value=-180.0, max_value=180.0)
st.write(dropoff_logitude)

#dropoff_latitude
dropoff_latitude = st.number_input('enter dropoff latitude:', step=0.0001, min_value=-90.0, max_value=90.0)
st.write(dropoff_latitude)

#passenger_count
passenger_count = st.number_input("Number of passengers:",min_value=1,max_value=10,step=1)
st.write(passenger_count)

'''

2. Let's build a dictionary containing the parameters for our API...

3. Let's call our API using the `requests` package...

4. Let's retrieve the prediction from the **JSON** returned by the API...

## Finally, we can display the prediction to the user
'''

url = 'https://taxifare.lewagon.ai/predict'
params = {'pickup_datetime': date_and_time,
          'pickup_longitude': pickup_longitude,
          'pickup_latitude': pickup_latitude,
          'dropoff_longitude': dropoff_logitude,
          'dropoff_latitude': dropoff_latitude,
          'passenger_count': passenger_count}

if url == 'https://taxifare.lewagon.ai/predict':

    response = requests.get(url, params=params)
    st.write(response.json())
