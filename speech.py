import streamlit as st
import speech_recognition as sr


def transcribe_speech():
    # Initialize recognizer class
    r = sr.Recognizer()
    # Reading Microphone as source
    with sr.Microphone() as source:
        st.info("Speak now...")
        # listen for speech and store in audio_text variable
        audio_text = r.listen(source)
        st.info("Transcribing...")

        try:
            # using Google Speech Recognition
            text = r.recognize_google(audio_text)
            return text
        except:
            return "Sorry, I did not get that."


def main():
    st.title("Speech Recognition App")
    st.write("Click on the microphone to start speaking:")

    # Initialize session state if it doesn't exist
    if "text" not in st.session_state:
        st.session_state.text = ""

    # add a button to trigger speech recognition
    if st.button("Start Recording"):
        text = transcribe_speech()
        st.write("Transcription: ", text)

    if st.button('Download transcribed speech'):
            label = 'Download Speech',
            data = st.session_state.text,
            file_name = 'transcribe.txt',
            mime='text/plain'
        

if __name__ == "__main__":
    main()