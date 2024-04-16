from flask import Flask, render_template, request
from utils import *
from chineseocr_lite.model import OcrHandle
from emotion_recognizer.emotion_recognizer import EmotionRecognizer
from speech_recognizer.speech_recognizer import SpeechRecognizer

api_list = parameters['port'].keys()

app = Flask(__name__)
ocrHandle = OcrHandle()
emotionRecognizer = EmotionRecognizer()
speechRecognizer = SpeechRecognizer()


@app.route('/')
def index():
    return render_template('index.html', api_list=api_list)

@app.route('/demo/<api>')
def demo(api):
    if api in api_list:
        return render_template('demo.html', api=api)
    index()

@app.route('/<api>', methods=['POST'])
def run_api(api):
    if api in api_list:
        file_str = request.json.get('file')
        if file_str is None:
            return 'error'
            
        type = 'audio' if api == 'speech_recognition' else 'image'
        output_path = parameters['temp_file'][type]
        save_file_str_to(file_str, output_path)
        print(f'save file to: {output_path}')
        # 将保存到本地的文件的路径发送给识别程序
        if api == 'ocr':
            result = ocrHandle.text_predict_from_image_path(output_path)
            result = cvt_ocr_result_to_json(result)
        elif api == 'speech_recognition':
            result = speechRecognizer.recognize_audio(output_path)
            result = cvt_sr_result_to_json(result)
        elif api == 'face_emotion_recognition':
            result = emotionRecognizer.recognize_emotion_from_path(output_path)
            result = cvt_fer_result_to_json(result)
        else:
            return 'invalid api'

        return result

    index()

app.run('0.0.0.0', debug=True)