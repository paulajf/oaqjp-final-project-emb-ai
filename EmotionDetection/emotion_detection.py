''' Emotion Detection
    This package exports an emotion analyzer using the Watson NLP libraries.
'''
import json
import requests

def emotion_detector(text_to_analyze):
    ''' This code passes the input text to the the emotion detector.
        It then parses the response to get the label and score if the status_code
        returned is 200. It returns these, and None if the status_code is not 200.
    '''
    host = 'https://sn-watson-emotion.labs.skills.network'
    url = host + '/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    jsonobj = { "raw_document": { "text": text_to_analyze } }

    response = requests.post(url, json = jsonobj, headers = headers, timeout = 5)
    if response.status_code == 400:
        return { "anger" : None, "disgust" : None, "fear" : None,
        "joy" : None, "sadness" : None,  "dominant_emotion" : None }

    formatted_response = json.loads(response.text)
    emotion_dictionary = formatted_response['emotionPredictions'][0]['emotion']
    dominant_emotion = max(emotion_dictionary, key=lambda k: emotion_dictionary[k])
    emotion_dictionary['dominant_emotion'] = dominant_emotion
    return emotion_dictionary
