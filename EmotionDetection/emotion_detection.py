import requests
import json

def emotion_detector(text_to_analyse):

    # Handle empty input BEFORE sending API request
    if not text_to_analyse or text_to_analyse.strip() == "":
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    # API endpoint
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    # Request body
    myobj = { "raw_document": { "text": text_to_analyse } }

    # Header
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Call the Watson NLP Emotion API
    response = requests.post(url, json=myobj, headers=header)

    # Handle API error (status_code = 400)
    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    # Parse JSON response
    response_data = json.loads(response.text)

    # Extract emotion scores
    emotions = response_data['emotionPredictions'][0]['emotion']

    anger = emotions.get('anger')
    disgust = emotions.get('disgust')
    fear = emotions.get('fear')
    joy = emotions.get('joy')
    sadness = emotions.get('sadness')

    # Determine dominant emotion
    dominant_emotion = max(emotions, key=emotions.get)

    # Return formatted dictionary
    return {
        'anger': anger,
        'disgust': disgust,
        'fear': fear,
        'joy': joy,
        'sadness': sadness,
        'dominant_emotion': dominant_emotion
    }

