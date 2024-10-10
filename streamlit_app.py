import streamlit as st

# Title of the app
st.title("Self-Service Kiosk")

# Sample menu items
menu_items = {
    "Burger": 5.99,
    "Pizza": 8.99,
    "Salad": 4.99,
    "Soda": 1.50,
}

# Display menu
st.header("Menu")
for item, price in menu_items.items():
    st.write(f"{item}: ${price:.2f}")

# Order form
st.header("Place Your Order")
order = {}
for item in menu_items:
    quantity = st.number_input(f"How many {item}s?", min_value=0, max_value=10, value=0)
    order[item] = quantity

# Calculate total
total = sum(menu_items[item] * qty for item, qty in order.items())

# Submit button
if st.button("Submit Order"):
    if total > 0:
        st.success(f"Your order has been placed! Total: ${total:.2f}")
    else:
        st.warning("Please select at least one item.")

# Optionally, add a reset button
if st.button("Reset Order"):
    st.experimental_rerun()

