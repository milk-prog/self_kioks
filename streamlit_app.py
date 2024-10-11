import streamlit as st

# Simple chatbot function
def chatbot_response(user_input):
    responses = {
        "hello": "Hi there! How can I assist you today?",
        "how are you?": "I'm just a program, but thanks for asking!",
        "what is your name?": "I'm your friendly kiosk assistant!",
        "bye": "Goodbye! Have a great day!"
    }
    return responses.get(user_input.lower(), "Sorry, I don't understand that.")

# Streamlit interface
st.title("Self Kiosk with AI Assistant")

st.header("Welcome to the Self Kiosk")
st.write("Ask me anything!")

# User input
user_input = st.text_input("You:", "")

if user_input:
    # Get the response from the chatbot
    response = chatbot_response(user_input)
    
    # Display the response
    st.write(f"Assistant: {response}")



