import streamlit as st

# Function to simulate AI response
def get_ai_response(user_input):
    # Replace this with actual AI response logic or API call
    return f"AI: You said '{user_input}'"

# Set up the Streamlit app
st.title("Self-Service Kiosk")
st.write("Welcome to the self-service kiosk! Ask me anything.")

# Create a chat history list in session state
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# Input field for user messages
user_input = st.text_input("Type your message:", "")

# On submit, get AI response and update chat history
if st.button("Send"):
    if user_input:
        ai_response = get_ai_response(user_input)
        st.session_state.chat_history.append({"user": user_input, "ai": ai_response})

# Display chat history
st.sidebar.header("Chat History")
for chat in st.session_state.chat_history:
    st.sidebar.write(f"You: {chat['user']}")
    st.sidebar.write(f"{chat['ai']}")

# Optional: Clear chat history button
if st.sidebar.button("Clear Chat History"):
    st.session_state.chat_history.clear()
    st.sidebar.write("Chat history cleared.")

