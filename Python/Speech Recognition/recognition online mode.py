import tkinter as tk
import speech_recognition as sr

# Initialize the recognizer
recognizer = sr.Recognizer()

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
            # Recognize and convert speech to text
            text = recognizer.recognize_google(audio_data)
            text_box.delete(1.0, tk.END)
            text_box.insert(tk.END, text)
    except sr.UnknownValueError:
        text_box.insert(tk.END, "Sorry, I could not understand the audio.")
    except sr.RequestError:
        text_box.insert(tk.END, "Sorry, there was a request error.")
    finally:
        status_label.config(text="Click 'Start Listening' to speak again")

# Setup the main Tkinter window
root = tk.Tk()
root.title("Speech to Text")
root.geometry("400x300")

# Create and place widgets
status_label = tk.Label(root, text="Click 'Start Listening' to begin", font=("Arial", 12))
status_label.pack(pady=10)

start_button = tk.Button(root, text="Start Listening", command=start_listening, font=("Arial", 12))
start_button.pack(pady=10)

text_box = tk.Text(root, wrap="word", height=10, width=40)
text_box.pack(pady=10)

# Run the Tkinter main loop
root.mainloop()
