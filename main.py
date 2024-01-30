import speech_recognition as sr
import os
import pyttsx3
import webbrowser
import openai
import datetime
from config import apikey
import random

chatStr = ""

def chat(text):
    global chatStr
    openai.api_key = apikey
    chatStr += f"usera: {text}\n AI:"

    messages = [
        {"role": "system", "content": "using artificial intelligence"},
        {"role": "user", "content": text},
        {"role": "assistant", "content": ""}
    ]

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    try:
        content = response["choices"][0]["message"]["content"]
        print(content)
        say(content)
        chatStr += f"{content}\n"
        return content
    except KeyError as e:
        print(f"KeyError: {e}. Response structure might be different than expected.")
        print(response)  # Print the response to understand its structure


def myai(prompt):
    openai.api_key = apikey
    msg = f"OpenAI response for prompt: {prompt}\n***********\n\n"

    messages = [
        {"role": "system", "content": "using artificial intelligence"},
        {"role": "user", "content": prompt},
        {"role": "assistant", "content": "write a letter to a friend"}
    ]

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    try:
        content = response["choices"][0]["message"]["content"]
        print(content)
        msg += content

        if not os.path.exists("Openai"):
            os.mkdir("Openai")
        with open(f"Openai/prompt-{random.randint(1, 1000)}", "w") as f:
            f.write(msg)
    except KeyError as e:
        print(f"KeyError: {e}. Response structure might be different than expected.")
        print(response)  # Print the response to understand its structure

def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def input_to_speech():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language = "en-in")
            print(f"user said : {query}")
            return query
        except Exception as e:
            return "sorry some error occured"

if __name__ == '__main__':
    print('PyCharm')
    say("hello welcome")

    while True:
        print("listening---")
        text = input_to_speech()
        sites = [["youtube" , "https://www.youtube.com/"] , ["wikipedia" , "https://www.wikipedia.org/"] , ["google" , "https://www.google.com/"]]
        for site in sites:
            if f"Open {site[0]}".lower() in text.lower():
                say(f"yes openning{site[0]}.....")
                webbrowser.open(site[1])
        if "open music" in text:
                musicPath = r"C:\Users\user Singh\Downloads\town-10169.mp3"
                os.startfile(musicPath)
        elif "the time" in text:
            strfTime = datetime.datetime.now().strftime("%H:%M:%S")
            say(f"the time is {strfTime}")
        elif "open google" in text:
            Google = r"C:\Program Files\Google"
            os.startfile(Google)
        elif "using artificial intelligence".lower() in text.lower():
            myai(prompt=text)
        elif "exit".lower() in text.lower():
            say("bye bye usera see you soon...")
            exit()
        elif "reset chat".lower() in text.lower():
            chatStr = ""
            say("chat reset")
        else:
            print("chatting---")
            chat(text)
