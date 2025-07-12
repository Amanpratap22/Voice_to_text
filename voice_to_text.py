
import speech_recognition as sr

def recognize_speech():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("\n[INFO] Speak something...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("[INFO] Recognizing...")
        text = recognizer.recognize_google(audio)
        print("[RESULT] You said:", text)
        with open("output.txt", "w") as file:
            file.write(text)
    except sr.UnknownValueError:
        print("[ERROR] Could not understand the audio.")
    except sr.RequestError:
        print("[ERROR] API unavailable or network issue.")

if __name__ == '__main__':
    recognize_speech()
