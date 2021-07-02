##################################### This  is a virtual AI assistant #######################################################
# created by : Raj Mittal 
# Indian Institute of Information Technology , Lucknow 

# YOU HAVE TO DOWNLOAD ALL THE NECESSARY DEPENDENCIES TO ENSURE THE EXECUTION WITHOUT ANY ERROR

# IF YOU WANT TO KNOW WHAT COMMAND YOU HAVE TO GIVE TO PERFORM TASKS JUST HEAD TO ExecuteTasks() function
# NOTE THAT SOME PATHS ARE MENTIONED ACCORDING TO MY DIRECTORY YOU HAVE TO CHANGE THAT PATH NAME ACCORDINGLY
# THEY ARE IN LINE NO. 175 , 206 ,265 ,274 ,304 ,307
from types import ModuleType
import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import requests
import time
import fitz
import random
import wolframalpha
import cv2
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
todo_list=[]

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe(name):
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak(f"Good Morning")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak(f"I am {name} Sir. Please tell me how may I help you")


def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold=3000 #(if it's too noisy outside)
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):                        # To send email 
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

def intro():
    speak(f'''Allow me to introduce myself. I am an aritificial virtual ai assistant and i am here to assist you with a 
        variety of tasks best i can , 24 hours a day 7 days a week 
        I can do wikipedia search,open applications such as chrome,notepad,your ide ,play music, send a mail, read a pdf
        ,get weather info , get latest news headlines ,create a todo list , get your location ,perform math calculations
        etcetra ''')

def todo():              # to do list tou can update,add or del any task 
    
    speak("tell me sir what should I do update,delete or read")
    print("tell me sir what should I do update,delete or read")
    query_todo=takeCommand().lower()
    if 'update' in query_todo:
        flag=True
        while(flag):
            speak("tell me what to add sir")
            print("tell me what to add sir")
            q_add=takeCommand().lower()
            if 'exit' in q_add:
                speak('ok sir')
                print('ok sir')
                flag=False
            elif q_add in  todo_list:
                speak("it is already added sir")
                print("it is already added sir")
            else:
                speak(f"are you sure you want to add {q_add} to todo list" )
                q_que=takeCommand().lower()
                if "yes" in q_que:
                    todo_list.append(q_add)
                    speak("successfully added sir") 
                    print("successfully added sir")
    elif 'delete' in query_todo:
        flag=True
        while(flag):
            speak("tell me what to delete sir")
            q_del=takeCommand().lower()
            if 'exit' in q_del:
                speak('ok sir')
                flag=False
            if 'delete all' in q_del:
                todo_list.clear()
            try:
                todo_list.remove('q_del')
                speak("successfully deleted sir")
            except:
                speak("its already deleted sir")
    elif 'read' in query_todo:
        for to_do in todo_list:
            print(to_do)
            speak(to_do)
def weather():            # get weateher info 
    api_data = requests.get("http://api.openweathermap.org/data/2.5/weather?" + "appid=" + "8750ba08644e8acf88dba51faac11bca" + "&q=" + "agra").json()

    #for more information go to api.openweathermap.org

    weather_main=api_data["weather"][0]["main"]      #weather
    speak(f"weather today is {weather_main}")
    print(f"weather today is {weather_main}")

    temp=int(api_data["main"]["temp"] - 273.15)     #temperature
    speak(f"and  temperature is {temp} celcius")
    print(f"and  temperature is {temp} celcius")

    hum=int(api_data["main"]["humidity"])             #humidity
    if(hum>=30 and hum<=50):speak("air today is normal humid")
    elif(hum>50):
        speak("It is too humid today")
        print("It is too humid today")
    else:
        speak("It is less humid today")
        print("It is less humid today")

def news():                         
    news_data = requests.get("https://newsapi.org/v2/top-headlines?country=in&apiKey=0b92b97c15b6468b84b8bc6f6c61d902").json()
    articles = news_data["articles"]
    times=5                       # tells 5 news articles you can change how much articles you want to read
    for ar in articles:
        if(times>0):
            speak(ar["title"])
            print(ar["title"])
            time.sleep(1)
            times-=1

def get_location():                           
    ip = requests.get('https://api.ipify.org').text
    data = requests.get(f"https://get.geojs.io/v1/ip/geo/{ip}.json").json()
    city = data["city"]
    country=data["country"]
    speak(f"It might not be accurate but we are in {city} city in {country}country")
    print(f"It might not be accurate but we are in {city} city in {country}country")
    time.sleep(1)
    lon=data["longitude"]
    lat=data["latitude"]
    speak(f"to be precise its longitude coordinates are {lon} and latitude coordinates are {lat}")
    print(f"to be precise its longitude coordinates are {lon} and latitude coordinates are {lat}")

