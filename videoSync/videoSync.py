import os
from moviepy.editor import VideoFileClip

import tkinter as tk
from tkinter import filedialog
from tkinter.ttk import Progressbar


def select_video_folder():
    global video_folder_path
    video_folder_path = filedialog.askdirectory(title="Select folder with videos without audio")
    video_folder_label.config(text=video_folder_path)

def select_audio_folder():
    global audio_folder_path
    audio_folder_path = filedialog.askdirectory(title="Select folder with videos containing audio (it will take the first one)")
    audio_folder_label.config(text=audio_folder_path)

def add_audio():
    global video_folder_path, audio_folder_path

    videos_without_audio = [f for f in os.listdir(video_folder_path) if f.endswith('.mp4')]
    videos_with_audio = [f for f in os.listdir(audio_folder_path) if f.endswith('.mp4')]

    total_videos = len(videos_without_audio)
    progress = 0
    progress_var.set(0)

    for video_file in videos_without_audio:
        video_without_audio_path = os.path.join(video_folder_path, video_file)
        audio_file_path = os.path.join(audio_folder_path, videos_with_audio[0])  # Assuming only one audio file

        video = VideoFileClip(video_without_audio_path)
        audio = VideoFileClip(audio_file_path).audio

        video = video.set_audio(audio)
        output_file = os.path.join(video_folder_path, 'with_audio_' + video_file)

        video.write_videofile(output_file, codec='libx264', audio_codec='aac')
        video.close()

        progress += 1
        progress_value = int((progress / total_videos) * 100)
        progress_var.set(progress_value)
        root.update_idletasks()

    tk.messagebox.showinfo("Success", "Audio added to videos without audio!")

root = tk.Tk()
root.title("Video Audio Merger")

video_folder_path = ""
audio_folder_path = ""

video_folder_label = tk.Label(root, text="Folder with videos containing audio: ")
video_folder_label.pack()

video_button = tk.Button(root, text="Select Video Folder", command=select_video_folder)
video_button.pack()

audio_folder_label = tk.Label(root, text="Folder with videos without audio: ")
audio_folder_label.pack()

audio_button = tk.Button(root, text="Select Audio Folder", command=select_audio_folder)
audio_button.pack()

progress_var = tk.DoubleVar()
progress_bar = Progressbar(root, variable=progress_var, maximum=100)
progress_bar.pack(fill='x', padx=10, pady=10)

add_audio_button = tk.Button(root, text="Add Audio to Videos", command=add_audio)
add_audio_button.pack()

root.mainloop()
