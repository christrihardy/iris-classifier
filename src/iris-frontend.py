import streamlit as st
from PIL import Image
import requests

# header images
image = Image.open('assets/header-iris.png')
st.image(image)
st.title("Iris classifier app")
st.markdown('by: chris')
st.divider()
st.subheader("type the value then click predict")

# form input
with st.form("iris-ap-form"):
    sepal_length = st.number_input("Sepal length:", help="0.5")
    sepal_width = st.number_input("Sepal width:", help="0.2")
    petal_length = st.number_input("petal length:", help="0.3")
    petal_width = st.number_input("petal width:", help="0.1")

    # submmit button
    submitted = st.form_submit_button("Predict")

    #check if button clicked
    if submitted:
        # post data
        data = {
            "sepal_length": sepal_length,
            "sepal_width": sepal_width,
            "petal_length": petal_length,
            "petal_width": petal_width
        }

        # post request
        response = requests.post('http://backend:8000/predict', json = data)  

        # get response
        result = response.json()

        # check response
        if result['code'] == 200:
            messages = "the flower is: " + result['prediction'] + " Iris"
            st.success(messages)

        else:
            st.error(result['messages'])



