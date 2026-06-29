import streamlit as st
import requests
import re
import phonenumbers

st.title('Basketball Camp Regitser From')

name_field = st.text_input("Please enter the full name of the athlete:")
if name_field:
    field_len = len(name_field)
    if field_len < 2 or field_len > 10:
        st.error("Name is too short or too long - min 2 and max 10 characters")

last_name_field = st.text_input("Please enter your last name:")
if last_name_field:
    last_name_len = len(last_name_field)
    if last_name_len < 2 or last_name_len > 10:
        st.error("Last name is too short or too long - min 2 and max 10 characters")


email_field = st.text_input("Please enter your email address:")
if email_field:
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(email_pattern, email_field):
        st.error("Invalid email address - must be in the format name@domain.com")
    else:
        st.success("Email is valid")

col1, col2 = st.columns([1, 3])

with col1:
    phone_country_code = st.selectbox("Code", ['+1 🇺🇸', '+44 🇬🇧', '+91 🇮🇳', '+972 🇮🇱'], index=3)

with col2:
    phone_number_field = st.text_input("Phone number")

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