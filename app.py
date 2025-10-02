# THIS IS A SIMPLE TO DO LIST APP USING STREAMLIT = PY LIBRARY:  Why I called your app “Lisp-flavored”
# 
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

#streamlit run "c:\Users\jcih\Desktop\DS = DataScience2024NoPmtReq-25\KiwyAppOnVsc25\app.py"
#streamlit --version

#VM = Virtual Machine

 #3sudo apt update && sudo apt upgrade -y


#sudo apt install python3 python3-pip -y

#pip3 install streamlit

#mkdir todo-lisp-app && cd todo-lisp-app
#nano app.py
#streamlit run app.py --server.port 8501 --server.address 0.0.0.0


# Run the app
# streamlit run app.py --server.port 8501 --server.address 0.0.0.0
# 
# 
# --server.address 0.0.0.0 makes it listen on all IPs (so you can connect from outside).
# 
# --server.port 8501 is the default port.
# 
# 7. Open firewall (if cloud VM)
# 
# If using AWS EC2/GCP/Azure:
# 
# Go to firewall/security settings.
# 
# Open port 8501 (TCP).

#http://<VM_PUBLIC_IP>:8501
 


#     ✅ How to reset WSL default user properly
# 
# Open PowerShell or Command Prompt in Windows (not inside WSL, not inside VS Code).
# 
# Run this (replace Ubuntu with your distro name if different, check with wsl --list):
# 
# wsl -d Ubuntu -u root


# That should drop you into your WSL instance as root.
# 
# Now, from that root shell, set your normal username as the default user. For example, if your WSL user is mary:
# 
# ubuntu config --default-user mary
# 
# 
# or on newer versions of WSL:
# 
# wsl -d Ubuntu config --default-user mary


# No < > — just the actual username.
# 
# 🛠 If you don’t remember your WSL username
# 
# From the root shell, list users:
# 
# ls /home

# You’ll see directories for each WSL user. That’s your original username.
# 
# 🛠 If ubuntu config doesn’t exist
# 
# On WSL 2, the ubuntu.exe command lives on Windows side. Try this in PowerShell:
# 
# ubuntu.exe config --default-user mary
# 
# 🕵️ About the devcontainers user
# 
# That’s just the account created when VS Code spun up a Dev Container. It’s not a hacker.
# You don’t need to passwd or userdel it — just switch your WSL instance back to your real user.




# Now that you’ve got your Ubuntu environment clean again, you should be able to set up the Streamlit Todo app smoothly:
# Update and install dependencies:

# sudo apt update && sudo apt upgrade -y
# sudo apt install python3 python3-pip -y
# 
# 
# Install Streamlit:
# 
# pip3 install streamlit
# 
# 
# Create your app.py file with the Todo app code.
# 
# Run it:
# 
# streamlit run app.py --server.port 8501 --server.address 0.0.0.0
# 
# 
# Then in your browser on Windows, open:
# 
# http://localhost:8501   #THIS ONE IS TO ENTER INSIDE THE BROWSER URL SPACE ADR. AND IT WORKS PERFECT


#  oh what if i want to see the toDo app with streamlit on my android/smartphone
#  ChatGPT said:
#  
#  Nice thought 💡 — yes, you can see your Streamlit app from your Android phone!
#  
#  Right now your app runs in WSL on your PC, which only opens http://localhost:8501 on your machine. 
#To see it on your phone, you need to make   it reachable on your local network (Wi-Fi).
#  
#  📱 How to view your Streamlit app on Android
#  1. Get your Windows (host) IP address
#  
#  In PowerShell (on Windows, not WSL):
#  
#  ipconfig
#  
#  
#  Look for your Wi-Fi adapter’s IPv4 Address, e.g. 192.168.1.42.
 # THIS IS IT!!! = IPv4 Address. . . . . . . . . . . : 192.168.16.1
#  
#  2. Run Streamlit in WSL to listen on all addresses
#  
#  In your WSL terminal, run:
#  
#  streamlit run app.py --server.address 0.0.0.0 --server.port 8501
#  
#  3. Open the app on your phone
#  
#  On your Android device (connected to the same Wi-Fi), open Chrome and go to:
#  
#  http://192.168.1.42:8501
#  
#  
#  (replace 192.168.1.42 with the IP you found in step 1).
#  
#  ✅ Now your phone will load the same Streamlit Todo app that’s running on your PC.
#  
# Notes:
#  
#  Both your PC and Android must be on the same Wi-Fi.
#  
#  If Windows Firewall blocks it, you may need to allow Python/WSL through on port 8501.
#  
#  If you want to share it outside your home network, we’d use something like ngrok
#   or deploy it to Streamlit Cloud.




# Perfect choice 🙌 — Streamlit Cloud will save you the whole IP/firewall hassle, and you’ll get a public link you can open on your Android (or share with anyone).
# 
# Here’s the step-by-step:
# 
# 🌐 Deploy your Todo app to Streamlit Cloud
# 1. Push your app to GitHub
# 
# Create a free GitHub account if you don’t already have one.
# 
# Make a new repository, e.g. todo-lisp-app.
# 
# Inside your repo, put:
# 
# app.py → your Streamlit Todo code
# 
# requirements.txt → listing your Python dependencies
# 
# Example requirements.txt:
# 
# streamlit
# 
# 
# Push both files to GitHub.
# 
# 2. Go to Streamlit Cloud
# 
# Visit 👉 https://streamlit.io/cloud
# 
# Sign in with GitHub.
# 
# 3. Deploy your app
# 
# Click “New app”.
# 
# Select your GitHub repo.
# 
# Pick the branch (e.g., main) and enter the file name: app.py.
# 
# Click Deploy.
# 
# 4. Get your link
# 
# Streamlit Cloud will build your app and give you a public URL like:
# 
# https://your-username-todo-lisp-app.streamlit.app
# 
# 
# Now you can open that link on your Android, laptop, or anywhere in the world 🌍.
# 
# ⚡ That’s it — no VM, no firewall, no IP addresses. Just one click and your app is live.
# 
# 👉 Do you want me to prepare the exact GitHub repo structure for you (with ready-made app.py and requirements.txt), so you can just upload and deploy?