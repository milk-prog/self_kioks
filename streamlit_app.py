import streamlit as st

# Function to get bot responses
def get_bot_response(message):
    # Placeholder for bot response logic
    return "I'm sorry, I don't have an answer for that."

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
    "Iced Tea": 2.50,
    "Beyonce Meal": 3.00
}

# Image paths for each item
menu_images = {
    "Burger": "https://www.thecookierookie.com/wp-content/uploads/2023/04/featured-stovetop-burgers-recipe.jpg",
    "Fries": "https://cdn.sanity.io/images/g1s4qnmz/production/82694af53c1e85caca322e435067067806223518-2500x2500.jpg",
    "Pizza": "https://upload.wikimedia.org/wikipedia/commons/8/8f/Neapolitan_pizza.jpg",
    "Milkshake": "https://thebigmansworld.com/wp-content/uploads/2024/06/protein-milkshake-recipe.jpg",
    "Water": "https://images.thdstatic.com/productImages/2c12c804-7728-4112-9a79-d3dbb0c33548/svn/dasani-water-049000026566-64_600.jpg",
    "Soft Drinks": "https://upload.wikimedia.org/wikipedia/commons/0/0b/Coca-Cola_Logo.svg",  # Updated to an actual drink image
    "Iced Tea": "https://upload.wikimedia.org/wikipedia/commons/e/eb/Iced_Tea.png",
    "Beyonce Meal": "https://i.abcnewsfe.com/a/b8916d79-a2f2-4e47-9de8-5591b2e91b23/beyonce-mo_1729909966498_hpMain.jpg"
}

# Multi-select box for the menu items
selected_items = st.multiselect("Select items to add to your order", list(menu_items.keys()))

# Calculate total cost
total_cost = sum(menu_items[item] for item in selected_items)

# Step 3: Display the total cost, selected items, and their images
st.header("Step 3: Review your order")

if selected_items:
    st.write("You have selected the following items:")
    for item in selected_items:
        st.write(f"{item}: ${menu_items[item]:.2f}")
        st.image(menu_images[item], width=150, caption=item)  # Display image for each selected item
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
    st.session_state.clear()  # Clear all session state variables

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





