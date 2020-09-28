# importing speech recognition package from google api 
import speech_recognition as sr  
import playsound # to play saved mp3 file 
from gtts import gTTS # google text to speech 
import os # to save/open files 
import requests # to get API responses
import json # to get detailed info from API responses
 
num = 1
def assistant_speaks(output): 
    global num 
  
    # num to rename every audio file  
    # with different name to remove ambiguity 
    num += 1
    print("Movie Assistant : ", output) 
  
    toSpeak = gTTS(text = output, lang ='en', slow = False) 
    # saving the audio file given by google text to speech 
    file = str(num)+".mp3"  
    toSpeak.save(file) 
      
    # playsound package is used to play the same file. 
    playsound.playsound(file, True)  

    # TODO: NOT COMMENT THIS, BUT NOW I WANT TO KEEP THE AUDIOS
    #os.remove(file) 

    
def get_audio(): 
  
    rObject = sr.Recognizer() 
    audio = '' 
  
    with sr.Microphone() as source: 
        print("Speak (5sec to speak)...") 
          
        # recording the audio using speech recognition 
        audio = rObject.listen(source, phrase_time_limit = 5)
  
    try: 
  
        text = rObject.recognize_google(audio, language ='en-US') 
        print("You : ", text) 
        return text 
  
    except: 
  
        assistant_speaks("Could not understand you, say again") 
        return get_audio()
  
  
if __name__ == "__main__": 
    assistant_speaks("Hello, I am a movie assistant. What's your name?") 
    name = get_audio()
    assistant_speaks("Hello, " + name + '.') 
      
    while(1): 
  
        assistant_speaks("What movie do you want to check?") 
        text = get_audio()
  
        if text == 0: 
            continue
  
        if "exit" in str(text) or "bye" in str(text) or "sleep" in str(text): 
            assistant_speaks("Ok bye, "+ name+'.') 
            break
        else:
            # Go to omdbapi to check movie (we can take info from here to talk about a movie)
            apikey = 'efcac389' #iñaki api key
            response = requests.get(f"http://www.omdbapi.com/?t={text}&apikey={apikey}")
            # As usual in a web
            # 200 – OK. The request was successful.
            # 204 – No Content.
            # 301 – Moved Permanently.
            # 400 – Bad Request. 
            # 401 – Unauthorized. 
            # 403 – Forbidden.
            # 404 – Not Found.
            # 500 – Internal Server Error. 
            if (response.status_code == 200):
                #Find value -> "Ratings":[{"Source":"Internet Movie Database","Value":"8.8/10"},...]
                details_movie = json.loads(response.text)
                rating = float(details_movie['Ratings'][0]['Value'].split("/")[0])
                if (rating < 5.):   
                    assistant_speaks(f"This movie only gets a {rating}, I don't think you like it...") 
                    text = get_audio()
                elif (rating > 5.) and (rating < 8.):
                    assistant_speaks(f"This movie only gets a {rating}, not bad at all...") 
                    text = get_audio()
                else:
                    assistant_speaks(f"OH! This movie gets a {rating}, you should watch it...") 
                    break
            else:
                assistant_speaks("Sorry I can't find this movie") 
                break
  