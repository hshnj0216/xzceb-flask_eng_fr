import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

#language_translator.set_disable_ssl_verification(True)

def english_to_french(english_text):
    """Translates from english to french"""
    #checks the input for null or empty string
    if english_text is None:
        return 'Cannot translate null or empty text'
    #assigns value to french_text variable using the
    #custom translate language function
    french_text = translate_language(english_text, 'en-fr')
    return french_text['translations'][0]['translation']

def french_to_english(french_text):
    """Translates from french to english"""
    #checks the input for null or empty string
    if french_text is None:
        return 'Cannot translate null or empty text'
    #assigns value to english_text variable using the
    #custom translate language function
    english_text = translate_language(french_text, 'fr-en')
    return english_text['translations'][0]['translation']

def translate_language(text_to_translate, translator_model_id):
    """Translates text based on the translator model id"""
    #calls the translate method and returns the translated text
    return language_translator.translate(
    text=text_to_translate,
    model_id=translator_model_id).get_result()
    