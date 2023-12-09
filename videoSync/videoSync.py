# logic.py
import os
from moviepy.editor import VideoFileClip

def add_audio_to_videos(video_folder_path, audio_folder_path, update_progress):
    videos_without_audio = [f for f in os.listdir(video_folder_path.get()) if f.endswith('.mp4')]
    videos_with_audio = [f for f in os.listdir(audio_folder_path.get()) if f.endswith('.mp4')]

    total_videos = len(videos_without_audio)
    progress = 0
    update_progress(0)

    for video_file in videos_without_audio:
        video_without_audio_path = os.path.join(video_folder_path.get(), video_file)
        audio_file_path = os.path.join(audio_folder_path.get(), videos_with_audio[0])  # Assuming only one audio file

        video = VideoFileClip(video_without_audio_path)
        audio = VideoFileClip(audio_file_path).audio

        video = video.set_audio(audio)
        output_file = os.path.join(video_folder_path.get(), 'with_audio_' + video_file)

        video.write_videofile(output_file, codec='libx264', audio_codec='aac')
        video.close()

        progress += 1
        progress_value = int((progress / total_videos) * 100)
        update_progress(progress_value)
