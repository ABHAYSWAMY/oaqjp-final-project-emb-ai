"""
Flask application for handling emotion detection requests.
Uses emotion_detector() to analyze user-submitted text
and returns formatted emotional analysis results.
"""

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")


@app.route("/emotionDetector")
def emo_detector():
    """
    Flask route to process emotion detection requests.
    Extracts text from query parameters, validates input,
    calls the emotion_detector function, and formats the response.

    Returns:
        str: A formatted message containing emotion scores or an error message.
    """
    text_to_analyze = request.args.get("textToAnalyze")

    # Handle case where the user provides no input
    if not text_to_analyze:
        return "Invalid text! Please try again!"

    result = emotion_detector(text_to_analyze)

    # Handle case where detector returns None values
    if result["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    anger = result["anger"]
    disgust = result["disgust"]
    fear = result["fear"]
    joy = result["joy"]
    sadness = result["sadness"]
    dominant_emotion = result["dominant_emotion"]

    response_text = (
        "For the given statement, the system response is "
        f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
        f"'joy': {joy} and 'sadness': {sadness}. "
        f"The dominant emotion is {dominant_emotion}."
    )

    return response_text


@app.route("/")
def home_page():
    """
    Renders the homepage of the Emotion Detector application.

    Returns:
        str: The HTML content of the homepage.
    """
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    