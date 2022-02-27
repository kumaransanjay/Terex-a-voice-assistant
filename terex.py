from datetime import datetime
from random import random
import random
import webbrowser

import pyttsx3
import datetime
import urllib.request
import re
import speech_recognition as sr
import wikipedia
import os
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def joke():
    speak("ok")
    a="Why do we tell actors to break a leg?"+"  Because every play has a cast"
    b="What do dentists call their x-rays?"+"  Tooth pics!"
    c="Do you want to hear a construction joke?"+" Sorry, I\'m still working on it."
    d="Why do ducks have feathers?"+" To cover their butt quacks!"
    e="What does a nosey pepper do?"+" It gets jalapeño business. "
    f="Why did the bullet end up losing his job?"+" He got fired."
    g="How do you measure a snake?"+" In inches—they don\'t have feet."
    lst1=[a,b,c,d,e,f]
    joke=random.choice(lst1)
    print(joke)
    speak(joke)
    speak("ha ha ha ha ha")
def playinyt():
        speak("what to play in youtube")

        search=mycommand()
           
        space_count=0
        for character in search:
           if character==" ":
             space_count=space_count+1
        number_of_words=space_count+1
        lst=[]
        for i in range(0,number_of_words):
           num=search.split()[i]
           lst.append(num)
        a=len(lst)
        castor=lst[0]+"+"
        for j in range(1,a):
          
            castor=castor+"+"+lst[j]
             
        speak("playing"+search)
        html=urllib.request.urlopen("https://www.youtube.com/results?search_query="+castor)
        video_ids=re.findall(r"watch\?v=(\S{11})",html.read().decode())
        webbrowser.open("https://www.youtube.com/watch?v="+video_ids[0])
def activity():
    speak("I can search for you what do you ask")

  
    

def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning master")
    elif hour>=12 and hour<17:
        speak("Good afternoon master")
    elif hour>=17 and hour<19:
        speak("Good evening master")
    else:
        speak("Good night master")
def whoamI():
    speak("naan thaan TEREX")
   
    speak("what help do you want") 
"""def alarm():
    Hh=int(input("set hour"))
    mm=int(input("set minute"))
    
    hour=int(datetime.datetime.now().hour)
    if (Hh==hour):
        speak("MASTER enthuringa")"""
def mycommand():
    r=sr.Recognizer()
  
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source,duration=0.5)
        # r.energy_threshold()
        print("say anything : ")
        audio= r.listen(source)
        try:
            query = r.recognize_google(audio)
            print(query)
        except:
            print("sorry, could not recognise")
            mycommand()
        return query   

if __name__=="__main__":
   
   wishme()
   whoamI()
 
  
   while True:
       query=mycommand().lower()
       if "wikipedia"in query:
           speak("Searching in wikipeia")
           query=query.replace("wikipedia","")
           results=wikipedia.summary(query,sentences=1)
           speak("according to wikipedia")
           speak(results)
           print(results)
           break;
       elif"tell me a joke"in query:
           joke()
           break;
       elif "tell joke"in query:
           joke()
           break;
       elif "joke"in query:
           joke()
           break;


           
           
       elif"hai"in query:
           speak("hi master")
           break;

       elif "open youtube"in query:
           speak("opening youtube")
           webbrowser.open("youtube.com")
           break;


       elif "open google"in query:
           speak("opening google")
           webbrowser.open("google.com")
           break;

       elif "open geeks for geeks"in query:
           speak("opening geeks for geeks ")
           webbrowser.open_new_tab("geeksforgeeks.org")
           break;
       elif "play music"in query:
           speak("opening music player")
           music="C:\\Users\\home\\Desktop\\songs"
           songs=os.listdir(music)
           print(songs)
           a=random.choice(songs)
           print(a)
           os.startfile(os.path.join(music,a))
           break;
       elif "open whatsapp"in query:
           speak("opening whatsapp")
           webbrowser.open("web.whatsapp.com")
           break;
       elif "play movie"in query:
           speak("playing a movie")
           kmovie="C:\\Users\\home\\Desktop\\sanjay"
           movie="C:\\Users\\home\\Desktop\\movie\\movie"
           
           k=[kmovie,movie]
           c=random.choice(k)
           film=os.listdir(c)
           print(film)
           b=random.choice(film)
           print(b)
           os.startfile(os.path.join(movie,b))
           break;
       elif "open chrome"in query:
           speak("opening chrome" )
           codepath="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe "
           os.startfile(codepath)
           break;
       elif "time now"in query:
           time=datetime.datetime.now().strftime("%H:%M")
           speak("THE TIME IS")
           speak(time)
           break;
       elif "nothing"in query:
           speak("Bye master")
           exit()
       elif "search in youtube"in query:
           speak("what to search in youtube")
           search=mycommand()
           speak("searching for"+search)
           
           webbrowser.open("https://www.youtube.com/results?search_query="+search)
           break;
       elif"play in youtube" in query:

           playinyt()
           break;
       elif "play youtube songs"in query:
           playinyt()
           break;
       elif "play youtube"in query:
           playinyt()
           break;
       elif"youtube"in query:
           playinyt()
           break;
       elif"search in google"in query:
           speak("what to search in google")
           search=mycommand()
           speak("searching for"+search)
           
           webbrowser.open("https://www.google.com/search?q="+search)
           break;





           



