import streamlit as st

# Title
st.title("Self-Service Kiosk")

# Function to take order
def take_order():
    st.header("Place Your Order")

    # Menu items
    menu = {
        "Coffee": 5.00,
        "Tea": 3.00,
        "Sandwich": 7.00,
        "Salad": 6.00,
        "Muffin": 2.50
    }

    # Order form
    order = {}
    for item, price in menu.items():
        order[item] = st.number_input(f"{item} (${price})", 0, 10, step=1)

    # Calculate total
    total = sum(order[item] * price for item, price in menu.items())
    st.write(f"Total: ${total:.2f}")

    # Submit button
    if st.button("Submit Order"):
        st.write("Order Submitted!")
        st.write(order)
        st.write(f"Total: ${total:.2f}")

# Main application
def main():
    st.sidebar.title("Self-Service Kiosk")
    option = st.sidebar.selectbox("Select an option", ("Order", "About"))

    if option == "Order":
        take_order()
    elif option == "About":
        st.header("About This Kiosk")
        st.write("""
        This is a simple self-service kiosk application built with Streamlit.
        You can place your order using the 'Order' section and learn more about
        the application in the 'About' section.
        """)

if __name__ == "__main__":
    main()



