"""runs the web application"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector


app = Flask("Emotion Detector")


@app.route("/emotionDetector")
def emotion_detector_fask():
    """handles the flask routing, gets emotion dict based on query and returns formatted response"""
    text = request.args.get('textToAnalyze')
    le_dict = emotion_detector(text)

    if le_dict['dominant_emotion'] is None:
        return "Invalid text! Please try again!."

    return (
        "For the given statement, the system response is "
        f"'anger': {le_dict['anger']}, "
        f"'disgust': {le_dict['disgust']}, "
        f"'fear': {le_dict['fear']}, "
        f"'joy': {le_dict['joy']} "
        f"and 'sadness': {le_dict['sadness']}. "
        f"The dominant emotion is {le_dict['dominant_emotion']}"
    )


@app.route("/")
def render_index_page():
    """renders the flask index page"""
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
