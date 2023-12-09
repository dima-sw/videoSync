# ui.py
import tkinter as tk
from tkinter import filedialog
from tkinter.ttk import Progressbar

class UserInterface:
    def __init__(self, root, select_video_folder, select_audio_folder, add_audio):
        self.root = root
        self.root.title("Video Audio Merger")
        self.video_folder_path = tk.StringVar()
        self.audio_folder_path = tk.StringVar()

        self.video_folder_label = tk.Label(root, text="Folder with videos containing audio: ")
        self.video_folder_label.pack()

        self.video_button = tk.Button(root, text="Select Video Folder", command=select_video_folder)
        self.video_button.pack()

        self.audio_folder_label = tk.Label(root, text="Folder with videos without audio: ")
        self.audio_folder_label.pack()

        self.audio_button = tk.Button(root, text="Select Audio Folder", command=select_audio_folder)
        self.audio_button.pack()

        self.progress_var = tk.DoubleVar()
        self.progress_bar = Progressbar(root, variable=self.progress_var, maximum=100)
        self.progress_bar.pack(fill='x', padx=10, pady=10)

        self.add_audio_button = tk.Button(root, text="Add Audio to Videos", command=add_audio)
        self.add_audio_button.pack()

    def update_video_folder_label(self, text):
        self.video_folder_path.set(text)

    def update_audio_folder_label(self, text):
        self.audio_folder_path.set(text)

    def update_progress(self, value):
        self.progress_var.set(value)
        self.root.update_idletasks()

    def show_success_message(self):
        tk.messagebox.showinfo("Success", "Audio added to videos without audio!")
