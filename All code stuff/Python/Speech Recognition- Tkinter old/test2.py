import tkinter as tk
import speech_recognition as sr
import pyttsx3

# Initialize the recognizer and TTS engine
recognizer = sr.Recognizer()
tts_engine = pyttsx3.init()

# Dictionary of supported languages and their Google API language codes
languages = {
    "English": "en-US",
    "Hindi": "hi-IN"
}

# List available voices and set a default
voices = tts_engine.getProperty('voices')
for index, voice in enumerate(voices):
    print(f"Voice {index}: {voice.name} - {voice.id}")

# Function to set TTS voice
def set_tts_voice(voice_index=1):
    voices = tts_engine.getProperty('voices')
    tts_engine.setProperty('voice', voices[voice_index].id)

# Set the default voice (change to 0 for an alternate voice)
set_tts_voice(voice_index=1)

def start_listening():
    # Update the status label to indicate listening
    status_label.config(text="Listening...")
    root.update()

    try:
        # Use the microphone as the source of input
        with sr.Microphone() as source:
            # Adjust for ambient noise
            recognizer.adjust_for_ambient_noise(source)
            # Listen for the user's speech
            audio_data = recognizer.listen(source)

            # Get the selected language from the dropdown
            selected_language = language_var.get()
            language_code = languages[selected_language]

            # Recognize and convert speech to text in the selected language
            text = recognizer.recognize_google(audio_data, language=language_code)
            text_box.delete(1.0, tk.END)
            text_box.insert(tk.END, text)

            # Speak out the recognized text
            speak_text(text)

    except sr.UnknownValueError:
        text_box.insert(tk.END, "Sorry, I could not understand the audio.")
    except sr.RequestError:
        text_box.insert(tk.END, "Sorry, there was a request error.")
    finally:
        status_label.config(text="Click 'Start Listening' to speak again")

def speak_text(text):
    """Function to convert text to speech using pyttsx3."""
    tts_engine.say(text)
    tts_engine.runAndWait()

# Setup the main Tkinter window
root = tk.Tk()
root.title("Speech to Text with Language Selection")
root.geometry("400x350")

# Create and place widgets
status_label = tk.Label(root, text="Click 'Start Listening' to begin", font=("Arial", 12))
status_label.pack(pady=10)

# Language selection dropdown
language_var = tk.StringVar(root)
language_var.set("English")  # Default value
language_dropdown = tk.OptionMenu(root, language_var, *languages.keys())
language_dropdown.pack(pady=10)

start_button = tk.Button(root, text="Start Listening", command=start_listening, font=("Arial", 12))
start_button.pack(pady=10)

text_box = tk.Text(root, wrap="word", height=10, width=40)
text_box.pack(pady=10)

# Run the Tkinter main loop
root.mainloop()
