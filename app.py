# THIS IS A SIMPLE TO DO LIST APP USING STREAMLIT = PY LIBRARY:  Why I called your app “Lisp-flavored”
# WSL BACK TO 'ROOT' COMMANDS = START @ LINE 82
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
#THIS IS THE 1ST COMMAND YOU GET ON 'POWERSHELL' TO GET WSL BACK TO 'ROOT'

# That should drop you into your WSL instance as root.
# Now, from that root shell, set your normal username as the default user. For example, if your WSL user is mary:
# 
# ubuntu config --default-user mary
# 
# or on newer versions of WSL:
# 
# wsl -d Ubuntu config --default-user mary

# TOKEN NMR. = KEEP SECRET = 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 BUT NO MORE NEEDED, WAS THE LAST ONE NOW I HAVE SSH
# YES THIS IS MY NEW APP LINK FOR MY PHONE = https://todo-lisp-app-mnj-star.streamlit.app

#ABSOLUTELY KEEP THAT TOO: ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIPc4FyTq/AJLfgTp7SOWIFPgu74WNS6emtzgGwk1qYEg jo.clever@yahoo.de

#AND THIS ONE TOO = ED25519 key fingerprint is SHA256:+DiY3wvvV6TuJJhbpZisF/zLDA0zPMSvHdkr4UvCOqU.
#Name of the repo= https://github.com/Mnj-star/todoApp.git

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
# YES THIS IS MY NEW APP LINK FOR MY PHONE = https://todo-lisp-app-mnj-star.streamlit.app


#I inserted it on my phone on google * it works!!
# 
# Now you can open that link on your Android, laptop, or anywhere in the world 🌍.
# 
# ⚡ That’s it — no VM, no firewall, no IP addresses. Just one click and your app is live.
# 
# 👉 Do you want me to prepare the exact GitHub repo structure for you (with ready-made app.py and requirements.txt), so you can just upload and deploy?  





