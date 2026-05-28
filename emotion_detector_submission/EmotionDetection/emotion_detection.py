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


def emotion_detector(text_to_analyze):
    """Call the Watson NLP service and return its raw response."""
    payload = {"raw_document": {"text": text_to_analyze}}
    response = requests.post(URL, json=payload, headers=HEADERS)
    response_data = json.loads(response.text)

    if response.status_code == 200:
        return response_data

    if response.status_code == 400:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None,
        }

    return response_data


def emotion_predictor(detected_text):
    """Format Watson NLP output into the structure used by the assignment."""
    if not detected_text:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None,
        }

    if all(value is None for value in detected_text.values()):
        return detected_text

    if detected_text.get("emotionPredictions") is None:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None,
        }

    emotions = detected_text["emotionPredictions"][0]["emotion"]
    dominant_emotion = max(emotions, key=emotions.get)

    return {
        "anger": emotions["anger"],
        "disgust": emotions["disgust"],
        "fear": emotions["fear"],
        "joy": emotions["joy"],
        "sadness": emotions["sadness"],
        "dominant_emotion": dominant_emotion,
    }

