## pre-recorded
# import speech_recognition as sr
from pathlib import Path

# Initialize recognizer
r = sr.Recognizer()


# Load audio file
base = Path.cwd().joinpath("TriageAI", "app", "audio")
test = str(base / 'test.wav')
with sr.AudioFile(test) as source:
    audio = r.record(source)  # Read the entire audio file

# Use offline Sphinx for speech recognition
try:
    text = r.recognize_sphinx(audio)
    print("Recognized text:", text)
except sr.UnknownValueError:
    print("Sphinx could not understand the audio")
except sr.RequestError:
    print("Sphinx request failed")


## real-time
# import speech_recognition as sr

# # Initialize the recognizer
# recognizer = sr.Recognizer()

# # Use the default microphone as the audio source
# with sr.Microphone() as source:
#     print("🎤 Speak now... (Ctrl+C to exit)")

#     # Adjust for ambient noise
#     recognizer.adjust_for_ambient_noise(source)

#     while True:
#         try:
#             # Capture audio
#             print("Listening...")
#             audio = recognizer.listen(source)

#             # Recognize speech using PocketSphinx (offline)
#             text = recognizer.recognize_sphinx(audio)
#             print(f"You said: {text}")

#         except sr.UnknownValueError:
#             print("Sorry, I couldn't understand that.")
#         except sr.RequestError as e:
#             print(f"Speech Recognition request failed: {e}")
#         except KeyboardInterrupt:
#             print("\nExiting...")
#             break