# Awesome choice 🙌 — let’s wire your **Lisp-style Todo app** into **Google Sheets** so tasks are saved permanently and sync across devices.
# 
# ---
# 
# # ✅ Step 1: Setup Google Cloud + Sheets
# 
# 1. Go to [Google Cloud Console](https://console.cloud.google.com/).
# 2. Create a new project (e.g., `todo-lisp-app`).
# 3. Enable **Google Sheets API** and **Google Drive API**.
# 4. Go to **APIs & Services → Credentials**.
# 
#    * Click **Create Credentials → Service account**.
#    * After creating, go into it → create a **JSON key**.
#    * Download the `.json` file (e.g., `service_account.json`).
# 5. Create a new Google Sheet (name it `TodoApp`).
# 
#    * Share it with the service account email (found in the JSON, ends with `@<project>.iam.gserviceaccount.com`).
#    * Give **Editor** access.
# 6. Copy the Google Sheet **URL** and extract the Sheet ID (long string between `/d/` and `/edit`).
# 
# ---
# 
# # ✅ Step 2: Install dependencies
# 
# Update your `requirements.txt`:
# 
# ```
# streamlit
# gspread
# oauth2client
# ```
# 
# Commit + push it so Streamlit Cloud installs them.
# 
# ---
# 
# # ✅ Step 3: Streamlit App Code (`app.py`)
# 
# Here’s a ready-to-run version:
# 
# ```python
# import streamlit as st
# import gspread
# from oauth2client.service_account import ServiceAccountCredentials
# 
# # --- Google Sheets setup ---
# SHEET_ID = "YOUR_SHEET_ID_HERE"  # replace with your sheet ID
# SHEET_NAME = "Sheet1"  # default sheet name
# 
# @st.cache_resource
# def get_gsheet_client():
#     scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
#     creds = ServiceAccountCredentials.from_json_keyfile_name("service_account.json", scope)
#     client = gspread.authorize(creds)
#     return client
# 
# def get_tasks():
#     try:
#         sheet = get_gsheet_client().open_by_key(SHEET_ID).worksheet(SHEET_NAME)
#         tasks = sheet.col_values(1)
#         return tasks
#     except Exception as e:
#         st.error(f"Error reading from Google Sheets: {e}")
#         return []
# 
# def add_task(task):
#     sheet = get_gsheet_client().open_by_key(SHEET_ID).worksheet(SHEET_NAME)
#     sheet.append_row([task])
# 
# def delete_task(task):
#     sheet = get_gsheet_client().open_by_key(SHEET_ID).worksheet(SHEET_NAME)
#     tasks = sheet.col_values(1)
#     if task in tasks:
#         index = tasks.index(task) + 1
#         sheet.delete_rows(index)
# 
# # --- Streamlit UI ---
# st.title("📝 Lisp-flavored Todo App (Google Sheets Edition)")
# 
# new_task = st.text_input("Add a task (e.g., buy-milk):")
# if st.button("Add"):
#     if new_task.strip():
#         add_task(new_task.strip())
#         st.success(f"Task '{new_task}' added!")
# 
# tasks = get_tasks()
# 
# if tasks:
#     st.subheader("Your tasks in Lisp style:")
#     st.code("(tasks " + " ".join(tasks) + ")")
# 
#     delete_choice = st.selectbox("Select a task to delete:", [""] + tasks)
#     if st.button("Delete") and delete_choice:
#         delete_task(delete_choice)
#         st.success(f"Task '{delete_choice}' deleted!")
# else:
#     st.info("No tasks yet. Add one above!")
# ```
# 
# ---
# 
# # ✅ Step 4: Deployment Setup
# 
# 1. Place `service_account.json` in your repo root.
#    ⚠️ **But don’t commit secrets to GitHub** (bad practice).
#    Instead, in **Streamlit Cloud → Secrets Manager**, paste the JSON into `[secrets]`. Example:
# 
#    ```toml
#    [gcp_service_account]
#    type = "service_account"
#    project_id = "your-project-id"
#    private_key_id = "your-key-id"
#    private_key = "-----BEGIN PRIVATE KEY-----\n..."
#    client_email = "xxxx@xxxx.iam.gserviceaccount.com"
#    client_id = "1234567890"
#    ...
#    ```
# 
# 2. Update code to load creds from `st.secrets` instead of file if deploying:
# 
#    ```python
#    creds = ServiceAccountCredentials.from_json_keyfile_dict(st.secrets["gcp_service_account"], scope)
#    ```
# 
# ---
# 
# ✨ That’s it — once deployed, your tasks will live in Google Sheets and sync across devices forever.
# 
# ---
# 
# 👉 Do you want me to adjust the code so it **always uses `st.secrets`** (no file at all), so it’s 100% ready for Streamlit Cloud?
# 



# You're almost there! You're on the Service Account details page, and the service_account.json file is downloaded from the "Keys" tab.
# 
# Here's exactly what you need to do to download it:
# 
# ✅ How to download service_account.json:
# 
# Go to the "Keys" tab in your service account settings. You're already in the right place, just click on the “Keys” section in the left-hand menu (if not already selected).
# 
# Click the “Add Key” button:
# 
# You'll see a dropdown.
# 
# Select “Create new key”.
# 
# In the pop-up, choose:
# 
# Key type: JSON
# 
# Then click “Create”
# 
# Your browser will automatically download a file named something like:
# 
# todo-lisp-app-xxxxxxxxxxxx.json
# 
# 🔒 Important:
# 
# This JSON file is your service_account.json, and it contains private credentials — keep it safe!
# 
# Do not share this file publicly.
# 
# Store it in a secure place in your project (for example, in the root directory or a secrets/ folder).



#🗂️ If you're using Python (e.g., with Google Sheets, Drive, etc.):
#
#Install Google client libraries (if not already):
#
#pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
#

#Use the JSON file to authenticate:
#
#from google.oauth2 import service_account
#from googleapiclient.discovery import build
#
#SERVICE_ACCOUNT_FILE = 'todo-lisp-app-f15e78fad8d3.json'
#SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
#
#credentials = service_account.Credentials.from_service_account_file(
#    SERVICE_ACCOUNT_FILE, scopes=SCOPES
#)
#
#service = build('sheets', 'v4', credentials=credentials)
#sheet = service.spreadsheets()
#
#
#If you're working on something specific (e.g. connecting to Google Sheets, Firebase, or Google Calendar), just tell me and I’ll give you the tailored setup instructions.
#
#What would you like to do with the service account now?


#mary-618@todo-lisp-app.iam.gserviceaccount.com

