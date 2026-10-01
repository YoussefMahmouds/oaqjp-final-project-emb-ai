"""from flask import Flask, request, render_template"""

from flask import Flask, request, render_template
from EmotionDetection import emotion_detector
app = Flask(__name__)

@app.route("/emotionDetector")
def emotion_detector_route():
    """Analyze the emotion of the provided text."""
    text_to_analyze = request.args.get("textToAnalyze")
    response = emotion_detector(text_to_analyze)
    anger = response["anger"]
    disgust = response["disgust"]
    fear = response["fear"]
    joy = response["joy"]
    sadness = response["sadness"]
    dominant_emotion = response["dominant_emotion"]
    if dominant_emotion is None:
        return "Invalid text! Please try again!"
    return (
    f"For the given statement, the system response is "
    f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
    f"'joy': {joy} and 'sadness': {sadness}. "
    f"The dominant emotion is <b>{dominant_emotion}</b>.")
@app.route("/")
def render_index_page():
    """Render the main application page."""
    return render_template("index.html")
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
