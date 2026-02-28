"""
This module provides a Flask-based web application for emotion detection.
It analyzes text input and returns scores for various emotions.
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_detection():
    """
    Analyzes the text provided in the request arguments and returns
    emotion scores and the dominant emotion.
    """
    text_to_analyze = request.args.get("textToAnalyze")
    response = emotion_detector(text_to_analyze)

    if response["dominant_emotion"] is None:
        return "Invalid text! Please try again!."

    return (
        f"For the given statement, the system response is 'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, 'fear': {response['fear']}, "
        f"'joy': {response['joy']}, "
        f"and 'sadness': {response['sadness']}. The dominant emotion "
        f"is {response['dominant_emotion']}."
    )

@app.route("/")
def render_index_page():
    """
    Renders the main index page of the application.
    """
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
