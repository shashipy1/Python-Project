import speech_recognition as sr
filename = "1. Valuable Resources.mp4"
# initialize the recognizer
r = sr.Recognizer()
# open the file
with sr.VideoFile("1. Valuable Resources.mp4") as E:\
    # listen for the data (load audio to memory)
    video_data = r.record()
    # recognize (convert from speech to text)
    text = r.recognize_google(video_data)
    print(text)