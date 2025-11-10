import requests
import json

def emotion_detector(text_to_analyse):
    """
    Detect emotions in text using Watson NLP library.
    """
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = {"raw_document": {"text": text_to_analyse}}
    
    response = requests.post(url, headers=headers, json=input_json)
    response_dict = json.loads(response.text)
    
    emotions = response_dict['emotionPredictions'][0]['emotion']
    
    # Find dominant emotion
    dominant_emotion = max(emotions, key=emotions.get)
    
    return {
        **emotions,
        'dominant_emotion': dominant_emotion
    }
