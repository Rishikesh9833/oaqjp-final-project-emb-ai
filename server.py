
"""Flask web application for detecting emotions in text."""

from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask(__name__)


@app.route("/emotionDetector")
def detect_emotion():
    """Analyze the supplied text and return emotion scores."""
    text_to_analyze = request.args.get("textToAnalyze", "")

    response = emotion_detector(text_to_analyze)

    anger = response["anger"]
    disgust = response["disgust"]
    fear = response["fear"]
    joy = response["joy"]
    sadness = response["sadness"]
    dominant_emotion = response["dominant_emotion"]

    return (
        f"For the given statement, the system response is "
        f"'anger': {anger}, 'disgust': {disgust}, "
        f"'fear': {fear}, 'joy': {joy} and "
        f"'sadness': {sadness}. "
        f"The dominant emotion is {dominant_emotion}."
    )


@app.route("/")
def render_index_page():
    """Render the application home page."""
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="localhost", port=5000)
