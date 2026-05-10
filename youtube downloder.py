import yt_dlp
import customtkinter as ctk
from tkinter import filedialog, messagebox
import threading

# ---------------- UI SETUP ---------------- #
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("YouTube Downloader PRO")
app.geometry("600x420")

# ---------------- FUNCTIONS ---------------- #

def progress_hook(d):
    if d['status'] == 'downloading':
        percent = d.get('_percent_str', '0%').strip()
        progress_label.configure(text=f"Downloading... {percent}")

    elif d['status'] == 'finished':
        progress_label.configure(text="Download Completed ✔")

def download_video():
    url = url_entry.get()
    quality = quality_option.get()

    if not url:
        messagebox.showerror("Error", "Please enter a URL")
        return

    # Ask folder every time
    save_path = filedialog.askdirectory(title="Select Download Folder")

    if not save_path:
        messagebox.showwarning("Cancelled", "No folder selected")
        return

    format_map = {
        "Best": "best",
        "720p": "best[height<=720]",
        "480p": "best[height<=480]",
        "360p": "best[height<=360]"
    }

    ydl_opts = {
        "format": format_map[quality],
        "outtmpl": f"{save_path}/%(title)s.%(ext)s",
        "progress_hooks": [progress_hook]
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
    except Exception as e:
        messagebox.showerror("Error", str(e))

def start_download():
    threading.Thread(target=download_video).start()

# ---------------- UI DESIGN ---------------- #

title = ctk.CTkLabel(app, text="YouTube Downloader PRO", font=("Arial", 22, "bold"))
title.pack(pady=15)

url_entry = ctk.CTkEntry(app, width=500, placeholder_text="Enter YouTube Video URL")
url_entry.pack(pady=10)

quality_option = ctk.CTkComboBox(app, values=["Best", "720p", "480p", "360p"])
quality_option.set("Best")
quality_option.pack(pady=10)

download_btn = ctk.CTkButton(app, text="Download Video", command=start_download, height=40)
download_btn.pack(pady=20)

progress_label = ctk.CTkLabel(app, text="")
progress_label.pack(pady=10)

app.mainloop()