import speech_recognition as sr
import moviepy.editor as mp
clip = mp.VideoFileClip(r"1. Valuable Resources.mp4") #this is the input video file in the path
clip.audio.write_audiofile(r"audio.wav") #this is the generating audio file.
r = sr.Recognizer()
audio = sr.AudioFile("audio.wav")
with audio as source:
    audio_file = r.record(source)
result = r.recognize_google(audio_file)
print(result)
with open('recog.txt', mode='w') as file:
    file.write(result)