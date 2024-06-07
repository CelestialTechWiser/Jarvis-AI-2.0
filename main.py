import openai
import requests
import wikipedia
import speech_recognition as sr
import pyttsx3
from datetime import datetime
import webbrowser

openai.api_key = 'Your API Key'

def ask_chatgpt(question):
    response = openai.Completion.create(
        model="gpt-3.5-turbo",
        prompt=question,
        max_tokens=50
    )
    return response.choices[0].text.strip()

def search_wikipedia(query):
    try:
        result = wikipedia.summary(query, sentences=2)
        return result
    except wikipedia.exceptions.DisambiguationError as e:
        return "Wikipedia found multiple matches. Please be more specific."
    except wikipedia.exceptions.PageError:
        return "Wikipedia page not found."

def get_gemini_balance():
    url = "https://api.gemini.com/v1/balances"
    headers = {"Content-Type": "application/json", "X-GEMINI-APIKEY": gemini_api_key}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        balance_info = response.json()
        return balance_info
    else:
        return "Error accessing Gemini API."

def ask_groq(question):
    url = "https://console.groq.com/keys"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {groq_api_key}"
    }
    data = {
        "question": question
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        return response.json().get('answer', 'Sorry, I could not find an answer.')
    else:
        return "Error accessing Groq API."

def speak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    for voice in voices:
        if "david" in voice.name.lower() and "desktop" in voice.name.lower():
            engine.setProperty('voice', voice.id)
            break
    engine.say(text)
    engine.runAndWait()

def main():
    print("I am Jarvis a virtual artificial inteliigence made by Mohammad Ambisat")
    speak("I am Jarvis a virtual artificial inteliigence made by Mohammad Ambisat")

    paused = False

    while True:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            audio = r.listen(source)

        try:
            user_input = r.recognize_google(audio)
            print("You:", user_input)

            if user_input.lower() in ['exit', 'bye', 'quit', 'close']:
                print("Sure sir, Feel free to ask if any more queries")
                speak("Sure sir, Feel free to ask if any more queries")
                break

            if user_input.lower() == 'stop for a moment':
                paused = True
                print("Okay Sir")
                speak("Okay Sir")

            elif user_input.lower() == 'jarvis are you there' and paused:
                paused = False
                print("Yes sir, How may I help you ?")
                speak("Yes sir, How may I help you ?")
                

            elif not paused:
                if user_input.lower().startswith('Jarvis ask computer'):
                    user_question = user_input[len('Jarvis ask computer'):].strip()
                    if user_question:
                        response = ask_groq(user_question)
                        print("Jarvis:", response)
                        speak(response)
                    else:
                        print("Jarvis: Sure sir, What would you like to ask?")
                        speak("Sure sir, What would you like to ask?")
                
                elif user_input.lower().startswith('jarvis'):
                    user_question = user_input[7:].strip()
                    if user_question:
                        response = ask_chatgpt(user_question)
                        print("Jarvis:", response)
                        speak(response)
                    else:
                        print("Jarvis: Yes, sir?")
                        speak("Yes, sir?")

                elif 'gemini' in user_input.lower():
                    balance_info = get_gemini_balance()
                    print("Jarvis:", balance_info)
                    speak(balance_info)

                elif 'date' in user_input.lower():
                    current_date = datetime.now().strftime("%A, %B %d, %Y")
                    print("Jarvis: Today's date is", current_date)
                    speak("Today's date is " + current_date)

                elif 'time' in user_input.lower():
                    current_time = datetime.now().strftime("%I:%M %p")
                    print("Jarvis: The current time is", current_time)
                    speak("The current time is " + current_time)

                elif 'open chrome' in user_input.lower():
                    webbrowser.open("https://www.google.com")

                elif 'open youtube' in user_input.lower():
                    webbrowser.open("https://www.youtube.com")

                elif 'open edge' in user_input.lower():
                    webbrowser.get("C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe %s").open_new_tab("https://www.microsoft.com")

                elif 'open calculator' in user_input.lower():
                    webbrowser.open("calc.exe")

                elif 'launch speed test' in user_input.lower():
                    webbrowser.open("https://www.speedtest.net")
                    
                else:
                    response = search_wikipedia(user_input)
                    print("Jarvis:", response)
                    speak(response)

        except sr.UnknownValueError:
            print("Sorry, I didn't catch that. Could you please repeat?")
            speak("Sorry, I didn't catch that. Could you please repeat?")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
            speak("Could not request results from Google Speech Recognition service")

if __name__ == "__main__":
    main()
