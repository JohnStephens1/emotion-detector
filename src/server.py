"""runs the web application"""
from flask import Flask, render_template, request
from src.emotion_detection import emotion_detection


app = Flask(
    "Emotion Detector",
    template_folder="third_party/templates",
    static_folder="third_party/static"
)


def get_fancy_output(input_text, emotion_dict):
    """formats the response to be clean and readable"""
    prettified_emotion_dict = {'\n'.join([f"{key}: {val:.3f}%" for key, val in emotion_dict['emotion_dict'].items()])}

    fancy_output = f"""
    The dominant emotion for the given text is {emotion_dict['dominant_emotion']}.\n\n
    Context:\n\n
    Prompt:\n
    {input_text}\n\n
    Full Eval:\n
    {prettified_emotion_dict}
    """

    return fancy_output


@app.route("/emotionDetector")
def emotion_detector_flask():
    """handles the flask routing, gets emotion dict based on query and returns formatted response"""
    text = request.args.get('textToAnalyze')
    emotion_dict = emotion_detection.get_emotion_eval(text)

    if not emotion_dict:
        return "couldn't get a response"

    fancy_response = get_fancy_output(text, emotion_dict)

    return fancy_response


@app.route("/")
def render_index_page():
    """renders the flask index page"""
    return render_template('index.html')


def run_server():
    app.run(host="0.0.0.0", port=5000)
