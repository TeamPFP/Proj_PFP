import speech_recognition as sr
import pyttsx3

badWords = set()


def fillBadWordsWithWords(file):
    f = open(file, "r")
    f1 = f.readlines()
    for i in f1:
        badWords.add(i)


def sayNotToCurse():
    engine = pyttsx3.init("espeak")
    engine.setProperty('rate', 150)
    engine.say('''D'not curse! Julian''')
    engine.runAndWait()


def main():
    r = sr.Recognizer()
    m = sr.Microphone()
    try:
        with m as source:
            r.adjust_for_ambient_noise(source)
        print("Set minimum energy threshold to {}".format(r.energy_threshold))

        while True:
            with m as source:
                audio = r.listen(source)
            try:
                # recognize speech using Google Speech Recognition
                value = r.recognize_google(audio, language="uk-UA")

                print(value)
                if value in badWords:
                    print("is recognised")
                    sayNotToCurse()
                else:
                    print("is not recognised")

            except sr.UnknownValueError:
                pass
            except sr.RequestError as e:
                print("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    fillBadWordsWithWords("погані_слова.txt")
    main()
