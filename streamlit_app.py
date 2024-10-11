import streamlit as st
import cv2
import numpy as np
import tensorflow as tf

# Load the pre-trained models for age and gender detection
age_model = tf.keras.models.load_model('path_to_age_model.h5')  # Update with your model path
gender_model = tf.keras.models.load_model('path_to_gender_model.h5')  # Update with your model path

# Define a function to preprocess the input image
def preprocess_image(image):
    # Convert to RGB and resize for the model
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = cv2.resize(image, (64, 64))  # Assuming the model input size is 64x64
    image = image / 255.0  # Normalize
    return np.expand_dims(image, axis=0)

# Define a function for age and gender prediction
def predict_age_gender(image):
    processed_image = preprocess_image(image)
    gender_prediction = gender_model.predict(processed_image)
    age_prediction = age_model.predict(processed_image)

    gender = 'Male' if gender_prediction[0][0] > 0.5 else 'Female'
    age = int(age_prediction[0][0] * 100)  # Assuming output is a normalized value

    return age, gender

# Streamlit interface
st.title("Self Kiosk: Face, Age, and Gender Detection")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Read the image
    image = np.array(cv2.imdecode(np.frombuffer(uploaded_file.read(), np.uint8), cv2.IMREAD_COLOR))
    
    # Display the uploaded image
    st.image(image, channels="RGB", caption="Uploaded Image", use_column_width=True)

    # Predict age and gender
    age, gender = predict_age_gender(image)

    # Display the results
    st.write(f"Detected Age: {age} years")
    st.write(f"Detected Gender: {gender}")


