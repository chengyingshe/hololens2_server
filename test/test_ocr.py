import _init_path
from chineseocr_lite.model import OcrHandle
import cv2

image_path = 'ocr1.png'
img = cv2.imread(image_path)
ocrHandle = OcrHandle()
result = ocrHandle.text_predict(img)
print(result)

def plot_on_image(img, res, rectangle_color=(0, 255, 0), text_color=(0, 0, 255)):
    img = img.copy()
    for info in res:
        rec, text = info[0], info[1]
        cv2.rectangle(img, rec[0], rec[2], rectangle_color, 1)
        cv2.putText(img, text,
                    (rec[0][0], rec[0][1] + 10), 
                    cv2.FONT_HERSHEY_SIMPLEX, 
                    0.5, text_color, 1)
    return img

img = plot_on_image(img, result)
cv2.imshow('res', img)

cv2.waitKey(0)
cv2.destroyAllWindows