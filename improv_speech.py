import streamlit as st
import speech_recognition as sr

def transcribe_speech(api_choice, language):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("Speak now...")
        try:
            audio_text = r.listen(source, timeout=5, phrase_time_limit=10)
        except sr.WaitTimeoutError:
            return "No speech detected. Please try again."

        st.info("Transcribing...")

        try:
            if api_choice == "Google":
                text = r.recognize_google(audio_text, language=language)
            elif api_choice == "Sphinx":
                text = r.recognize_sphinx(audio_text, language=language)
            else:
                text = "Selected API not implemented."
            return text
        except sr.UnknownValueError:
            return "Sorry, could not understand the audio."
        except sr.RequestError as e:
            return f"API Request failed: {e}"
        except Exception as e:
            return f"Unexpected error: {str(e)}"

def main():
    st.title("Speech Recognition App")
    st.write("Click on the microphone to start speaking:")

    # API Selection
    api_choice = st.sidebar.selectbox("Select Speech Recognition API", ["Google", "Sphinx"])
    
    # Language Selection (BCP-47 format)
    language = st.sidebar.text_input("Language (e.g., en-US, fr-FR, hi-IN)", value="en-US")

    # Session state to store text
    if "text" not in st.session_state:
        st.session_state.text = ""

    # "Recording" simulation
    if st.button("Start Recording"):
        st.session_state.text = transcribe_speech(api_choice, language)
        st.write("Transcription:", st.session_state.text)

    # Pause/Resume simulation
    if st.button("Pause/Resume"):
        st.warning("Pause/Resume is not supported in real-time mic input with this method. Try breaking speech into parts.")

    # Download feature
    if st.session_state.text:
        st.download_button(
            label="Download Transcribed Speech",
            data=st.session_state.text,
            file_name="transcribe.txt",
            mime="text/plain"
        )

if __name__ == "__main__":
    main()
