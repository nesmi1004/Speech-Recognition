#pip install SpeechRecognition
#pip install pyaudio

import speech_recognition as sr


def speech_recog():
    r=sr.Recognizer()
    mic=sr.Microphone()

    with mic as source:
        print("speak.......")
        r.energy_threshold=700
        r.adjust_for_ambient_noise(source,duration=1)
        audio=r.listen(source)


        try:
            text=r.recognize_google(audio)
            print("you said",text)

        except:
            print("didn't here anything. pls speak again...")  

speech_recog()