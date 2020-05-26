import pytesseract
import cv2


if __name__ == "__main__":
    img = cv2.imread('test.png')
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    result = pytesseract.image_to_data(img, lang='eng', nice=0, output_type=pytesseract.Output.DICT)
    print(result)