#https://docs.google.com/spreadsheets/d/1baiMrjcUoH85UQFYwbPmAVcwKHxFCmj2wd-istlI4Zw/edit?usp=sharing


# 🪄 Step-by-step:
# 
# Go to Google Sheets
# 
# Click ➕ Blank to create a new spreadsheet.
# 
# Name it TodoApp (or anything you like).
# 
# It will be a Google Sheet (.gsheet) — not a .xlsx Excel file.
# 
# You’ll see a URL like:
# 
# https://docs.google.com/spreadsheets/d/1AbCdEfGh1234567890XYZ/edit#gid=0
# 
# 
# The part between /d/ and /edit is your Sheet ID (e.g., 1AbCdEfGh1234567890XYZ).
# 
# Share it with your service account email (from your JSON key file).
# 
# Click Share (top right).
# 
# Paste the email ending with @<project>.iam.gserviceaccount.com.
# 
# Give it Editor access.
# 
# Click Done.
# 
# That’s it ✅
# No Excel files — just a regular Google Sheet created in Google Drive.
# 
# Would you like me to show how to correctly find and copy your Sheet ID from the URL?
# 
# You said:
# should i give etitor access to 'all' or 'limited'
# ChatGPT said:
# 
# Excellent question — and this part is very important ✅
# 
# You should NOT give access to “All” or “Anyone with the link.”
# Instead, you must give Editor access only to the service account email.
# 
# Here’s how to do it safely:
# 
# 🧭 Correct way to share:
# 
# In your Google Sheet, click the blue “Share” button (top right).
# 
# In the “Add people or groups” field, paste the service account email —
# it looks like this:
# 
# my-streamlit-app@myproject-123456.iam.gserviceaccount.com
# 
# 
# On the right side of that email, choose Editor (not Viewer).
# 
# Click Send or Share.
# 
# ❌ Don’t do this:
# 
# Don’t set access to “Anyone with the link”.
# 
# Don’t make it public.
# 
# Don’t share with your personal Google account (unless you also want to view it manually).
# 
# So to answer clearly:
# 
# 🟢 Give Editor access to the service account email only (limited access)


# Perfect 👍 you’re absolutely on track — and your goal is clear:
# 
# ✅ You want your Streamlit Todo App (hosted online) to be usable by anyone with the URL, even on their Android phone — no login, no setup.
# 
# Let’s go over how that works and how your sharing settings affect it 👇
# 
# 🔐 How Access Actually Works
# 
# Even though anyone can open your Streamlit app URL (on phone, tablet, desktop — anywhere),
# only your service account needs access to the Google Sheet.
# 
# Here’s the key distinction:
# 
# Who	Needs Access to Google Sheet?	Why
# 👤 You (app creator)	Optional	You can view/edit directly if you want.
# 🤖 Service Account (from JSON)	✅ Yes, Editor access	This is the “bridge” that lets the app read/write data.
# 🌍 Other users of your app	❌ No	They only use Streamlit; they never touch the sheet directly.
# 🧱 How it works technically
# 
# When someone opens your Streamlit app (on Android, iPhone, or laptop),
# the app runs on Streamlit Cloud, not on their phone.
# 
# Your app (running on Streamlit Cloud) connects to Google Sheets using the service account credentials stored in service_account.json.
# 
# So, even though anyone can access your app, they all use your service account behind the scenes to save and load tasks.
# 
# That’s what makes the sheet access “limited” but the app itself “public” ✅


# 
# 🌐 How to make your app public for anyone to use
# 
# Once you’ve deployed your app to Streamlit Cloud:
# 
# Go to https://share.streamlit.io
# .
# 
# Deploy your GitHub repo that contains:
# 
# app.py
# 
# requirements.txt
# 
# service_account.json
# 
# When it’s done, Streamlit gives you a public URL like:
# 
# https://yourusername-yourapp.streamlit.app
# 
# 
# Share this link — anyone with it can open your app (including from Android).
# 
# So the answer is:
# 
# 👉 Share the Google Sheet with only the service account (Editor access),
# and share the Streamlit app URL publicly — that’s what everyone will use.

