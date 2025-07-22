"""handles emotion detection logic"""


import requests
import json


URL = r'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
HEADERS = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}


def get_post_response(text, url=URL, headers=HEADERS):
    """
    posts a request containing the provided text.
    the url and header default to the relevant emotion prediction model.
    returns:
    - the response text, if the request was successful
    - an empty string otherwise
    """

    text_request = {"raw_document": {"text": text}}
    response = requests.post(url, json=text_request, headers=headers)

    if response.status_code == 200:
        return response.text
    else:
        return ""


def get_emotion_eval(text):
    """
    evaluates emotions associated with given string.
    returns either:
    - the emotion dictionary, containing the likelihood of different emotions
    - an empty dict, if no response was received
    """

    result_dict = {}
    response_text = get_post_response(text)

    if not response_text:
        print("couldn't get a response")
        return {}

    emotion_dict = json.loads(response_text)['emotionPredictions'][0]['emotion']
    dominant_emotion = max(emotion_dict, key=emotion_dict.get)

    result_dict['emotion_dict'] = emotion_dict
    result_dict['dominant_emotion'] = dominant_emotion

    return result_dict
