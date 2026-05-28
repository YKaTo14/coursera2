# Coursera Q1-Q16 Submission Sheet

Use this as a paste-ready checklist for the Emotion Detector final project.

## Q1

`https://github.com/YKaTo14/coursera2/blob/main/README.md`

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
```

## Q3

Run:

```bash
python -m unittest test_emotion_detection.py
```

Paste the terminal output from your machine.

## Q4

Use the same code as Q2.

## Q5

Run:

```bash
python -m unittest test_emotion_detection.py
```

Paste the terminal output showing the formatted output test.

## Q6

`https://github.com/YKaTo14/coursera2/blob/main/EmotionDetection/__init__.py`

## Q7

Run:

```bash
python -c "import EmotionDetection; print('EmotionDetection is a valid package')"
```

Paste the terminal output from your local environment.

## Q8

```python
"""Unit tests for the emotion detection application."""

import unittest

from EmotionDetection.emotion_detection import emotion_detector
from EmotionDetection.emotion_detection import emotion_predictor


class TestEmotionDetection(unittest.TestCase):
    """Test the expected dominant emotion for sample inputs."""

    def test_emotion_predictor(self):
        """Verify the predictor returns the expected dominant emotion."""
        result_1 = emotion_predictor(
            emotion_detector("I am glad this happened")
        )
        self.assertEqual(result_1["dominant_emotion"], "joy")

        result_2 = emotion_predictor(
            emotion_detector("I am really mad about this")
        )
        self.assertEqual(result_2["dominant_emotion"], "anger")

        result_3 = emotion_predictor(
            emotion_detector("I feel disgusted just hearing about this")
        )
        self.assertEqual(result_3["dominant_emotion"], "disgust")

        result_4 = emotion_predictor(
            emotion_detector("I am so sad about this")
        )
        self.assertEqual(result_4["dominant_emotion"], "sadness")

        result_5 = emotion_predictor(
            emotion_detector("I am really afraid that this will happen")
        )
        self.assertEqual(result_5["dominant_emotion"], "fear")


if __name__ == "__main__":
    unittest.main()
```

## Q9

Run:

```bash
python -m unittest test_emotion_detection.py
```

Paste the output that shows all tests passed.

## Q10

```python
"""Flask web server for the emotion detection application."""

from flask import Flask, render_template, request

from EmotionDetection.emotion_detection import emotion_detector
from EmotionDetection.emotion_detection import emotion_predictor


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

    response = emotion_detector(text_to_detect)
    formatted_response = emotion_predictor(response)

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

Upload the screenshot file you create locally:

`C:\Users\javpu\OneDrive\Pictures\Screenshots\6b_deployment_test.png`

## Q12

Use the same code as Q2.

## Q13

Use the same code as Q10.

## Q14

Upload the screenshot file you create locally:

`C:\Users\javpu\OneDrive\Pictures\Screenshots\7c_error_handling_interface.png`

## Q15

Use the same code as Q10.

## Q16

Run:

```bash
pylint server.py
```

Paste the pylint score output from your terminal.

