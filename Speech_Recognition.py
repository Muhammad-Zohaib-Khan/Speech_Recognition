import speech_recognition as s
import pyttsx3 as p

print("Welcome".center(120)) 
def Speech_To_Text():
    #Recognizer object, which will be responsible for recognizing the speech.
    sr=s.Recognizer()
    #message
    print("Hello Speak now I am listening........")
    #To record audio. We will use the Microphone class from the SpeechRecognition library
    with s.Microphone() as m:
        audio=sr.listen(m)
        #we can use the Recognizer object to recognize the speech.
        query=sr.recognize_google(audio,language="English")
        print(query)
def Text_To_Speech():
    user_input=input("Hello Enter text to recognize: ")
    # init object, which will be responsible for recognizing the text
    engine = p.init()
    #say method on the engine that passing input text to be spoken
    engine.say(user_input)
    # run and wait method, it processes the voice commands. 
    engine.runAndWait()
while True:
    print("Enter Number \n 1) Speech to text \n 2) Text to speech \n 3) Exit")
    enter_number=input("Enter Number : ")
    if enter_number=="1":
        Speech_To_Text()        
    elif enter_number=="2":
        Text_To_Speech()
    elif enter_number=="3":
        break
    else:
        print("You Must Enter Correct Number Enter Again")
