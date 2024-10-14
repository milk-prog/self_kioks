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
    "Coffee": 3.00,
    "Tea": 2.50,
    "Sandwich": 5.00,
    "Salad": 4.50,
    "Water": 1.00
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



