import speech_recognition as sr
voice=sr.Recognizer()
with sr.Microphone() as source:
    print("Boliy ab")
    audio=voice.listen(source)
try:
    text = voice.recognize_google(audio)
    print("Appne Bola=", text)
except:
   print("Your voice is not clear")

