
"""Emotion detection module using Watson NLP API."""

import json
import requests


def emotion_detector(text_to_analyze):
    """Analyze text and return emotion scores."""

    # Define the API URL
    url = (
        "https://sn-watson-emotion.labs.skills.network/v1/"
        "watson.runtime.nlp.v1/NlpService/EmotionPredict"
    )

    # Create the request payload
    myobj = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    # Define API headers
    header = {
        "grpc-metadata-mm-model-id":
        "emotion_aggregated-workflow_lang_en_stock"
    }

    # Default response for invalid input
    empty_result = {
        "anger": None,
        "disgust": None,
        "fear": None,
        "joy": None,
        "sadness": None,
        "dominant_emotion": None
    }

    # Send request to Watson API
    response = requests.post(
        url,
        json=myobj,
        headers=header,
        timeout=30
    )

    # Task 7: Handle HTTP 400 error
    if response.status_code == 400:
        return empty_result

    # Handle other unsuccessful responses
    if response.status_code != 200:
        return empty_result

    # Convert JSON response to dictionary
    formatted_response = json.loads(response.text)

    # Extract emotion predictions safely
    predictions = formatted_response.get(
        "emotionPredictions"
    )

    if not predictions:
        return empty_result

    emotions = predictions[0]["emotion"]

    # Extract individual emotion scores
    anger_score = emotions["anger"]
    disgust_score = emotions["disgust"]
    fear_score = emotions["fear"]
    joy_score = emotions["joy"]
    sadness_score = emotions["sadness"]

    # Identify dominant emotion
    dominant_emotion = max(
        emotions,
        key=emotions.get
    )

    # Return formatted output
    return {
        "anger": anger_score,
        "disgust": disgust_score,
        "fear": fear_score,
        "joy": joy_score,
        "sadness": sadness_score,
        "dominant_emotion": dominant_emotion
    }
