import streamlit as st

st.title("My HomeRent App")
st.subheader("Welcome to the HomeRent App! Here you can find the best rental properties in your area.")

name = st.text_input("Enter your name:")
st.write(f"Hello, {name}! Let's find your perfect rental property.")
location = st.text_input("Enter your current location:")
st.write(f"Great! We'll look for rentals in {location}.")
city = st.selectbox("Select your preferred city for rental properties:",["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"])
st.write(f"You have selected: {city}")

agree = st.checkbox("I agree to the terms and conditions.")


amount = st.slider("Select your budget range:", 5000, 15000, (5000, 15000))
st.write(f"Your budget range is: ${amount[0]} to ${amount[1]}")

if st.button("Search Rentals"):
    if not name or not location or not city:
        st.warning("Please enter your name , current and city location before searching.")
    elif amount[0] >= 10000 and amount[1] <= 15000:
        st.success("Homes are available in your selected budget range.")
    else:
        st.error("No rentals found in your budget range. Please adjust your budget and try again.")
else:
    st.info("Please enter your name, location, and budget range to search for rental properties.")
        