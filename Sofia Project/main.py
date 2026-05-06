import speech_recognition as sr
import pyttsx3
import webbrowser
import time
import musicLibrary

# ---------------------------
# INITIALIZATION
# ---------------------------

r = sr.Recognizer()





# ---------------------------
# TEXT TO SPEECH
# ---------------------------

def speak(text):

    print("Speaking:", text)

    try:
        temp_engine = pyttsx3.init('sapi5')

        voices = temp_engine.getProperty('voices')

        temp_engine.setProperty('voice', voices[0].id)
        temp_engine.setProperty('rate', 170)

        temp_engine.say(text)

        temp_engine.runAndWait()

        temp_engine.stop()

    except Exception as e:
        print("TTS Error:", e)


# ---------------------------
# COMMAND PROCESSING
# ---------------------------

def processCommand(command):

    command = command.lower()

    print("Command:", command)

    if "open google" in command:
        speak("Opening Google")
        webbrowser.open("https://google.com")

    elif "open youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://youtube.com")

    elif "open linkedin" in command:
        speak("Opening LinkedIn")
        webbrowser.open("https://linkedin.com")

    elif "open whatsapp" in command:
        speak("Opening WhatsApp")
        webbrowser.open("https://whatsapp.com")

    elif command.startswith("play"):

        try:
            song = command.split(" ", 1)[1]

            if song in musicLibrary.music:

                link = musicLibrary.music[song]

                speak(f"Playing {song}")

                webbrowser.open(link)

            else:
                speak("Song not found in library")

        except Exception as e:
            print(e)
            speak("Could not play the song")

    else:
        speak("Command not recognized")


# ---------------------------
# MAIN PROGRAM
# ---------------------------

if __name__ == "__main__":

    speak("Initializing Sofia")

    while True:

        try:

            print("\nListening for wake word...")

            # ---------------------------
            # LISTEN FOR WAKE WORD
            # ---------------------------

            with sr.Microphone() as source:

                r.adjust_for_ambient_noise(source, duration=1)

                audio = r.listen(
                    source,
                    timeout=3,
                    phrase_time_limit=4
                )

            # ---------------------------
            # RECOGNIZE WAKE WORD
            # ---------------------------

            try:

                word = r.recognize_google(audio)
                audio = None

                print("Heard:", word)

            except sr.UnknownValueError:

                print("Could not understand audio")
                continue

            except sr.RequestError as e:

                print("Speech Recognition Error:", e)
                continue

            heard = word.lower().strip()

            # ---------------------------
            # WAKE WORD DETECTED
            # ---------------------------

            if "sofia" in heard or "sophia" in heard:

                print("Wake word detected")

                speak("Yes")

                time.sleep(0.5)

                # ---------------------------
                # LISTEN FOR COMMAND
                # ---------------------------

                with sr.Microphone() as source:

                    print("Sofia Active...")

                    r.adjust_for_ambient_noise(source, duration=0.5)

                    audio = r.listen(
                        source,
                        timeout=5,
                        phrase_time_limit=6
                    )

                # ---------------------------
                # RECOGNIZE COMMAND
                # ---------------------------

                try:

                    command = r.recognize_google(audio)
                    audio = None

                    print("Recognized Command:", command)

                    processCommand(command)

                except sr.UnknownValueError:

                    print("Could not understand command")

                    speak("Sorry, I did not understand")

                except sr.RequestError as e:

                    print("Recognition API Error:", e)

                    speak("Speech service is unavailable")

            else:

                print("Wake word not detected")

        except KeyboardInterrupt:

            print("\nExiting Sofia...")
            speak("Goodbye")
            break

        except Exception as e:

            print("Main Error:", e)