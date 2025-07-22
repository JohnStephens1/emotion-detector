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
    returns:
    - the emotion dictionary, associating likelihood with different emotions.
    - the most likely appropriate emotion as a string
    """

    response_text = get_post_response(text)

    if not response_text:
        print("couldn't get a response")
        return ""

    emotion_dict = json.loads(response)['emotionPredictions'][0]['emotion']
    highest_ranking_emotion = max(emotion_dict, key=emotion_dict.get)

    return emotion_dict, highest_ranking_emotion
