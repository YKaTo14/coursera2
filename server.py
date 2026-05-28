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