# 
# 
# ✅ Safe Workflow Summary
# Where	What to do	Why
# 💻 Your computer (local)	Keep service_account.json in your project folder for testing.	Needed for local runs.
# ☁️ Streamlit Cloud	Upload the file privately under “Secrets → Add file.”	Safe & encrypted.
# 🌍 GitHub	❌ Do NOT upload it — instead, add it to .gitignore.	Prevents leaks.
# 🧱 How to protect it before you push
# 
# Create a file named .gitignore (if you don’t already have one), and add this line:
# 
# service_account.json
# 
# 
# Then when you run:
# 
# git add .
# git commit -m "Initial commit"
# git push origin main
# 
# On bash = git status + git rm --cached service_account.json + 
#git init
#git add .
#git commit -m "Initial commit for Streamlit Todo App"
#

# /todo-app/
# ├── app.py
# ├── requirements.txt
# ├── service_account.json     ← ignored by Git
# ├── .gitignore               ← contains: service_account.json


 
# GitHub will ignore that file completely.
# 
# ✅ Next Step
# 
# Once it’s ignored locally, you can safely:
# 
# Push your repo to GitHub (without the secret).
# 
# Deploy the repo to Streamlit Cloud.
# 
# Upload your service_account.json file inside Streamlit Cloud → Secrets → Add file.

# TOKEN NMR. = KEEP SECRET = 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 BUT NO MORE NEEDED, WAS THE LAST ONE NOW I HAVE SSH
# YES THIS IS MY NEW APP LINK FOR MY PHONE = https://todo-lisp-app-mnj-star.streamlit.app

#ABSOLUTELY KEEP THAT TOO: ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIPc4FyTq/AJLfgTp7SOWIFPgu74WNS6emtzgGwk1qYEg jo.clever@yahoo.de

#AND THIS ONE TOO = ED25519 key fingerprint is SHA256:+DiY3wvvV6TuJJhbpZisF/zLDA0zPMSvHdkr4UvCOqU.
#Name of the repo= https://github.com/Mnj-star/todoApp.git

🎉 PERFECT, Mary — that’s exactly what we wanted to see!

✅ Your SSH key works (Hi Mnj-star! …)
✅ Your repo remote is correctly linked via SSH (git@github.com:Mnj-star/todoapp-kiwy.git)
✅ That means no more tokens, passwords, or login prompts ever again inside WSL 🎯

Now let’s finish by actually pushing your local code to GitHub 👇

🚀 Final Step — Push your app code

Run these:

git add .
git commit -m "Initial commit for Streamlit Todo App"
git push -u origin main


✅ This will upload your whole project to GitHub securely via SSH.
You’ll see output showing your files being transferred.


# 
# 
# 🧩 Step-by-step SSH setup (copy & paste each line)
# 1️⃣ Create a new SSH key
# ssh-keygen -t ed25519 -C "jo.clever@yahoo.de"
# 
# 
# 🔸 Replace "your_email@example.com" with the email you use for GitHub.
# When it asks:
# 
# File to save the key → just press Enter
# 
# Passphrase → press Enter twice (no password needed)
# 

# 2️⃣ Start the SSH agent
# eval "$(ssh-agent -s)"
# 
# 3️⃣ Add your key to the agent
# ssh-add ~/.ssh/id_ed25519
# 
# 4️⃣ Copy your public key
# cat ~/.ssh/id_ed25519.pub
# 
# 
# It’ll print something like:
# 
# ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAA... your_email@example.com
# 
# 5️⃣ Add it to GitHub
# 
# Go to GitHub → Settings → SSH and GPG keys
# 👉 https://github.com/settings/keys
# 
# Click New SSH key
# 
# Title it something like WSL Key
# 
# Paste the key from step 4
# 
# Click Add SSH key
# 
# 6️⃣ Link your local project to your new repo
# 
# In WSL, navigate to your project folder:
# 
# cd "/mnt/c/Users/jcih/Desktop/DS = DataScience2024NoPmtReq-25/KiwyAppOnVsc25"
# 
# 
# Then connect it to your new GitHub repo (replace the URL with your new one):
# 
# git remote set-url origin git@github.com:Mnj-star/todoapp-kiwy.git
# 
# 
# Verify:
# 
# git remote -v
# 
# 
# It should show:
# 
# origin  git@github.com:Mnj-star/todoapp-kiwy.git (fetch)
# origin  git@github.com:Mnj-star/todoapp-kiwy.git (push)
# 
# 7️⃣ Push without passwords 🎉
# git push -u origin main
# 
# 
# ✅ No username, no password, no token — you’re free forever.
# 