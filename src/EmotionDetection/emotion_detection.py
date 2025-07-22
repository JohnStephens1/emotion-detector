import requests
import json
from pprint import pprint


def raw_emo_getting(text):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    text_request = { "raw_document": { "text": text } }
    response = requests.post(url, json=text_request, headers=headers)

    if response.status_code == 200:
        return response.text
    else:
        return "{}"


def emotion_detector(text):
    response = json.loads(raw_emo_getting(text))

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


def get_max_emo(le_dict):
    emo = ""
    last_val = 0

    for key, val in le_dict.items():
        if val > last_val:
            emo = key
            last_val = val
        
    return emo, last_val



emotion_detector("my name eh jeff")
emotion_detector("")
