__module_name__ = "hexchat-Translate Script"
__module_version__ = "1.0"
__module_description__ = "Translates messages to Korean using Google Cloud Translation API"

import hexchat
import requests

# Google Cloud Translation API 설정
GOOGLE_CLOUD_API_KEY = '~~~~~~~~'
API_ENDPOINT = 'https://translation.googleapis.com/language/translate/v2'

def translate_to_korean(text):
    params = {
        'q': text,
        'target': 'ko',
        'format': 'text',
        'key': GOOGLE_CLOUD_API_KEY
    }

    response = requests.get(API_ENDPOINT, params=params)
    result = response.json()

    if 'data' in result and 'translations' in result['data'] and len(result['data']['translations']) > 0:
        return result['data']['translations'][0]['translatedText']
    else:
        return None

def on_message(word, word_eol, userdata):
    user = word[0]
    original_message = word[1]
    translated_message = translate_to_korean(original_message)


    if translated_message:
        hexchat.prnt(f"<{user}>  ↱{translated_message}")

hexchat.hook_print('Channel Message', on_message)
hexchat.hook_print('Private Message', on_message)
hexchat.hook_print('Private Message to Dialog', on_message)

hexchat.prnt("Auto-Translate Script Loaded")
