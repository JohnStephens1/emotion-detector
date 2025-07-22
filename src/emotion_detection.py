# URL: 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
# Headers: {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
# Input json: { "raw_document": { "text": text_to_analyse } }

from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Define constants
URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
HEADERS = {'grpc-metadata-mm-model-id': 'emotion_aggregated-workflow_lang_en_stock'}

@app.route('/analyze', methods=['POST'])
def emotion_detector():
    data = request.get_json()
    
    # Make sure 'text' is provided
    if not data or 'text' not in data:
        return jsonify({'error': 'Missing "text" in request'}), 400
    
    # Prepare the input JSON for the external request
    input_json = {
        'raw_document': {
            'text': data['text']
        }
    }

    # Make the request to the external service
    response = requests.post(URL, headers=HEADERS, json=input_json)

    # Return the 'text' attribute of the response
    return response.text  # <- This is what the instruction is asking for

# To run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
