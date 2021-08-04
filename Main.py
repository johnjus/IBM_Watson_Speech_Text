from ibm_watson import SpeechToTextV1 
import json
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson import LanguageTranslatorV3

def speechToText():
    #url to connect to the api
    url_s2t = "#####"
    #unique key to acces the api
    iam_apikey_s2t= "####"

    #setting up the api to be ready to be called when needed
    authenticator = IAMAuthenticator(iam_apikey_s2t)
    s2t = SpeechToTextV1(authenticator=authenticator)
    s2t.set_service_url(url_s2t)

    #the audio file we are translating from audio to text
    filename='PolynomialRegressionandPipelines.mp3'

    #opening the audio file and sending it to the api
    with open(filename, mode='rb') as wav:

        response = s2t.recognize(audio=wav, content_type='audio/mp3')

    #dictionary for the translation from text to speech
    #includes the confidence and what ibm watson believes the audio file is saying
    #---------
    #print(response.result())
    #---------


    #from here we can obtain specific sections of the translated audio file

    text = response.result['results'][0]['alternatives'][0]['transcript']

    #goes into the the dictionary grabs results at 0
    #then inside results grabds alternatives at 0
    #inside alternatives we grab the transcript which contains the string version of a specified section of the audio file
    return text

print(speechToText())
text = speechToText()
#output - in this video we will cover polynomial regression and pipelines

def languageTranslation(text):
    #url to connect to the api
    url_lt=''
    #api key
    apikey_lt=''
    #version we want to use
    version_lt=''
    authenticator = IAMAuthenticator(apikey_lt)
    language_translator = LanguageTranslatorV3(version=version_lt,authenticator=authenticator)
    language_translator.set_service_url(url_lt)
    #translating from english to spanish
    translation_response = language_translator.translate(text=text, model_id='en-es')
    translation=translation_response.get_result()
    spanish_translation =translation['translations'][0]['translation']
    print(spanish_translation)
languageTranslation(text)

#output - en este vídeo cubriremos la regresión polinómica y las tuberías
