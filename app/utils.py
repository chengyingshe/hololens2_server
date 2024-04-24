import base64
import io
import json
import os
import sys
import numpy as np
from PIL import Image, ImageOps

PROJ_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(PROJ_DIR)
from server_client.server_client import Server, Client

parameters = {
    'temp_file': {
        'image': os.path.join(PROJ_DIR, 'temp/tmp_image.jpg'),
        'audio': os.path.join(PROJ_DIR, 'temp/tmp_audio.wav')
    },
    'port': {
        'ocr': 7878,
        'speech_recognition': 7979,
        'face_emotion_recognition': 7070,
    },
    'test_data': {
        'ocr': {  # ocr
            "data": {
                "lines": [
                    {
                        "text": "xxx",
                        "confidence": 0.612,
                        "position": [[25,  7],
                                    [72,  7],
                                    [72, 39],
                                    [25, 39]]
                    }
                ]
            }
        },
        'face_emotion_recognition': {  #face_emotion_recognition
            "data": {
                "emotion": "happy",
                "confidence": 0.98
            }
        },
        'speech_recognition': {  #speech_recognition
            "data": {
                "text": "识别到的结果是xxxx"
            }
        }
    }
}

def save_file_str_to(f_str: str, to_path: str, flip=False):
    dirname = os.path.dirname(to_path)
    if not os.path.exists(dirname):
        os.makedirs(dirname, exist_ok=True)
    image = Image.open(io.BytesIO(base64.b64decode(f_str))).convert('L')
    if flip:
        image = Image.fromarray(np.flipud(np.array(image))) # 将图片转换为灰度格式并上下翻转
    image.save(to_path, format='JPEG')
    
def cvt_ocr_result_to_json(result, to_str=False):
    data_obj = {
        "data": {
            "lines": []
        }
    }
    for line in result:
        line_obj = {
            "text": line[1],
            "confidence": float(line[2]),
            "position": [[float(line[0]), float(line[1])] for line in line[0]]  # [x1, y1, x2, y2]
        }
        data_obj["data"]["lines"].append(line_obj)
    if to_str: data_obj = json.dumps(data_obj)
    return data_obj

def cvt_fer_result_to_json(result, to_str=False):
    data_obj = { "data": {} }
    if result[0]:
        data_obj["data"] = {
            "emotion": result[0],
            "confidence": float(result[1])
        }
    if to_str: data_obj = json.dumps(data_obj)
    return data_obj

def cvt_sr_result_to_json(result, to_str=False):
    data_obj = { "data": {} }
    if result[0]:
        data_obj["data"] = {
            "text": result
        }
    if to_str: data_obj = json.dumps(data_obj)
    return data_obj