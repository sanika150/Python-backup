import speech_recognition as sr
import streamlit as st
st.title("Speech Recognition with Streamlit")


# Initialize recognizer and capture audio
recognizer = sr.Recognizer()
with sr.Microphone() as source:
    print("Listening...")
    audio = recognizer.listen(source)

if st.button("Start Recognition"):
    st.success(audio)

upload_audio = st.button("Upload Audio")
if upload_audio:
    st.success(audio)

# Transcribe using Google Speech Recognition
try:
    print("You said: " + recognizer.recognize_google(audio))
except Exception as e:
    print(e)

'''
uploaded_file = st.file_uploader(
    "Upload PDF",
    type=["pdf"]
)

if uploaded_file:
    pdf_reader = PyPDF2.PdfReader(uploaded_file)
    text = ""

    for page in pdf_reader.pages:
        text += page.extract_text()

    st.text_area("Extracted Text", text)'''
'''       
if st.button("Start Recognition"):
    st.success(audio)

upload_audio = st.button("Upload Audio")
if upload_audio:
    st.success(audio)

# Transcribe using Google Speech Recognition
try:
    print("You said: " + recognizer.recognize_google(audio))
except Exception as e:
    print(e)
///////////
st.title("Speech to Text App")

# This creates a button that records and transcribes automatically
text = speech_to_text(
    language='en', 
    start_prompt="Click to Speak", 
    stop_prompt="Stop Recording", 
    just_once=True, 
    key='STT'
)

if text:
    st.success("Transcription complete!")
    st.write(text)
'''