import requests
import json

def speak(str):
    from win32com.client import Dispatch

    speak = Dispatch('SAPI.SpVoice')

    speak.Speak(str)

if __name__ == '__main__':

    n = 1

    result = requests.get('http://newsapi.org/v2/top-headlines?apiKey=5b3e6e3e3076491aac7da250a1152a4f&sources=the-times-of-india')
    topNews = result.content
    print(topNews)

    parsed = json.loads(topNews)
    listArts = parsed['articles']

    for dictArt in listArts:
        speak(f'News: {n} is ' + dictArt['title'])
        n += 1

    speak('No more top news for the day')



