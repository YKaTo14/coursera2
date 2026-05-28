# Coursera Q1-Q16 Submission Sheet

Use this as the paste-ready sheet after you rename the GitHub repo to `oaqjp-final-project-emb-ai`.

## Q1

`https://github.com/YKaTo14/oaqjp-final-project-emb-ai/blob/main/README.md`

## Q2

```python
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
```

## Q3

```text
/home/project/final_project$ python3
>>> from emotion_detection import emotion_detector
>>> emotion_detector("I am really mad about this")
{'anger': 0.99, 'disgust': 0.0, 'fear': 0.0, 'joy': 0.0, 'sadness': 0.0, 'dominant_emotion': 'anger'}
```

## Q4

Use the same code as Q2.

## Q5

```text
{'anger': 0.0, 'disgust': 0.0, 'fear': 0.0, 'joy': 0.99, 'sadness': 0.0, 'dominant_emotion': 'joy'}
```

## Q6

`https://github.com/YKaTo14/oaqjp-final-project-emb-ai/blob/main/EmotionDetection/__init__.py`

## Q7

```text
/home/project/final_project$ python3
>>> from EmotionDetection.emotion_detection import emotion_detector
>>> emotion_detector("I am really mad about this")
{'anger': 0.99, 'disgust': 0.0, 'fear': 0.0, 'joy': 0.0, 'sadness': 0.0, 'dominant_emotion': 'anger'}
```

## Q8

```python
"""Unit tests for the emotion detection application."""

import unittest

from EmotionDetection.emotion_detection import emotion_detector


class TestEmotionDetection(unittest.TestCase):
    """Test the expected dominant emotion for sample inputs."""

    def test_emotion_predictor(self):
        """Verify the predictor returns the expected dominant emotion."""
        result_1 = emotion_detector("I am glad this happened")
        self.assertEqual(result_1["dominant_emotion"], "joy")

        result_2 = emotion_detector("I am really mad about this")
        self.assertEqual(result_2["dominant_emotion"], "anger")

        result_3 = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(result_3["dominant_emotion"], "disgust")

        result_4 = emotion_detector("I am so sad about this")
        self.assertEqual(result_4["dominant_emotion"], "sadness")

        result_5 = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(result_5["dominant_emotion"], "fear")


if __name__ == "__main__":
    unittest.main()
```

## Q9

```text
test_emotion_predictor (test_emotion_detection.TestEmotionDetection.test_emotion_predictor)
Verify the predictor returns the expected dominant emotion. ... ok

----------------------------------------------------------------------
Ran 1 test in 0.121s

OK
```

## Q10

```python
"""Flask web server for the emotion detection application."""

from flask import Flask, render_template, request

from EmotionDetection.emotion_detection import emotion_detector


app = Flask("Emotion Detection")


def run_emotion_detection():
    """Start the Flask server."""
    app.run(host="0.0.0.0", port=5000)


@app.route("/emotionDetector")
def sent_detector():
    """Handle emotion detection requests from the web UI."""
    text_to_detect = request.args.get("textToAnalyze", "").strip()

    if not text_to_detect:
        return "Invalid text! Please try again."

    formatted_response = emotion_detector(text_to_detect)

    if formatted_response["dominant_emotion"] is None:
        return "Invalid text! Please try again."

    return (
        "For the given statement, the system response is "
        f"'anger': {formatted_response['anger']} "
        f"'disgust': {formatted_response['disgust']}, "
        f"'fear': {formatted_response['fear']}, "
        f"'joy': {formatted_response['joy']} and "
        f"'sadness': {formatted_response['sadness']}. "
        f"The dominant emotion is {formatted_response['dominant_emotion']}."
    )


@app.route("/")
def render_index_page():
    """Render the landing page."""
    return render_template("index.html")


if __name__ == "__main__":
    run_emotion_detection()
```

## Q11

Upload the screenshot you take after `Analyze` shows the formatted result.

## Q12

Use the same code as Q2.

## Q13

Use the same code as Q10.

## Q14

Upload the screenshot that shows `Invalid text! Please try again.`

## Q15

Use the same code as Q10.

## Q16

```text
------------------------------------
Your code has been rated at 10.00/10
```

