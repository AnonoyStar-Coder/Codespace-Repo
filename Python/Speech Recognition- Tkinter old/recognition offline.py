import tkinter as tk
import vosk
import wave
import sounddevice as sd
import json

# Load the Vosk model
model = vosk.Model("path/to/your/vosk-model-directory")

def start_listening():
    # Update the status label to indicate listening
    status_label.config(text="Listening...")
    root.update()

    # Define callback to save audio data to buffer
    def callback(indata, frames, time, status):
        wf.writeframes(indata)

    # Record audio and save to file
    with wave.open("temp_audio.wav", "wb") as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(16000)
        with sd.InputStream(samplerate=16000, channels=1, callback=callback):
            sd.sleep(5000)  # Record for 5 seconds (adjust as needed)

    # Perform recognition
    with wave.open("temp_audio.wav", "rb") as wf:
        rec = vosk.KaldiRecognizer(model, wf.getframerate())
        while True:
            data = wf.readframes(4000)
            if len(data) == 0:
                break
            if rec.AcceptWaveform(data):
                result = json.loads(rec.Result())
                text_box.delete(1.0, tk.END)
                text_box.insert(tk.END, result["text"])
        final_result = json.loads(rec.FinalResult())
        text_box.insert(tk.END, final_result["text"])

    status_label.config(text="Click 'Start Listening' to speak again")

# Setup the main Tkinter window
root = tk.Tk()
root.title("Speech to Text with Vosk")
root.geometry("400x300")

status_label = tk.Label(root, text="Click 'Start Listening' to begin", font=("Arial", 12))
status_label.pack(pady=10)

start_button = tk.Button(root, text="Start Listening", command=start_listening, font=("Arial", 12))
start_button.pack(pady=10)

text_box = tk.Text(root, wrap="word", height=10, width=40)
text_box.pack(pady=10)

root.mainloop()
