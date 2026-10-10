
"""
Emotion Detection Flask Application.

This module provides a web interface for detecting emotions
in user-provided text using the EmotionDetection package.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector


app = Flask(__name__)


@app.route("/emotionDetector")
def detect_emotion():
    """
    Analyze the text provided by the user and display
    the emotion scores and dominant emotion.

    Returns:
        str: Formatted emotion analysis result or error message.
    """
    text_to_analyze = request.args.get("textToAnalyze", "")

    response = emotion_detector(text_to_analyze)

    if response["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    anger = response["anger"]
    disgust = response["disgust"]
    fear = response["fear"]
    joy = response["joy"]
    sadness = response["sadness"]
    dominant_emotion = response["dominant_emotion"]

    return (
        "For the given statement, the system response is "
        f"'anger': {anger}, "
        f"'disgust': {disgust}, "
        f"'fear': {fear}, "
        f"'joy': {joy} and "
        f"'sadness': {sadness}. "
        f"The dominant emotion is {dominant_emotion}."
    )


@app.route("/")
def render_index_page():
    """
    Render the home page of the emotion detection application.

    Returns:
        str: Rendered HTML template.
    """
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="localhost", port=5000)
