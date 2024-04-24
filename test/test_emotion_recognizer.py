import _init_path
from emotion_recognizer.emotion_recognizer import EmotionRecognizer
import cv2

emotionRecog = EmotionRecognizer()
image_path = 'face1.jpg'
image = cv2.imread(image_path)
result = emotionRecog.recognize_emotion_from_image(image)
print(result)