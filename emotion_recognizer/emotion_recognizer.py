from keras.utils import img_to_array
import cv2
from keras.models import load_model
import numpy as np
from .utils import parameters as er_params

class EmotionRecognizer:
    def __init__(self) -> None:
        self.face_detector = cv2.CascadeClassifier(er_params['model']['face'])
        self.emotion_detector = load_model(er_params['model']['emotion'])

    def recognize_emotion_from_image(self, image):
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        faces = self.face_detector.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, 
                                    minSize=(30,30), flags=cv2.CASCADE_SCALE_IMAGE)
        if len(faces) == 0: return (None, 0)
        faces = sorted(faces, reverse=True, 
                    key=lambda x: (x[2] - x[0]) * (x[3] - x[1]))[0]
        (fX, fY, fW, fH) = faces
        roi = gray[fY:fY + fH, fX:fX + fW]
        roi = cv2.resize(roi, (64, 64))
        roi = roi.astype("float") / 255.0
        roi = img_to_array(roi)
        roi = np.expand_dims(roi, axis=0)
        preds = self.emotion_detector.predict(roi)[0]
        max_index = preds.argmax()
        prob = preds[max_index]
        return (er_params['emotions'][max_index], prob)
    
    def recognize_emotion_from_path(self, image_path: str):
        image = cv2.imread(image_path)
        return self.recognize_emotion_from_image(image)