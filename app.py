# THIS IS A SIMPLE TO DO LIST APP USING STREAMLIT = PY LIBRARY:  Why I called your app “Lisp-flavored”
# Your app is in Python + Streamlit, but the way we display tasks looks like Lisp lists:
# 
# (tasks read-the-bible practice-IT pray-today)
# (tasks "buy-milk" "finish-homework" "call-Yeshua")

#pip install streamlit
#streamlit run app.py

import streamlit as st
import gspread
import json
from google.oauth2.service_account import Credentials

st.set_page_config(page_title="Todo App", page_icon="✅", layout="centered")

st.title("📝 Streamlit Todo App")
st.write("Keep track of your daily tasks easily!")

# ---- Load Google Service Account Credentials ----
# Make sure you’ve pasted your JSON content in Streamlit → Settings → Secrets
service_account_info = json.loads(st.secrets["SERVICE_ACCOUNT"]["JSON"])
creds = Credentials.from_service_account_info(service_account_info)
gc = gspread.authorize(creds)

# ---- Connect to Google Sheet ----
# Replace with your own Google Sheet ID (from the URL)
SHEET_ID = "1baiMrjcUoH85UQFYwbPmAVcwKHxFCmj2wd-istlI4Zw"
sh = gc.open_by_key(SHEET_ID)
worksheet = sh.sheet1

# ---- Fetch Tasks from Google Sheet ----
def get_tasks():
    try:
        records = worksheet.get_all_records()
        return [r["Task"] for r in records]
    except Exception as e:
        st.error(f"Error reading tasks: {e}")
        return []

# ---- Add a New Task ----
def add_task(task):
    if task:
        worksheet.append_row([task])
        st.success("Task added successfully!")
    else:
        st.warning("Please enter a task before adding.")

# ---- Delete a Task ----
def delete_task(task_to_delete):
    tasks = get_tasks()
    try:
        index = tasks.index(task_to_delete)
        worksheet.delete_rows(index + 2)  # +2 because of header row
        st.success("Task deleted!")
    except ValueError:
        st.error("Task not found. Try refreshing.")

# ---- Streamlit UI ----
st.subheader("✅ Your Todo List")

tasks = get_tasks()
for t in tasks:
    st.write(f"🟩 {t}")

new_task = st.text_input("Add a new task:")
if st.button("Add Task"):
    add_task(new_task)

task_to_delete = st.selectbox("Select a task to delete:", [""] + tasks)
if st.button("Delete Task"):
    delete_task(task_to_delete)

st.markdown("---")
st.markdown(
    """
    💖 **Support My Work**
    
    If you enjoy this app and want to support its development,  
    you can make a small donation using the button below 👇
    """
)

if st.button("☕ Support on PayPal"):
    st.markdown(
        "[Click here to donate via PayPal 💖](https://www.paypal.com/paypalme/ChildofGod777?country.x=CH)",
        unsafe_allow_html=True,
    )

st.markdown("---")
st.caption("Built with Streamlit & Google Sheets integration 🚀")





