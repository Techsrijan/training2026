import speech_recognition as sr

# Initialize the recognizer
voice = sr.Recognizer()

with sr.Microphone() as source:
    # Adjust for background noise to improve recognition accuracy
    print("Adjusting for ambient noise, please wait...")
    voice.adjust_for_ambient_noise(source, duration=2)

    print("Boliy ab (Speak now):")
    audio = voice.listen(source)

try:
    # Use the Google Web Speech API to transcribe the audio
    text = voice.recognize_google(audio)
    print("Apne Bola (You said): " + text)

except sr.UnknownValueError:
    print("Your voice is not clear (Could not understand the audio)")
except sr.RequestError as e:
    print(f"Could not request results from the Google Speech Recognition service; {e}")
except Exception as e:
    print(f"An error occurred: {e}")
