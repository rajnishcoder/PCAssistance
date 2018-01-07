import speech_recognition as sr

#custom classes
from AudioTracker import AudioTracker
 
# To Record Audio

r = sr.Recognizer()
audio = None
def listen():
    with sr.Microphone() as source:
        print("What Can I do for you?")
        global audio
        audio = r.listen(source)

# calling listning function
listen()

try:
    output = r.recognize_google(audio)
except sr.UnknownValueError:
    print("Sorry I did not understand! Can you say it again?")
    listen()
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))

# if output is not undefined
try:
    output
except NameError:
    print ("Oops there is an error in audio output :(")
else:    
    # send it to Audio Tracker
    AudioTracker(output)
    print(output)
  


