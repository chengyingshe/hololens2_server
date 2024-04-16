import os
import sys

CUR_DIR= os.path.dirname(os.path.abspath(__file__))

parameters = {
    'model': {
        'face': os.path.join(CUR_DIR, 
                             'models/haarcascade_frontalface_default.xml'),
        'emotion': os.path.join(CUR_DIR, 
                                'models/_mini_XCEPTION.102-0.66.hdf5')
    },
    # 'emotions': ["angry", 
    #              "disgust", 
    #              "scared", 
    #              "happy", 
    #              "sad", 
    #              "surprised", 
    #              "neutral"
    #              ],
    'emotions': ["生气", 
                 "厌恶", 
                 "焦虑", 
                 "高兴", 
                 "悲伤", 
                 "惊讶", 
                 "中性"
                 ]
}