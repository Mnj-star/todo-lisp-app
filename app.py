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

# --- Google Sheets authentication ---
service_account_info = json.loads(st.secrets["SERVICE_ACCOUNT"]["JSON"])
creds = Credentials.from_service_account_info(service_account_info)
gc = gspread.authorize(creds)

# Replace this with your actual Sheet ID (from the URL between /d/ and /edit)
SHEET_ID = "1baiMrjcUoH85UQFYwbPmAVcwKHxFCmj2wd-istlI4Zw"
sh = gc.open_by_key(SHEET_ID)
worksheet = sh.sheet1

# --- Streamlit UI ---
st.set_page_config(page_title="Todo App", page_icon="✅")

st.title("✅ My Todo App")
st.write("Keep track of your daily tasks!")

# Display tasks from the first column
tasks = worksheet.col_values(1)
if tasks:
    st.subheader("Your Tasks:")
    for i, task in enumerate(tasks, 1):
        st.write(f"{i}. {task}")
else:
    st.write("No tasks yet! Add one below.")

# Input to add a new task
new_task = st.text_input("Add a new task:")
if st.button("Add Task") and new_task.strip():
    worksheet.append_row([new_task])
    st.success(f"Task '{new_task}' added!")
    st.experimental_rerun()  # Refresh app to show updated list

# PayPal donation section
st.markdown("---")
st.subheader("Support this app 🙏")
st.write(
    "If you like this app, consider donating $1 via PayPal. Your support helps keep it running!"
)
paypal_link = "https://www.paypal.com/paypalme/ChildofGod777?country.x=CH"
st.markdown(f"[Donate $1 via PayPal]({paypal_link})")

