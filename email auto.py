# ==========================================
# PROFESSIONAL AUTO EMAIL SENDER IN PYTHON
# ==========================================
# Features:
# ✔ GUI Interface
# ✔ Send Single or Bulk Emails
# ✔ HTML Email Support
# ✔ Attachment Support
# ✔ Secure Gmail App Password Login
# ✔ Email Logging
# ✔ Modern Professional Design
# ✔ Error Handling
# ✔ Multi-threading (GUI Freeze Fix)
#
# Required:
# pip install customtkinter
#
# Gmail Setup:
# 1. Enable 2-Step Verification
# 2. Generate App Password
# 3. Use App Password instead of Gmail password
#
# ==========================================

import smtplib
import ssl
import threading
from email.message import EmailMessage
from tkinter import filedialog, messagebox
import customtkinter as ctk
import os
from datetime import datetime

# ---------------- APP SETTINGS ---------------- #

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# ---------------- MAIN WINDOW ---------------- #

app = ctk.CTk()
app.title("Professional Auto Email Sender")
app.geometry("900x700")

attachment_path = None

# ---------------- FUNCTIONS ---------------- #

def browse_file():
    global attachment_path
    attachment_path = filedialog.askopenfilename()
    if attachment_path:
        attachment_label.configure(
            text=f"Attached: {os.path.basename(attachment_path)}"
        )

def log_message(text):
    log_box.insert("end", f"{datetime.now().strftime('%H:%M:%S')} - {text}\n")
    log_box.see("end")

def send_emails():
    threading.Thread(target=send_email_thread).start()

def send_email_thread():
    sender_email = sender_entry.get()
    password = password_entry.get()
    subject = subject_entry.get()
    recipients = recipients_text.get("1.0", "end").strip().split("\n")
    body = body_text.get("1.0", "end")

    if not sender_email or not password:
        messagebox.showerror("Error", "Enter email and password")
        return

    context = ssl.create_default_context()

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls(context=context)
        server.login(sender_email, password)

        success = 0
        failed = 0

        for recipient in recipients:

            recipient = recipient.strip()

            if not recipient:
                continue

            try:
                msg = EmailMessage()
                msg["From"] = sender_email
                msg["To"] = recipient
                msg["Subject"] = subject

                # HTML EMAIL
                msg.add_alternative(f"""
                <html>
                    <body>
                        <h2 style='color:#4A90E2;'>Hello!</h2>
                        <p>{body}</p>
                        <br>
                        <p style='color:gray;'>
                        Sent using Professional Python Email Sender
                        </p>
                    </body>
                </html>
                """, subtype='html')

                # ATTACHMENT
                if attachment_path:
                    with open(attachment_path, "rb") as f:
                        file_data = f.read()
                        file_name = os.path.basename(attachment_path)

                    msg.add_attachment(
                        file_data,
                        maintype="application",
                        subtype="octet-stream",
                        filename=file_name
                    )

                server.send_message(msg)

                success += 1
                log_message(f"SUCCESS -> {recipient}")

            except Exception as e:
                failed += 1
                log_message(f"FAILED -> {recipient} | {e}")

        server.quit()

        messagebox.showinfo(
            "Completed",
            f"Emails Sent Successfully: {success}\nFailed: {failed}"
        )

    except Exception as e:
        messagebox.showerror("Login Error", str(e))

# ---------------- UI ---------------- #

title = ctk.CTkLabel(
    app,
    text="Professional Auto Email Sender",
    font=("Arial", 28, "bold")
)
title.pack(pady=20)

frame = ctk.CTkFrame(app)
frame.pack(fill="both", expand=True, padx=20, pady=10)

# Sender Email
ctk.CTkLabel(frame, text="Sender Gmail").pack(anchor="w", padx=20, pady=(20,5))
sender_entry = ctk.CTkEntry(frame, width=700, height=40)
sender_entry.pack(padx=20)

# Password
ctk.CTkLabel(frame, text="Gmail App Password").pack(anchor="w", padx=20, pady=(15,5))
password_entry = ctk.CTkEntry(frame, width=700, height=40, show="*")
password_entry.pack(padx=20)

# Subject
ctk.CTkLabel(frame, text="Subject").pack(anchor="w", padx=20, pady=(15,5))
subject_entry = ctk.CTkEntry(frame, width=700, height=40)
subject_entry.pack(padx=20)

# Recipients
ctk.CTkLabel(
    frame,
    text="Recipients (One Email Per Line)"
).pack(anchor="w", padx=20, pady=(15,5))

recipients_text = ctk.CTkTextbox(frame, width=700, height=120)
recipients_text.pack(padx=20)

# Email Body
ctk.CTkLabel(frame, text="Email Message").pack(anchor="w", padx=20, pady=(15,5))

body_text = ctk.CTkTextbox(frame, width=700, height=180)
body_text.pack(padx=20)

# Attachment
attachment_btn = ctk.CTkButton(
    frame,
    text="Attach File",
    command=browse_file
)
attachment_btn.pack(pady=10)

attachment_label = ctk.CTkLabel(frame, text="No file attached")
attachment_label.pack()

# Send Button
send_btn = ctk.CTkButton(
    frame,
    text="Send Emails",
    height=45,
    font=("Arial", 18, "bold"),
    command=send_emails
)
send_btn.pack(pady=20)

# Logs
ctk.CTkLabel(frame, text="Live Logs").pack(anchor="w", padx=20)

log_box = ctk.CTkTextbox(frame, width=700, height=120)
log_box.pack(padx=20, pady=(5,20))

# ---------------- RUN ---------------- #

app.mainloop()