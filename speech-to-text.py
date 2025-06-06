import speech_recognition as sr


r = sr.Recognizer()

def record_text():
    while True:
        try:
           

            with sr.Microphone() as source2:
                print("\nAdjusting for background noise... Please wait.")
                r.adjust_for_ambient_noise(source2, duration=1)
                print("Listening... Speak clearly.")

                audio2 = r.listen(source2)
                print("Recognizing...")

            
                MyText = r.recognize_google(audio2)
                print("You said:", MyText)

                return MyText

        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition; {0}".format(e))
        except sr.UnknownValueError:
            print("Speech Recognition could not understand audio. Please try again.")


def output_text(text):
    with open("output.txt", "a", encoding="utf-8") as f:
        f.write(text)
        f.write("\n")
    print("Saved to output.txt\n")


if __name__ == "__main__":
    print("Voice-to-Text Logger Started. Say 'stop recording' to end.\n")

    while True:
        text = record_text()

        if text.lower() == "stop recording":
            print("Stopping the program as per your request.")
            break

        output_text(text)
