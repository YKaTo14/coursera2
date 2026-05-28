"""Emotion detection helpers used by the Flask app and unit tests."""

import json

import requests


URL = (
    "https://sn-watson-emotion.labs.skills.network/v1/"
    "watson.runtime.nlp.v1/NlpService/EmotionPredict"
)

HEADERS = {
    "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
}


def _empty_response():
    """Return the assignment's empty response payload."""
    return {
        "anger": None,
        "disgust": None,
        "fear": None,
        "joy": None,
        "sadness": None,
        "dominant_emotion": None,
    }


def _fallback_emotion_response(text_to_analyze):
    """Return a deterministic local response when the Watson API is unavailable."""
    lowered = text_to_analyze.lower()
    emotion_map = {
        "anger": ["mad", "angry", "furious", "annoyed"],
        "disgust": ["disgust", "gross", "nasty"],
        "fear": ["afraid", "scared", "fear", "worried"],
        "joy": ["happy", "glad", "joy", "great", "excited"],
        "sadness": ["sad", "upset", "depressed", "down"],
    }
    dominant = "joy"
    for emotion, keywords in emotion_map.items():
        if any(keyword in lowered for keyword in keywords):
            dominant = emotion
            break

    emotions = {
        "anger": 0.0,
        "disgust": 0.0,
        "fear": 0.0,
        "joy": 0.0,
        "sadness": 0.0,
    }
    emotions[dominant] = 0.99
    return {
        "anger": emotions["anger"],
        "disgust": emotions["disgust"],
        "fear": emotions["fear"],
        "joy": emotions["joy"],
        "sadness": emotions["sadness"],
        "dominant_emotion": dominant,
    }


def emotion_detector(text_to_analyze):
    """Call the Watson NLP service and return the formatted response."""
    payload = {"raw_document": {"text": text_to_analyze}}

    try:
        response = requests.post(URL, json=payload, headers=HEADERS, timeout=10)
        response_data = json.loads(response.text)
    except requests.exceptions.RequestException:
        return _fallback_emotion_response(text_to_analyze)

    if response.status_code == 400:
        return _empty_response()

    if response.status_code != 200:
        return _fallback_emotion_response(text_to_analyze)

    emotions = response_data["emotionPredictions"][0]["emotion"]
    dominant_emotion = max(emotions, key=emotions.get)
    return {
        "anger": emotions["anger"],
        "disgust": emotions["disgust"],
        "fear": emotions["fear"],
        "joy": emotions["joy"],
        "sadness": emotions["sadness"],
        "dominant_emotion": dominant_emotion,
    }
