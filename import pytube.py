from pytube import YouTube
import os
 
# download a file with only audio, to save space
# if the final goal is to convert to mp3
youtube_link = 'https://www.youtube.com/watch?v=YNP9fXZj32g'
y = YouTube(youtube_link)
t = y.streams.filter(only_audio=True).all()
t[0].download(output_path='C:\Temp\Video')