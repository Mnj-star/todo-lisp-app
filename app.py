# THIS IS A SIMPLE TO DO LIST APP USING STREAMLIT = PY LIBRARY:  Why I called your app “Lisp-flavored”
# Your app is in Python + Streamlit, but the way we display tasks looks like Lisp lists:
# 
# (tasks read-the-bible practice-IT pray-today)
# (tasks "buy-milk" "finish-homework" "call-Yeshua")

# streamlit run app.py

import streamlit as st
import yfinance as yf
import pandas as pd

st.title("📝 Lisp-flavored Todo App")

if "tasks" not in st.session_state:
    st.session_state.tasks = []

# Add task
new_task = st.text_input("Add a task (e.g., buy-milk):")

if st.button("Add") and new_task:
    st.session_state.tasks.append(new_task)

# Show tasks in Lisp-style list
if st.session_state.tasks:
    st.write("Your tasks in Lisp style:")
    st.code(f"(tasks {' '.join(st.session_state.tasks)})", language="lisp")

# Delete tasks
delete_task = st.selectbox("Select a task to delete:", [""] + st.session_state.tasks)
if st.button("Delete") and delete_task:
    st.session_state.tasks.remove(delete_task)


#pip install streamlit
#streamlit run app.py