def pdf_read():
    try:
        with fitz.open("daa.pdf") as doc: # enter your pdffile name which you want to read it should be in the current woking directory 
            pages = doc.page_count    
            speak(f"sir this book has {pages} pages tell me which should i read first")
            pg = int(input("enter the page no. "))
            text = ""
            k=1
            for page in doc:
                if(pg==k):text += page.getText()
                k+=1
        # print(text)       
        speak(text)
        
    except:
        speak("sorry sir but i cant find the book in current directory")

def get_answer():      # it can give you answer to basic to advance math calculations and give you answer to your questions
                       # for example you can ask : what is the integration of x^2 or you can ask what is the capital of delhi 
    speak("sir ask what you want to ask")
    question = takeCommand()

    client = wolframalpha.Client("R4RWVY-QQYWL43W8U")
    res = client.query(question)

    answer = next(res.results).text
    print(answer)
    speak(answer)

def face_recognition():                                     # face recognition security system code 
    vid = cv2.VideoCapture(0,cv2.CAP_DSHOW)
    casc = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read("C:\\Users\\Raj mittal\\Desktop\\python\\recognizer\\trainer.yml")

    names=[""]
    with open("names.txt","r") as f:
        lines = f.readlines()
        for line in lines:
            data = line.rstrip("\n")
            names.append(data)

    font = cv2.FONT_HERSHEY_SIMPLEX
    while True:
        check,frame = vid.read()
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        faces = casc.detectMultiScale(gray,1.32,5)
        for x,y,w,h in faces:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,255),2)
            id,accuracy = recognizer.predict(gray[y:y+h,x:x+w])
            if(accuracy<100):
                id = names[id]
                vid.release()
                cv2.destroyAllWindows()
                ExecuteTasks()
                exit
            else :
                id="Unknown face"
            cv2.putText(frame, str(id), (x+5,y-5), font, 1, (255,255,255), 2)
            cv2.putText(frame, str(accuracy), (x+5,y+h-5), font, 1, (255,255,0), 1)
        cv2.imshow("face",frame)
        key = cv2.waitKey(1)
        if(key==27):break
    vid.release()
    cv2.destroyAllWindows()    

def ExecuteTasks():                 # main function that perform all tasks 
    wishMe('david')
    commands=True
    while commands:
    # if 1:
        query = takeCommand().lower()
        print(f"user said :{query}")
        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   

        elif 'play music' in query:
            music_dir = 'C:\\Users\\Raj mittal\\Desktop\\music'      # enter the directory of your music playlist it will pick random songs
            songs = os.listdir(music_dir)    
            os.startfile(os.path.join(music_dir,random.choice(songs)))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open ide' in query:
            codePath = "C:\\Users\\Raj mittal\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"   # enter the path of your ide
            os.startfile(codePath)

        elif 'send email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                speak("sir enter receivers email id")
                to = "receiver@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry sir , I am not able to send this email")

        elif 'change voice' in query:                                               #command to change to female voice 
            engine.setProperty('voice',voices[1].id)
            wishMe('lucy')

        elif 'David' in query:                                              #command to change to male voice
            engine.setProperty('voice',voices[0].id)
            wishMe('david')

        elif 'what can you do' in query:                                       
            intro()

        elif 'to do' in query or 'todo' in query:                           #command to create and update to-do list
            todo()

        elif 'open notepad' in query:                                         # enter the path of your notepad
            path = "C:\\WINDOWS\\system32\\notepad.exe"
            os.startfile(path)
        elif 'open google chrome' in query:
            path = "C:\\Program Files (x86)\\Google\\Chrome\\Application"
            os.startfile(path)
        elif 'weather' in query:
            weather()

        elif 'news' in query:
            speak("wait sir getting latest news")
            news()

        elif 'location' in query:
            get_location()

        elif 'pdf' in query:
            pdf_read()

        elif 'give me answer' in query or 'answer me' in query or 'calculate' in query:
            get_answer()
            
        elif 'exit' in query or 'bye' in query:
            speak("Have a good Day ,sir")
            commands=False


if __name__ == "__main__":

    ExecuteTasks()                                     #comment it to get face recogntion security
    exit()                                             # comment it too

######################################### IF YOU WANT FACE RECOGNITION SECURITY ###########################################

############################## STEPS FOR FACE RECOGNITION###################################
    # 1. go to sample_generator.py and run the code it will just ask your name 
    # 2. go to Model_trainer.py and just run it
    # 3. now the work has been done just uncomment the code part and you are good to go 
    # 4. dont forget to comment the ExecuteTasks() function  
############################## STEPS TO ADD OR DELETE FACE DATA#################################################
    # 1. to add just repeat the steps that you did to first create your face data

    # 2. to delete the face data just go to the names.txt file and remove that name from the list and decrease the number in id.txt by 1
#################################### MAIN CODE UNCOMMENT IT TO RUN FACE RECOGNITION SECURITY SYSTEM#############################
    # speak("hello , I am a virtual AI assistant created by raj mittal , please verify your face id")
    # face_recognition()

   
    
