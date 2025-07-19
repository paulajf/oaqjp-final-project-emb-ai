''' Executing this function initiates the application of emotion
    detection to be executed over the Flask channel and deployed on
    localhost:5000.
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector")
def sent_analyzer():
    ''' This code receives the text from the HTML interface and 
        runs emotion detection over it using emotion_detector()
        function. The output returned shows the scores for each
        emotion and the dominant emotion.
    '''
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    if response['dominant_emotion'] is None:
        return "<strong>Invalid text! Please try again!</strong>"

    first_part = "For the given statement, the system response is"
    emotions = [f"{key}: {value}" for key, value in response.items()]
    second_part = f"{', '.join(emotions[:-1])} and {emotions[-1]}"
    third_part = f"The dominant emotion is <strong>{response['dominant_emotion']}</strong>."

    return first_part + " " + second_part + ". " + third_part

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="localhost", port=5000)
