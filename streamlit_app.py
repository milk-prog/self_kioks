import streamlit as st
import cv2
import numpy as np

# Meal recommendations based on simple criteria
def recommend_meal():
    meals = [
        "Cheeseburger",
        "Veggie Burger",
        "Chicken Nuggets",
        "Fries",
        "Salad",
        "Soda",
        "Milkshake",
    ]
    return np.random.choice(meals)

# Streamlit interface
st.title("Self Kiosk: Meal Recommendation")

st.write("This kiosk will recommend a meal for you!")

# Webcam input
if st.button("Start Camera"):
    # Initialize webcam
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            st.write("Error: Could not read frame.")
            break

        # Display the frame
        st.image(frame, channels='BGR', use_column_width=True)

        # Simple human detection based on frame brightness
        if np.mean(frame) > 100:  # Simple threshold; adjust as necessary
            st.write("Human detected! Recommending a meal...")
            meal = recommend_meal()
            st.write(f"Recommended Meal: {meal}")
            break

    cap.release()
else:
    st.write("Click the button to start the camera.")





