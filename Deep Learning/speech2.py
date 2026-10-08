import streamlit as st
from streamlit_mic_recorder import speech_to_text
import speech_recognition as sr

# Initialize recognizer and capture audio
recognizer = sr.Recognizer()
with sr.Microphone() as source:
    print("Listening...")
    audio = recognizer.listen(source)

#text = recognizer.recognize_google(audio, language='en-US')

if recognizer:
    try:
        st.write("Transcribing...")
        text = recognizer.recognize_google(audio)
        st.write(f"You said: {text}")
    except sr.UnknownValueError:
        st.write("Sorry, I could not understand the audio.")
    except sr.RequestError as e:
        st.write(f"Could not request results; {e}")



