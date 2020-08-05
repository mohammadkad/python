# Convert Video to Text, By : Mohammad Kadkhodaei, 1399-05-15

# 1- use ffmpeg to convert mp4 to mp3                    > ffmpeg -i 1.mp4 1.mp3
# 2- then convert mp3 to wav                             > ffmpeg -i 1.mp3 1.wav
# 3- install this library                                > pip install SpeechRecognition

import speech_recognition as sr

r = sr.Recognizer()

# open the file
with sr.AudioFile('1.wav') as source:
    # load audio to memory
    audio = r.record(source)
    # convert from speech to text
    text = r.recognize_google(audio)
    print(text)



