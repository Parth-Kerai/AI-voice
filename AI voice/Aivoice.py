import speech_recognition as sr
import pyttsx3
import webbrowser

def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio).lower()
        print(f"Recognized: {command}")
        return command
    except sr.UnknownValueError:
        print("Sorry, I didn't catch that. Please try again.")
        return None

def execute_command(command):
    if "open youtube" in command:
        open_youtube()
    elif "search google" in command:
        open_google()
    # Add more commands here

def open_youtube():
    webbrowser.open("https://www.youtube.com")

def open_google():
    webbrowser.open("https://www.google.com")

if __name__ == "__main__":
    while True:
        user_command = recognize_speech()
        if user_command:
            execute_command(user_command)
