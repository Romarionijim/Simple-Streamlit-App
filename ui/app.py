import streamlit as st
import requests
import re
import phonenumbers

st.title('Basketball Camp Regitser From')

def check_char_length(char: str):
    if len(char) < 2 or len(char) > 10:
        st.error("Name is too short or too long - min 2 and max 10 characters")

name_field = st.text_input("First name:")
if name_field:
    check_char_length(name_field)

last_name_field = st.text_input("Last name:")
if last_name_field:
    check_char_length(last_name_field)

email_field = st.text_input("Email address:")
if email_field:
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(email_pattern, email_field):
        st.error("Invalid email address - must be in the format name@domain.com")
    else:
        st.success("Email is valid")

player_age = st.number_input("Age:", min_value=18, max_value=45, value=18)

current_team = st.text_input("Type your current league team:", placeholder="Hapoel Nazareth Orthodox")

col1, col2 = st.columns([1, 3])

with col1:
    phone_country_code = st.selectbox("Country Code", ['+1 🇺🇸', '+44 🇬🇧', '+91 🇮🇳', '+972 🇮🇱'], index=3)

with col2:
    phone_number_field = st.text_input("Phone number")

phone_number = None
if phone_number_field:
    code = phone_country_code.split()[0]
    phone_number = code + phone_number_field
    try:
        parsed_number = phonenumbers.parse(phone_number)
        if phonenumbers.is_valid_number(parsed_number):
            st.success("Phone number is valid")
        else:
            st.error("Invalid phone number for the selected country code")
    except phonenumbers.NumberParseException:
        st.error("Could not parse phone number - digits only, no spaces or dashes")

submit_button = st.button("Submit")

if submit_button:
    payload = {
        "first_name": name_field,
        "last_name": last_name_field,
        "email": email_field,
        "age": player_age,
        "current_team": current_team,
        "phone_number": phone_number
    }

    response = requests.post("http://localhost:3030/register", json=payload)
    if response.status_code == 200:
        st.success("Registration successful")
    else:
        st.error("Registration failed")
