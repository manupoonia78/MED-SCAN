# MED-SCAN
Detection Of Budding Viruses in human body

CODE :

import pyttsx3                             ////////  IMPORTING          MODULES           //////////////
import speech_recognition as sr                                        
import os                                                                               
import smtplib
import cv2
import pytesseract
import matplotlib.pyplot as plt
from PIL import Image

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)             /////   SELECTING VOICE /////////


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
     

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:                     /////////   TAKING VOICE INPUT   //////////////
        print("Listening...")
        r.pause_threshold = 1                                        //////////    MINIMUM AUDIO PITCH   /////////
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")                         ///////   PRINTING THE RECIEVED OUTPUT  ////////

    except Exception as e:                                     
        # print(e)    
        print("Say that again please...")  
        return None
    return query
c=0
pytesseract.pytesseract.tesseract_cmd="C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe"    //////  SETTING THE TESSERECT MODULE PATH  ///////
directory = "Report_images"
search=takeCommand()
for filename in os.listdir(directory):
    if filename.endswith(".png"): 
        image = cv2.imread((os.path.join(directory, filename)))
        image_copy = image.copy()
        target_word = search                                    /////////   SETTING THE TARGET WORD WHICH HAS TO BE SEARCHED  //////////
        
        data = pytesseract.image_to_data(image, output_type=pytesseract.Output.DICT)
        word_occurences = [ i for i, word in enumerate(data["text"]) if word.lower()==target_word]
        text = pytesseract.image_to_string(image)
        if search in text.lower():
            for occ in word_occurences:
                w = data["width"][occ]                      /////   SETTING THE PARAMETERS FOR SEARCHING ///////// 
                h = data["height"][occ]
                l = data["left"][occ]
                t = data["top"][occ]
                p1 = (l, t)
                p2 = (l + w, t)
                p3 = (l + w, t + h)
                p4 = (l, t + h)
                image_copy = cv2.line(image_copy, p1, p2, color=(255, 0, 0), thickness=5)
                image_copy = cv2.line(image_copy, p2, p3, color=(255, 0, 0), thickness=5)
                image_copy = cv2.line(image_copy, p3, p4, color=(255, 0, 0), thickness=5)
                image_copy = cv2.line(image_copy, p4, p1, color=(255, 0, 0), thickness=5)
            plt.imsave("Hightlighted.png", image_copy)
            scale_percent = 10 
            width = int(image_copy.shape[1] * scale_percent / 100)
            height = int(image_copy.shape[0] * scale_percent / 100)
            dim = (width, height)
            image = cv2.resize(image_copy, dim, interpolation = cv2.INTER_AREA)        ///////////   RESIZING THE IMAGE /////////
            cv2.imshow("Matched image",image)
            plt.show()
            cv2.waitKey(0)
        c=1
if(c==0):
	print("Not found")


