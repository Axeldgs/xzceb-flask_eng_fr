import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator("jTx0lfzRnuSr29VMy71o-NVBJHfm7Mps5SetDP7hxwEo")
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url("https://api.us-south.language-translator.watson.cloud.ibm.com/instances/7a06e623-0180-4555-81bd-b4953c76d16e")

def english_to_french(english_text):
    translation = language_translator.translate(english_text, model_id='en-fr').get_result()
    french_text= translation['translations'][0]['translation']
    return french_text

def french_to_english(french_text):
    translation = language_translator.translate(french_text, model_id='fr-en').get_result()
    english_text= translation['translations'][0]['translation']
    return english_text
