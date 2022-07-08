from PIL import Image
import pytesseract

img_kor = Image.open('./image/img_kor.png')
img_eng = Image.open('./image/img_eng.png')
img_test = Image.open('./image/test.png')

text = pytesseract.image_to_string(img_eng, lang='eng')
print(text)

text = pytesseract.image_to_string(img_kor, lang='kor')
print(text)

text = pytesseract.image_to_string(img_test, lang='kor')
print(text)