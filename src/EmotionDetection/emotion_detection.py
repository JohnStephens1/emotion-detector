import requests
import json
from pprint import pprint


URL = r'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
HEADERS = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}


def get_post_response(text, url=URL, headers=HEADERS):
    text_request = {"raw_document": {"text": text}}
    response = requests.post(url, json=text_request, headers=headers)

    if response.status_code == 200:
        return response.text
    else:
        return ""


def get_max_emo(le_dict):
    emo = ""
    last_val = 0

    for key, val in le_dict.items():
        if val > last_val:
            emo = key
            last_val = val
        
    return emo, last_val


def emotion_detector(text):
    response = json.loads(get_post_response(text))

    if not response:
        return {
            'anger': None,
            'disgust': None,
            'dominant_emotion': None,
            'fear': None,
            'joy': None,
            'sadness': None
        }

    emotion_dict = response['emotionPredictions'][0]['emotion']

    emo, last_val = get_max_emo(emotion_dict)
    emotion_dict['dominant_emotion'] = emo

    pprint(emotion_dict)
    return emotion_dict


def mainy_boi(text):
    response_text = get_post_response(text)

    if not response_text:
        print("couldn't get a response")
        return ""

    emotion_dict = json.loads(response)['emotionPredictions'][0]['emotion']

    
    
emotion_detector("my name eh jeff")
emotion_detector("")
