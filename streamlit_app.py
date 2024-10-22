import streamlit as st

# Title and instructions
st.title("Self-Service Kiosk")
st.write("Welcome! Please follow the instructions to complete your order.")

# Step 1: Input user details
st.header("Step 1: Enter your details")
name = st.text_input("Enter your name:")
email = st.text_input("Enter your email:")

# Step 2: Select items from a menu
st.header("Step 2: Select your items")
menu_items = {
    "Burger": 3.00,
    "Fries": 2.50,
    "Pizza": 5.00,
    "Milkshake": 4.50,
    "Water": 1.00,
    "Soft Drinks": 2.50,
    "Iced Tea":2.50,
    "Beyonce Meal": 3.00
}

# Multi-select box for the menu items
selected_items = st.multiselect("Select items to add to your order", list(menu_items.keys()))

# Calculate total cost
total_cost = sum(menu_items[item] for item in selected_items)

# Step 3: Display the total cost and confirmation
st.header("Step 3: Review your order")

if selected_items:
    st.write("You have selected the following items:")
    for item in selected_items:
        st.write(f"{item}: ${menu_items[item]:.2f}")
    st.write(f"**Total Cost: ${total_cost:.2f}**")

    # Order confirmation button
    if st.button("Confirm Order"):
        if name and email:
            st.success(f"Thank you for your order, {name}! Your total is ${total_cost:.2f}.")
        else:
            st.error("Please enter your name and email to proceed.")
else:
    st.write("No items selected yet.")

# Optional: Add a reset button to clear inputs
if st.button("Reset"):
    st.experimental_rerun()

# Fast food chatbot response logic
def get_bot_response(user_input):
    user_input = user_input.lower()

    if "menu" in user_input:
        return "Our menu includes burgers, fries, pizzas, drinks and beyonce meal!"
    elif "burger" in user_input:
        return "Our burgers come with cheese, lettuce, and tomato. You can add bacon or extra toppings!"
    elif "order" in user_input:
        return "You can place an order for pickup or delivery. How would you like to proceed?"
    elif "fries" in user_input:
        return "Our fries are crispy and available in regular or large sizes."
    elif "drink" in user_input:
        return "We offer soft drinks, milkshakes, and iced tea. What's your favorite?"
    elif "opening hours" in user_input:
        return "We are open from 10 AM to 10 PM, seven days a week."
    elif "beyonce meal" in user_input:
        return "beyonce meal consist of a happy meal, baby oil as the drink, pdidy as the happy meal toy."
    elif "bye" in user_input or "thank you" in user_input:
        return "Thanks for visiting! Have a great day!"
    else:
        return "I'm sorry, I didn't quite catch that. Could you ask about our menu, orders, or hours?"

# Sidebar Chatbox
st.sidebar.title("Fast Food Chatbot")
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = ""  # Initialize chat history

# Display previous conversation
chat_history = st.sidebar.text_area("Chat History", st.session_state['chat_history'], height=300)

# Input for new messages
new_message = st.sidebar.text_input("You:", "")
if st.sidebar.button("Send"):
    if new_message:
        # Add user message to chat history
        st.session_state['chat_history'] += f"\nYou: {new_message}"
        
        # Get bot response
        bot_response = get_bot_response(new_message)
        st.session_state['chat_history'] += f"\nBot: {bot_response}"
        
        # Update chat history display
        chat_history = st.sidebar.text_area("Chat History", st.session_state['chat_history'], height=300)

# Button to reset chat history
if st.sidebar.button("Reset Chat"):
    st.session_state['chat_history'] = ""  # Clear chat history




