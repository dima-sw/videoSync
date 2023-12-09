# main.py
import tkinter as tk
from tkinter import filedialog
from ui import UserInterface
from videoSync import add_audio_to_videos

def select_video_folder():
    video_folder_path = filedialog.askdirectory(title="Select folder with videos without audio")
    ui.update_video_folder_label(video_folder_path)

def select_audio_folder():
    audio_folder_path = filedialog.askdirectory(title="Select folder with videos containing audio (it will take the first one)")
    ui.update_audio_folder_label(audio_folder_path)

def add_audio():
    add_audio_to_videos(ui.video_folder_path, ui.audio_folder_path, ui.update_progress)
    ui.show_success_message()

if __name__ == "__main__":
    root = tk.Tk()
    ui = UserInterface(root, select_video_folder, select_audio_folder, add_audio)
    root.mainloop()
