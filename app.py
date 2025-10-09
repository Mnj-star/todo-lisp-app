# THIS IS A SIMPLE TO DO LIST APP USING STREAMLIT = PY LIBRARY:  Why I called your app “Lisp-flavored”
# Your app is in Python + Streamlit, but the way we display tasks looks like Lisp lists:
# 
# (tasks read-the-bible practice-IT pray-today)
# (tasks "buy-milk" "finish-homework" "call-Yeshua")

# streamlit run app.py
# app.py

# app.py

import json
import gspread
from google.oauth2.service_account import Credentials
import streamlit as st

# -------------------------
# Google Sheets Setup
# -------------------------
# Load service account info from Streamlit secrets
service_account_info = json.loads(st.secrets["SERVICE_ACCOUNT"]["JSON"])
creds = Credentials.from_service_account_info(service_account_info)
gc = gspread.authorize(creds)

# Your Google Sheet ID
SHEET_ID = "1baiMrjcUoH85UQFYwbPmAVcwKHxFCmj2wd-istlI4Zw"
sh = gc.open_by_key(SHEET_ID)
worksheet = sh.sheet1

# -------------------------
# Streamlit App
# -------------------------
st.set_page_config(page_title="Todo Lisp App", page_icon="✅", layout="centered")

st.title("✅ Todo Lisp App")
st.write("Keep track of your daily tasks easily!")

# -------------------------
# Task Input
# -------------------------
task = st.text_input("Enter a new task:")

if st.button("Add Task"):
    if task.strip() != "":
        worksheet.append_row([task])
        st.success(f"Task added: {task}")
    else:
        st.error("Please enter a valid task.")

# -------------------------
# Display Tasks
# -------------------------
st.subheader("Your Tasks")
tasks = worksheet.get_all_values()
if tasks:
    for i, t in enumerate(tasks, 1):
        st.write(f"{i}. {t[0]}")
else:
    st.write("No tasks yet!")

# -------------------------
# PayPal Donation Section
# -------------------------
st.markdown("---")
st.header("Support This App 🙏")
st.write("If you like this app, consider making a small donation:")

paypal_url = "https://www.paypal.com/paypalme/ChildofGod777?country.x=CH/10"
st.markdown(f"[💖 Donate $1 via PayPal]({paypal_url})", unsafe_allow_html=True)
