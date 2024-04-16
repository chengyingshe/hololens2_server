from flask import Flask, render_template, request


app = Flask(__name__)
api_list = ['ocr', 'speech_recognition', 'face_emotion_recognition']
@app.route('/')
def index():
    return render_template('index.html', api_list=api_list)

@app.route('/demo/<api>')
def demo(api):
    return render_template('demo.html', api=api)

@app.route('/<api>', methods=['POST'])
def run_api(api):
    print(f"request: {request.json.get('file')}")
    return f'api: {api}'

app.run('0.0.0.0', debug=True)
